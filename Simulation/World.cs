using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;

namespace Marte.Simulation
{
    public sealed class ResourceNode
    {
        public int X, Y;
        public string Item = "";
    }

    /// <summary>
    /// Estado de uma construção (1 célula). Uma classe só pra todos os tipos: cada tipo usa os campos que precisa.
    /// Rotation: 0 = Norte (+Y), 1 = Leste (+X), 2 = Sul, 3 = Oeste. Saída sempre na frente.
    /// </summary>
    public sealed class Building
    {
        public int Id;
        public BuildingType Type;
        public int X, Y, Rotation;
        public int Timer;   // miner: progresso do próximo item; conveyor: progresso do item da frente; smelter: progresso da receita
        public int Item;    // miner: item do nó de recurso
        public int Input;   // smelter: itens de entrada no buffer
        public int Output;  // miner/smelter: itens esperando pra sair
        public List<int> Belt = new List<int>();  // conveyor: fila de itens (índice 0 = frente), só ints
        public int[] Stored = new int[0];         // storage: quantidade por índice de item
    }

    /// <summary>
    /// Pilha de itens no chão (conteúdo de uma construção removida). Fica guardada à parte das construções:
    /// não ocupa a célula (dá pra construir em cima e a pilha continua lá) e no máximo 1 pilha por célula (merge).
    /// </summary>
    public sealed class ItemDrop
    {
        public int Id;
        public int X, Y;
        public int[] Items = new int[0];  // quantidade por índice de item
    }

    /// <summary>Tudo que é salvo. O mesmo formato serve pro sync de rede no co-op.</summary>
    public sealed class WorldState
    {
        public long Tick;
        public int NextId = 1;
        public List<ResourceNode> Nodes = new List<ResourceNode>();
        public List<Building> Buildings = new List<Building>(); // sempre ordenada por Id (Ids só crescem)
        public List<ItemDrop> Drops = new List<ItemDrop>();     // idem
    }

    public enum CommandKind { Place, Remove, Rotate, PickUpDrop }

    /// <summary>Comando = dado puro e serializável. Única forma de mudar o estado. No co-op vai pela rede.</summary>
    public sealed class Command
    {
        public CommandKind Kind;
        public BuildingType Type;
        public int X, Y, Rotation, Id;

        public static Command Place(BuildingType type, int x, int y, int rotation) =>
            new Command { Kind = CommandKind.Place, Type = type, X = x, Y = y, Rotation = rotation };
        public static Command Remove(int id) => new Command { Kind = CommandKind.Remove, Id = id };
        public static Command Rotate(int id) => new Command { Kind = CommandKind.Rotate, Id = id };
        public static Command PickUpDrop(int dropId) => new Command { Kind = CommandKind.PickUpDrop, Id = dropId };
    }

    public readonly struct CommandResult
    {
        CommandResult(bool ok, string? reason, int id, int[]? items) { Ok = ok; Reason = reason; EntityId = id; Items = items; }
        public bool Ok { get; }
        public string? Reason { get; }  // código estável, ex. "cell_occupied"
        public int EntityId { get; }
        public int[]? Items { get; }    // PickUpDrop: itens recolhidos (quantidade por índice)
        public static CommandResult Success(int id, int[]? items = null) => new CommandResult(true, null, id, items);
        public static CommandResult Fail(string reason) => new CommandResult(false, reason, 0, null);
    }

    public sealed class World
    {
        public const int TicksPerSecond = 20;
        static readonly int[] Dx = { 0, 1, 0, -1 };
        static readonly int[] Dy = { 1, 0, -1, 0 };

        readonly WorldState s;
        readonly Dictionary<int, Building> byId = new Dictionary<int, Building>();
        readonly Dictionary<(int, int), Building> grid = new Dictionary<(int, int), Building>();

        public World(GameData data, IEnumerable<ResourceNode> nodes) : this(data, new WorldState { Nodes = nodes.ToList() }) { }

        World(GameData data, WorldState state)
        {
            Data = data;
            s = state;
            foreach (var b in s.Buildings) { byId.Add(b.Id, b); grid.Add((b.X, b.Y), b); }
        }

        public GameData Data { get; }
        public long CurrentTick => s.Tick;
        public IReadOnlyList<Building> Buildings => s.Buildings;
        public IReadOnlyList<ResourceNode> Nodes => s.Nodes;
        public IReadOnlyList<ItemDrop> Drops => s.Drops;
        // ponytail: busca linear nas pilhas; indexar por célula quando houver muitas
        public ItemDrop? DropAt(int x, int y) => s.Drops.FirstOrDefault(d => d.X == x && d.Y == y);
        public Building? Get(int id) => byId.TryGetValue(id, out var b) ? b : null;
        public Building? At(int x, int y) => grid.TryGetValue((x, y), out var b) ? b : null;

        public string Save() => JsonSerializer.Serialize(s, GameData.JsonOptions);

        public static World Load(GameData data, string json) =>
            new World(data, JsonSerializer.Deserialize<WorldState>(json, GameData.JsonOptions) ?? throw new InvalidDataException("empty save"));

        public CommandResult Apply(Command c)
        {
            if (c.Kind == CommandKind.Place) return Place(c);
            if (c.Kind == CommandKind.PickUpDrop)
            {
                // Sem inventário ainda: só tira a pilha do mundo e devolve os itens no resultado.
                var d = s.Drops.FirstOrDefault(x => x.Id == c.Id);
                if (d == null) return CommandResult.Fail("unknown_entity");
                s.Drops.Remove(d);
                return CommandResult.Success(d.Id, d.Items);
            }
            var b = Get(c.Id);
            if (b == null) return CommandResult.Fail("unknown_entity");
            if (c.Kind == CommandKind.Rotate)
            {
                b.Rotation = (b.Rotation + 1) % 4;
                return CommandResult.Success(b.Id);
            }
            if (c.Kind == CommandKind.Remove)
            {
                s.Buildings.Remove(b); byId.Remove(b.Id); grid.Remove((b.X, b.Y));
                DropContents(b);
                return CommandResult.Success(b.Id);
            }
            return CommandResult.Fail("unknown_command");
        }

        CommandResult Place(Command c)
        {
            if (!Data.Buildings.ContainsKey(c.Type)) return CommandResult.Fail("unknown_building_type");
            if (c.Rotation < 0 || c.Rotation > 3) return CommandResult.Fail("invalid_rotation");
            if (At(c.X, c.Y) != null) return CommandResult.Fail("cell_occupied");

            var b = new Building { Id = s.NextId, Type = c.Type, X = c.X, Y = c.Y, Rotation = c.Rotation };
            if (c.Type == BuildingType.Miner)
            {
                // ponytail: busca linear nos nós; indexar por célula quando houver milhares
                var node = s.Nodes.FirstOrDefault(n => n.X == c.X && n.Y == c.Y);
                if (node == null) return CommandResult.Fail("miner_needs_resource_node");
                b.Item = Data.ItemIndex(node.Item);
            }
            if (c.Type == BuildingType.Storage) b.Stored = new int[Data.Items.Count];

            s.NextId++;
            s.Buildings.Add(b); byId.Add(b.Id, b); grid.Add((b.X, b.Y), b);
            return CommandResult.Success(b.Id);
        }

        /// <summary>Conteúdo da construção removida vai pro chão na mesma célula (merge se já houver pilha).</summary>
        void DropContents(Building b)
        {
            var items = new int[Data.Items.Count];
            foreach (var it in b.Belt) items[it]++;
            for (int i = 0; i < b.Stored.Length; i++) items[i] += b.Stored[i];
            if (b.Type == BuildingType.Miner) items[b.Item] += b.Output;
            if (b.Type == BuildingType.Smelter)
            {
                var r = Data.Recipes[Data.Buildings[b.Type].Recipe!];
                items[Data.ItemIndex(r.Input)] += b.Input;
                items[Data.ItemIndex(r.Output)] += b.Output;
            }
            if (items.Sum() == 0) return;

            var d = DropAt(b.X, b.Y);
            if (d == null) s.Drops.Add(new ItemDrop { Id = s.NextId++, X = b.X, Y = b.Y, Items = items });
            else for (int i = 0; i < items.Length; i++) d.Items[i] += items[i];
        }

        /// <summary>Avança 1 tick (1/20 s). Ordem fixa por Id → determinístico.</summary>
        public void Tick()
        {
            foreach (var b in s.Buildings) Step(b, Data.Buildings[b.Type]);
            s.Tick++;
        }

        void Step(Building b, BuildingDef def)
        {
            switch (b.Type)
            {
                case BuildingType.Miner:
                    // Buffer cheio = minerador para (back-pressure).
                    if (b.Output < def.Capacity && ++b.Timer >= def.Ticks) { b.Output++; b.Timer = 0; }
                    if (b.Output > 0 && Push(b, b.Item)) b.Output--;
                    break;

                case BuildingType.Conveyor:
                    // Só o item da frente anda; os de trás esperam na fila → vazão de 1 item a cada `Ticks`.
                    if (b.Belt.Count == 0) break;
                    if (b.Timer < def.Ticks) b.Timer++;
                    if (b.Timer >= def.Ticks && Push(b, b.Belt[0])) { b.Belt.RemoveAt(0); b.Timer = 0; }
                    break;

                case BuildingType.Smelter:
                    var r = Data.Recipes[def.Recipe!];
                    if (b.Input >= r.InputCount && b.Output + r.OutputCount <= def.Capacity && ++b.Timer >= r.Ticks)
                    {
                        b.Input -= r.InputCount; b.Output += r.OutputCount; b.Timer = 0;
                    }
                    if (b.Output > 0 && Push(b, Data.ItemIndex(r.Output))) b.Output--;
                    break;
            }
        }

        /// <summary>Tenta entregar `item` pra construção na frente de `from`.</summary>
        bool Push(Building from, int item)
        {
            var to = At(from.X + Dx[from.Rotation], from.Y + Dy[from.Rotation]);
            if (to == null) return false;
            var def = Data.Buildings[to.Type];
            int side = SideTowards(to, from);
            switch (to.Type)
            {
                case BuildingType.Conveyor: // entra por trás ou pelos lados, nunca pela frente
                    if (side == to.Rotation || to.Belt.Count >= def.Capacity) return false;
                    to.Belt.Add(item);
                    return true;
                case BuildingType.Smelter:  // só por trás e só o item da receita
                    var r = Data.Recipes[def.Recipe!];
                    if (side != (to.Rotation + 2) % 4 || item != Data.ItemIndex(r.Input) || to.Input >= def.Capacity) return false;
                    to.Input++;
                    return true;
                case BuildingType.Storage:  // qualquer lado
                    if (to.Stored.Sum() >= def.Capacity) return false;
                    to.Stored[item]++;
                    return true;
                default:
                    return false;
            }
        }

        static int SideTowards(Building to, Building from)
        {
            for (int i = 0; i < 4; i++)
                if (to.X + Dx[i] == from.X && to.Y + Dy[i] == from.Y) return i;
            return -1;
        }
    }
}
