# Marte — instruções para o Claude Code

Jogo de colônia + automação em Marte, 1ª pessoa, Unity 6.3 LTS (URP). Dev solo (Caio) guiando o Claude Code.

## Leia antes de qualquer tarefa
- [DECISOES.md](DECISOES.md) — decisões fechadas (D1–D13). **Não contradizer sem o Caio pedir.**
- [CONHECIMENTO.md](CONHECIMENTO.md) — pesquisa de apoio (engine, MCP, terreno, concorrentes).
- Pilares (D9): toda feature precisa servir a um pilar e não bater com nenhum "não é" (ex: **sem combate**).

## Idioma
- Conversa, docs e comentários de design: Português do Brasil.
- Código (nomes, tipos, métodos, commits técnicos): Inglês.

## Estrutura
```
Simulation/          C# puro (netstandard2.1, C# 9) — lógica do jogo, SEM referência ao Unity
Simulation.Tests/    Testes NUnit da simulação (roda com `dotnet test`, sem Unity)
Data/                Dados de jogo (receitas, máquinas, recursos, stats) em JSON — separados do código
ferramentas/terreno/ Pipeline Python do heightmap real de Jezero → tiles RAW pro Unity
referencias/         Renders, documento original, transcrição de referência
Unity/               (futuro) projeto Unity 6.3 — só apresentação, input, câmera, UI, áudio
```

## Regras de arquitetura (D5 — base pronta pra co-op)
1. **Simulação separada da apresentação.** `Simulation/` nunca usa `UnityEngine`. O Unity só lê o estado e envia comandos.
2. **Toda mudança de estado é um comando** (`BuildCommand`, `RotateCommand`, ...). Nada altera o estado direto.
3. **Tick fixo** (20/s). Nada depende de frame rate ou `Time.deltaTime` dentro da simulação.
4. **Estado 100% serializável** — o mesmo formato serve pro save e pro futuro sync de rede.
5. **Toda entidade tem ID único.** Sem singletons do tipo "o jogador".
6. **Single-player = host com um jogador.**
7. **Determinismo:** simulação de fábrica em inteiros/ponto fixo, sem `float` em lógica que precise bater entre máquinas. Sem `DateTime.Now`/`Random` sem seed dentro da simulação.
8. **Esteiras com muitos itens:** itens são dados em arrays, nunca um objeto por item.

## Compatibilidade com Unity 6.3
- `Simulation/` mira **netstandard2.1 + C# 9**: nada de APIs só de .NET 5+, `record struct`, `required`, file-scoped types, etc. `record class` e `init` exigem cuidado (usar só se compilar no Unity).
- Testes usam **NUnit** (mesmo framework do Unity Test Framework) pra poder migrar.

## Unity (quando existir)
- Nunca editar `.unity`, `.prefab` ou `.meta` à mão. Criar conteúdo via **editor scripts**.
- Stack de IA: plugin oficial `unity-agent-plugin` + `unity` CLI; MCP `CoplayDev/unity-mcp` (telemetria off). **Não usar** AnkleBreaker MCP (licença exige logo no jogo).
- Terreno: MicroSplat Core + "URP for Unity 6.3". Não trocar a versão do Unity.

## Dados de terreno
- Só dados **CC0** (USGS HiRISE/CTX) na área jogável. **Nunca** o mosaico CTX da Murray Lab (NC-ND) nem Blend HRSC (CC BY-SA).
- Arquivos grandes (`*.raw`, `*.tif`, `*.npy`) ficam fora do Git; o script regenera.

## Antes de concluir uma tarefa
- `dotnet build` sem erros nem warnings novos.
- `dotnet test` passando.
- Valores de balanceamento em `Data/`, não hardcoded.

## Git
- **Nunca commitar ou dar push sem aprovação explícita do Caio.**
- Remote: `git@github.com:CaioAlexandreps02/Marte.git` (chave SSH padrão `id_ed25519`).
