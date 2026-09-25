# Marte — instruções para o Claude Code

Jogo de colônia + automação em Marte, 1ª pessoa, Unity 6.3 LTS (URP). Dev solo (Caio) guiando o Claude Code.

## Leia antes de qualquer tarefa
- [DECISOES.md](DECISOES.md) — decisões fechadas (D1–D14). **Não contradizer sem o Caio pedir.**
- [ROADMAP.md](ROADMAP.md) — ordem de trabalho até o MVP e sessões de design pendentes.
- [HISTORICO.md](HISTORICO.md) — o que foi feito em cada sessão (atualizar ao fim de cada uma).
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
ferramentas/terreno/ Pipeline Python do terreno real (mapa.json, edicoes.json) → tiles RAW + fundo pro Unity
referencias/         Renders, documento original, transcrição de referência
design/              Mecânicas detalhadas (resumo de cada uma em DECISOES.md)
Unity/               Projeto Unity 6.3 URP — só apresentação, input, câmera, UI, áudio (ver Unity/README.md)
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

## Unity
- Versão fixa: **6000.3.25f1 (6.3 LTS)**, URP. Não trocar a versão.
- Nunca editar `.unity`, `.prefab` ou `.meta` à mão. Criar conteúdo via **editor scripts** (menu `Marte/...`).
- **MCP `CoplayDev/unity-mcp`** em modo **stdio** via `.mcp.json` (uvx do winget), telemetria desligada. O Unity precisa estar aberto com a sessão ativa (Window → MCP for Unity). **Não usar** AnkleBreaker MCP (licença exige logo no jogo). `unity` CLI instalado; plugin `unity-agent-plugin` ainda não.
- **Antes de mexer na cena pelo MCP, checar se o editor está em Play** (`mcpforunity://editor/state`): mudanças feitas em Play se perdem.
- Terreno: gerado por `ferramentas/terreno/` e importado por `Marte → Terrain → Import Jezero` + `Marte → Scene → Setup World, Water and Player`. Tiles, horizonte e fundo são **gerados** (fora do Git). Streaming, floating origin e limite do mapa: ver `Unity/README.md`.
- Texturas futuras: MicroSplat Core + "URP for Unity 6.3".

## Dados de terreno
- Só dados **CC0** (USGS HiRISE/CTX/MOLA). **Nunca** o mosaico CTX da Murray Lab (NC-ND) nem Blend HRSC (CC BY-SA).
- Arquivos grandes (`*.raw`, `*.tif`, `*.npy`) ficam fora do Git; o script regenera.
- Tamanho, água, início e **área jogável** em `ferramentas/terreno/mapa.json`; platôs, suavizações e canyons em `edicoes.json`. As coordenadas de edição usam um **sistema de referência fixo** (canto sudoeste do mapa 25×25 original), então não mudam quando o mapa cresce.

## Antes de concluir uma tarefa
- `dotnet build` sem erros nem warnings novos.
- `dotnet test` passando.
- Valores de balanceamento em `Data/`, não hardcoded.

## Git
- **Nunca commitar ou dar push sem aprovação explícita do Caio.**
- Remote: `CaioAlexandreps02/Marte` no GitHub. **Neste PC** a conta do Caio usa a chave **`~/.ssh/id_ed25519_caio`** (as outras chaves são de outras contas: `id_ed25519` = MeuJudi, `vpt_github_new` = vptvolei-team, padrão do `~/.ssh/config`). O `origin` local está sem URL, então enviar pela URL:
  `GIT_SSH_COMMAND="ssh -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519_caio -F /dev/null" git push git@github.com:CaioAlexandreps02/Marte.git main`
- Não há `user.name`/`user.email` global: commitar com `git -c user.name="Caio" -c user.email="caioporto100@gmail.com" commit ...`.
- Mapa gerado (tiles, ~1,4 GB) não vai para o Git: zip em Release do GitHub (`ferramentas/terreno/cache/marte-terreno-*.zip`).
