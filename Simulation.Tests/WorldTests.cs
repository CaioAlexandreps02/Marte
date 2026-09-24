using System;
using System.IO;
using System.Linq;
using Marte.Simulation;
using NUnit.Framework;

namespace Marte.Simulation.Tests
{
    public class WorldTests
    {
        const int East = 1;
        static readonly GameData Data = GameData.Load(Path.Combine(TestContext.CurrentContext.TestDirectory, "Data"));
        static BuildingDef Def(BuildingType t) => Data.Buildings[t];
        static RecipeDef Smelt => Data.Recipes[Def(BuildingType.Smelter).Recipe!];

        static World NewWorld() => new World(Data, new[]
        {
            new ResourceNode { X = 0, Y = 0, Item = "iron_ore" },
            new ResourceNode { X = 0, Y = 5, Item = "regolith" },
        });

        static int Place(World w, BuildingType t, int x, int y, int rot = East)
        {
            var r = w.Apply(Command.Place(t, x, y, rot));
            Assert.That(r.Ok, Is.True, r.Reason);
            return r.EntityId;
        }

        static void Run(World w, int ticks) { for (int i = 0; i < ticks; i++) w.Tick(); }

        // minerador(0,0) → esteiras (1..3,0) → fundição(4,0) → esteiras (5..6,0) → baú(7,0)
        static (World w, int storage) Chain()
        {
            var w = NewWorld();
            Place(w, BuildingType.Miner, 0, 0);
            for (int x = 1; x <= 3; x++) Place(w, BuildingType.Conveyor, x, 0);
            Place(w, BuildingType.Smelter, 4, 0);
            for (int x = 5; x <= 6; x++) Place(w, BuildingType.Conveyor, x, 0);
            return (w, Place(w, BuildingType.Storage, 7, 0));
        }

        static int Ingots(World w, int storage) => w.Get(storage)!.Stored[Data.ItemIndex(Smelt.Output)];

        static int TotalItems(World w) =>
            w.Buildings.Sum(b => b.Output + b.Input + b.Belt.Count + b.Stored.Sum()) + w.Drops.Sum(d => d.Items.Sum());

        [Test]
        public void Chain_DeliversIngotsAtBottleneckRate()
        {
            var (w, storage) = Chain();
            // Período (ticks por craft) = o elo mais lento da cadeia, tudo vindo de Data/.
            int period = new[]
            {
                Smelt.Ticks,
                Def(BuildingType.Miner).Ticks * Smelt.InputCount,
                Def(BuildingType.Conveyor).Ticks * Smelt.InputCount,
                Def(BuildingType.Conveyor).Ticks * Smelt.OutputCount,
            }.Max();
            const int crafts = 10;
            int warmup = 20 * period;
            Assume.That((warmup / period + crafts + 1) * Smelt.OutputCount, Is.LessThan(Def(BuildingType.Storage).Capacity), "baú enche antes do fim");

            Run(w, warmup);
            int before = Ingots(w, storage);
            Assert.That(before, Is.GreaterThan(0));
            Run(w, crafts * period);
            Assert.That(Ingots(w, storage) - before, Is.EqualTo(crafts * Smelt.OutputCount));
        }

        [Test]
        public void BackPressure_FullStorageBlocksMiner_WithoutLosingItems()
        {
            var w = NewWorld();
            int miner = Place(w, BuildingType.Miner, 0, 0);
            for (int x = 1; x <= 3; x++) Place(w, BuildingType.Conveyor, x, 0);
            Place(w, BuildingType.Storage, 4, 0);
            var m = w.Get(miner)!;
            var minerDef = Def(BuildingType.Miner);
            int full = Def(BuildingType.Storage).Capacity + 3 * Def(BuildingType.Conveyor).Capacity + minerDef.Capacity;

            // Conservação tick a tick: o total só muda quando o minerador produz, e exatamente +1.
            for (int t = 0; t < (full + 10) * minerDef.Ticks; t++)
            {
                bool produces = m.Output < minerDef.Capacity && m.Timer + 1 >= minerDef.Ticks;
                int before = TotalItems(w);
                w.Tick();
                Assert.That(TotalItems(w) - before, Is.EqualTo(produces ? 1 : 0), $"tick {t}");
            }

            Assert.That(TotalItems(w), Is.EqualTo(full));
            Assert.That(m.Output, Is.EqualTo(minerDef.Capacity));
            Assert.That(w.Buildings.Where(b => b.Type == BuildingType.Conveyor).All(b => b.Belt.Count == Def(BuildingType.Conveyor).Capacity));

            // Travado: o estado não muda mais (só o contador de tick).
            var frozen = w.Save().Replace($"\"Tick\":{w.CurrentTick},", "");
            Run(w, 1000);
            Assert.That(w.Save().Replace($"\"Tick\":{w.CurrentTick},", ""), Is.EqualTo(frozen));
        }

        [Test]
        public void SaveLoad_RestoresIdenticalState()
        {
            var (a, _) = Chain();
            Run(a, 500);
            var json = a.Save();
            Assert.That(a.Buildings.Any(b => b.Belt.Count > 0), "precisa ter itens em trânsito no save");

            var b = World.Load(Data, json);
            Assert.That(b.Save(), Is.EqualTo(json));
            Run(a, 700);
            Run(b, 700);
            Assert.That(b.Save(), Is.EqualTo(a.Save()));
            // IDs continuam do mesmo ponto nos dois mundos
            Assert.That(b.Apply(Command.Place(BuildingType.Storage, 9, 9, 0)).EntityId,
                Is.EqualTo(a.Apply(Command.Place(BuildingType.Storage, 9, 9, 0)).EntityId));
        }

        [Test]
        public void SameCommands_ProduceByteIdenticalSaves()
        {
            string RunScript()
            {
                var (w, _) = Chain();
                Run(w, 1000);
                w.Apply(Command.Rotate(w.At(6, 0)!.Id));   // quebra a saída pro baú
                w.Apply(Command.Remove(w.At(2, 0)!.Id));   // corta a esteira
                w.Apply(Command.Place(BuildingType.Conveyor, 2, 0, East));
                Run(w, 2000);
                return w.Save();
            }
            Assert.That(RunScript(), Is.EqualTo(RunScript()));
        }

        [Test]
        public void Remove_DropsContentsOnGround_MergesAndSurvivesSaveLoad()
        {
            var (w, storage) = Chain();
            Run(w, 500);
            w.Apply(Command.Rotate(w.At(3, 0)!.Id)); // trava a esteira (3,0) → (2,0) enche
            Run(w, 300);
            var belt = w.At(2, 0)!;
            int[] beltItems = new int[Data.Items.Count];
            foreach (var it in belt.Belt) beltItems[it]++;
            int[] stored = (int[])w.Get(storage)!.Stored.Clone();
            Assert.That(beltItems.Sum(), Is.GreaterThan(0));
            Assert.That(stored.Sum(), Is.GreaterThan(0));
            int total = TotalItems(w);

            // Conservação: nada some, e a pilha tem exatamente o conteúdo da construção.
            Assert.That(w.Apply(Command.Remove(belt.Id)).Ok);
            Assert.That(w.Apply(Command.Remove(storage)).Ok);
            Assert.That(TotalItems(w), Is.EqualTo(total));
            var beltDrop = w.DropAt(2, 0)!;
            Assert.That(beltDrop.Items, Is.EqualTo(beltItems));
            Assert.That(w.DropAt(7, 0)!.Items, Is.EqualTo(stored));

            // Construir em cima da pilha é permitido; remover de novo faz merge na mesma pilha.
            int again = Place(w, BuildingType.Conveyor, 2, 0);
            Run(w, 200);
            int onBelt = w.Get(again)!.Belt.Count;
            Assert.That(onBelt, Is.GreaterThan(0));
            int before = beltDrop.Items.Sum();
            w.Apply(Command.Remove(again));
            Assert.That(w.Drops.Count, Is.EqualTo(2));
            Assert.That(w.DropAt(2, 0)!.Id, Is.EqualTo(beltDrop.Id));
            Assert.That(beltDrop.Items.Sum(), Is.EqualTo(before + onBelt));

            var json = w.Save();
            Assert.That(World.Load(Data, json).Save(), Is.EqualTo(json));
        }

        [Test]
        public void PickUpDrop_ReturnsItemsAndRemovesDrop()
        {
            var (w, storage) = Chain();
            Run(w, 500);
            int[] stored = (int[])w.Get(storage)!.Stored.Clone();
            w.Apply(Command.Remove(storage));
            int dropId = w.DropAt(7, 0)!.Id;

            var r = w.Apply(Command.PickUpDrop(dropId));
            Assert.That(r.Ok);
            Assert.That(r.Items, Is.EqualTo(stored));
            Assert.That(w.DropAt(7, 0), Is.Null);
            Assert.That(w.Apply(Command.PickUpDrop(dropId)).Reason, Is.EqualTo("unknown_entity"));
        }

        [Test]
        public void Commands_AreValidated()
        {
            var w = NewWorld();
            int id = Place(w, BuildingType.Conveyor, 3, 3);

            Assert.That(w.Apply(Command.Place(BuildingType.Storage, 3, 3, 0)).Reason, Is.EqualTo("cell_occupied"));
            Assert.That(w.Apply(Command.Remove(999)).Reason, Is.EqualTo("unknown_entity"));
            Assert.That(w.Apply(Command.Rotate(999)).Reason, Is.EqualTo("unknown_entity"));
            Assert.That(w.Apply(Command.Place(BuildingType.Miner, 1, 1, 0)).Reason, Is.EqualTo("miner_needs_resource_node"));
            Assert.That(w.Apply(Command.Place(BuildingType.Storage, 8, 8, 4)).Reason, Is.EqualTo("invalid_rotation"));

            // Rejeição não consome ID.
            Assert.That(Place(w, BuildingType.Miner, 0, 5), Is.EqualTo(id + 1));
            Assert.That(w.Get(id + 1)!.Item, Is.EqualTo(Data.ItemIndex("regolith")));

            Assert.That(w.Apply(Command.Rotate(id)).Ok);
            Assert.That(w.Get(id)!.Rotation, Is.EqualTo(East + 1));
            Assert.That(w.Apply(Command.Remove(id)).Ok);
            Assert.That(w.Get(id), Is.Null);
            Assert.That(w.At(3, 3), Is.Null);
        }
    }
}
