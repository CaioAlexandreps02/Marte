using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Marte.Simulation
{
    public enum BuildingType { Miner, Conveyor, Smelter, Storage }

    public sealed class ItemDef
    {
        public ItemDef(string id) { Id = id; }
        public string Id { get; }
    }

    public sealed class RecipeDef
    {
        public RecipeDef(string id, string input, int inputCount, string output, int outputCount, int ticks)
        {
            Id = id; Input = input; InputCount = inputCount; Output = output; OutputCount = outputCount; Ticks = ticks;
        }
        public string Id { get; }
        public string Input { get; }
        public int InputCount { get; }
        public string Output { get; }
        public int OutputCount { get; }
        public int Ticks { get; }
    }

    // Significado de Ticks/Capacity por tipo: ver comentário em Data/buildings.json.
    public sealed class BuildingDef
    {
        public BuildingDef(BuildingType type, int ticks, int capacity, string? recipe)
        {
            Type = type; Ticks = ticks; Capacity = capacity; Recipe = recipe;
        }
        public BuildingType Type { get; }
        public int Ticks { get; }
        public int Capacity { get; }
        public string? Recipe { get; }
    }

    /// <summary>Definições imutáveis carregadas de Data/*.json. Erro de dado = exceção (bug de conteúdo, não de gameplay).</summary>
    public sealed class GameData
    {
        // System.Text.Json (pacote NuGet, alvo netstandard2.0): suporta ctor imutável, campos públicos e
        // comentários em JSON sem escrever parser à mão. No Unity entra como DLL (+ dependências System.Memory etc.).
        // Alternativa se der atrito no Unity/IL2CPP: Newtonsoft (pacote oficial com.unity.nuget.newtonsoft-json).
        public static readonly JsonSerializerOptions JsonOptions = new JsonSerializerOptions
        {
            PropertyNameCaseInsensitive = true,
            IncludeFields = true,
            ReadCommentHandling = JsonCommentHandling.Skip,
            AllowTrailingCommas = true,
            Converters = { new JsonStringEnumConverter() },
        };

        readonly Dictionary<string, int> itemIndex;

        public GameData(IReadOnlyList<ItemDef> items, IEnumerable<RecipeDef> recipes, IEnumerable<BuildingDef> buildings)
        {
            Items = items;
            itemIndex = items.Select((it, i) => (it.Id, i)).ToDictionary(p => p.Id, p => p.i);
            Recipes = recipes.ToDictionary(r => r.Id);
            Buildings = buildings.ToDictionary(b => b.Type);

            foreach (var r in Recipes.Values)
            {
                ItemIndex(r.Input); ItemIndex(r.Output);
                if (r.InputCount <= 0 || r.OutputCount <= 0 || r.Ticks <= 0) throw new InvalidDataException($"recipe '{r.Id}': counts/ticks must be > 0");
            }
            foreach (BuildingType t in Enum.GetValues(typeof(BuildingType)))
            {
                if (!Buildings.TryGetValue(t, out var b)) throw new InvalidDataException($"missing building '{t}'");
                if (b.Capacity <= 0) throw new InvalidDataException($"building '{t}': capacity must be > 0");
                if ((t == BuildingType.Miner || t == BuildingType.Conveyor) && b.Ticks <= 0) throw new InvalidDataException($"building '{t}': ticks must be > 0");
                if (t == BuildingType.Smelter && (b.Recipe == null || !Recipes.ContainsKey(b.Recipe))) throw new InvalidDataException($"building '{t}': unknown recipe '{b.Recipe}'");
            }
        }

        public IReadOnlyList<ItemDef> Items { get; }
        public IReadOnlyDictionary<string, RecipeDef> Recipes { get; }
        public IReadOnlyDictionary<BuildingType, BuildingDef> Buildings { get; }

        public int ItemIndex(string id) =>
            itemIndex.TryGetValue(id, out var i) ? i : throw new InvalidDataException($"unknown item '{id}'");

        public static GameData Load(string dataDir) => new GameData(
            Read<List<ItemDef>>(dataDir, "items.json"),
            Read<List<RecipeDef>>(dataDir, "recipes.json"),
            Read<List<BuildingDef>>(dataDir, "buildings.json"));

        static T Read<T>(string dir, string file) =>
            JsonSerializer.Deserialize<T>(File.ReadAllText(Path.Combine(dir, file)), JsonOptions)
            ?? throw new InvalidDataException($"{file} is empty");
    }
}
