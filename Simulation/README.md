# Simulation — núcleo da simulação (C# puro)

Lógica da fábrica sem Unity (netstandard2.1, C# 9). O Unity só lê `World.Buildings` e manda `Command`s.

## Modelo
- **`World`**: grade de células inteiras, `Tick()` avança 1/20 s (`World.TicksPerSecond`). Só inteiros, ordem fixa por ID → determinístico.
- **Comandos** (`Command.Place/Remove/Rotate`) são dados puros; `world.Apply(cmd)` valida e devolve `CommandResult` (`Ok`, `Reason`, `EntityId`). Rejeição normal não lança exceção.
- **IDs**: contador do mundo (`NextId`), só avança quando um comando dá certo.
- **Construções** (1 célula, 4 rotações: 0=N, 1=L, 2=S, 3=O; saída sempre na frente):
  - `Miner` em nó de recurso → 1 item a cada `ticks`; para quando o buffer enche.
  - `Conveyor` → fila de ints (`Belt`), só o item da frente anda; aceita por trás/lados.
  - `Smelter` → receita fixa; aceita só por trás e só o item da receita.
  - `Storage` → aceita de qualquer lado até `capacity`, contagem por item.
- **Dados** em `Data/*.json` (PROVISÓRIOS). Nada de balanceamento no código.
- **Save**: `world.Save()` → JSON do `WorldState`; `World.Load(data, json)` restaura idêntico.

## Rodar os testes
```
dotnet test
```
