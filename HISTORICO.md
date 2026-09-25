# Histórico de sessões

> O que foi feito em cada sessão de trabalho, em ordem. Decisões ficam em [DECISOES.md](DECISOES.md); pesquisa em
> [CONHECIMENTO.md](CONHECIMENTO.md); próximos passos em [ROADMAP.md](ROADMAP.md).

## 24/09/2026 — Unity, MCP e terreno jogável

### Ambiente
- Removido o Unreal Engine 5.8 do PC (~37 GB: `D:\Epic Games\UE_5.8`, caches em AppData/ProgramData e a pasta
  "Unreal Projects"). O Epic Games Launcher foi mantido.
- Instalado o **Unity Hub** e o **Unity 6.3 LTS (6000.3.25f1)** com Visual Studio Community 2026, sem módulos de
  outras plataformas (jogo é PC). Editor em `D:\Epic Games\Editor\6000.3.25f1` (local padrão escolhido pelo Hub).
- Criado o projeto **`Unity/`** (template Universal 3D / URP) dentro do repositório, com o **Unity CLI** ativado.
- Instalado o **`uv`** (winget) e configurado o **MCP `CoplayDev/unity-mcp`** v10.2.0 em modo **stdio**
  (`.mcp.json`), com **telemetria desligada** nos dois lados (Unity: `EditorPrefs`; servidor: `DISABLE_TELEMETRY=1`).
  O modo HTTP do assistente do pacote falhou (chama `uv --from` em vez de `uvx`) — stdio resolve.
- O plugin oficial `unity-agent-plugin` **não** foi instalado (não era necessário ainda).

### Terreno (pipeline em `ferramentas/terreno/`)
1. Gerado o 8×8 km original e importado no Unity; jogador em 1ª pessoa no ponto de início.
2. Mapa ampliado para **16×16**, depois **25×25** (crescendo para nordeste) e por fim **28×25 km** (3 km a menos
   a oeste, 6 km a mais a leste). O script passou a processar em **faixas de 1 km** (grade em disco), a juntar
   **HiRISE 1 m + mosaico CTX 20 m + DTMs CTX do catálogo USGS** (com correção de desvio vertical de cada um) e a
   ler tudo de `mapa.json` / `edicoes.json`.
3. **Nível da água** baixado de −2530 para **−2560 m** (lago de ~24% para ~15% do mapa).
4. **Edições à mão** (`edicoes.json`, em coordenadas de referência fixas):
   - platô da base inicial (raio 300 m, borda irregular);
   - suavização "planície norte do lago" (ondulação a 30%);
   - **canyon norte**: vale real das Hephaestus Fossae (HiRISE 1 m, CC0), 10 km, ~300 m de profundidade no jogo.
5. **Área jogável** em polígono (`mapa.json`): limite no meio da subida da borda da cratera (oeste) e na beirada sul
   do canyon (norte); o resto é só visual.
6. **Terreno de fundo** (`exportar_fundo.py`): 100×100 km só visual (CTX perto, **MOLA 463 m** longe), com a
   cratera de Jezero inteira visível.

### Unity (`Unity/Assets/`)
- `FirstPersonController`: andar, correr (Shift, 60 m/s para teste) e **modo voo (F)** para explorar o mapa.
- **Streaming de terreno** (`TerrainStreamer`): tiles completos num raio de 2,5 km com carregamento antecipado;
  **horizonte** de baixa resolução do mapa inteiro; **fundo** além do mapa; tudo aparece também na aba Scene.
- **Floating origin** (mundo recentraliza a cada 1 km), **limite do mapa** com aviso "sinal da base fraco",
  **céu caramelo** (shader próprio) e **névoa de poeira** na paleta do D12.
- Editor scripts: `Marte → Terrain → Import Jezero`, `Import Backdrop Only`, `Render Stamp Previews` e
  `Marte → Scene → Setup World, Water and Player`.

### Design
- **D14 — Nivelamento de terreno** (fundações auto-niveladoras no MVP, terraplanagem que gera regolito, drone depois),
  com documento em `design/mecanica-nivelamento-terreno.md`.
- D8 atualizado várias vezes: tamanho 28×25, água, canyon, mundo sem fim visível, direção "mapa grande = espaço de
  construção; recursos raros longe".

### Pendências conhecidas (terreno)
- Linhas retas fracas onde termina cada DTM CTX do catálogo (norte/nordeste) — suavizar a emenda.
- Paredão sul do canyon com triângulos de interpolação do DTM — disfarçar com textura/ruído.
- **Canyon ainda não impressiona visto do chão:** sem textura de rocha nas partes íngremes e sem sombras longas, o paredão de ~300 m parece encosta lisa → resolver na etapa de texturas (pintura por inclinação) e sombras. O limite jogável acompanha a beirada a ~25 m (33 pontos).
- Água ainda reflete o céu azul antigo; aviso do limite é provisório (OnGUI).
- Streaming não foi testado em alta velocidade com o editor em foco (só a largada).
- 14% (16×16) / ~67% (28×25) do mapa vem de dado de 20 m: mais liso, sem pedras pequenas.
- Git: criada a chave `~/.ssh/id_ed25519_caio` (conta CaioAlexandreps02) e enviados os commits; o `origin` local
  continua sem URL (ver CLAUDE.md → Git). Release com o zip do mapa: pendente.

## 25/09/2026 — Marcos, cavernas e base no centro (design + pipeline)

### Design
- **Recursos (continuação):** a água segue em duas frentes (hidrogênio da Terra + CO₂ → Sabatier; **gelo escondido em
  cavernas** [JOGO]) e os metais ganharam direção (magnésio da olivina/serpentina, aço = ferro + carbono dos
  carbonatos). Isso virou critério para os marcos: cavernas de gelo, carbonatos, meteoritos ferrosos, olivina em Séítah.
- **D15 — Marcos, área jogável e canyon** ([proposta](design/proposta-marcos-e-cavernas.md), imagens 12–16): lugares reais
  de Jezero localizados pelos waypoints do Perseverance/Ingenuity e pelo DTM CTX (Kodiak, Belva, Three Forks, Séítah,
  Cheyava Falls…); área jogável **Variante A "Delta + Leste"** (~338 km²); canyon das Hephaestus Fossae na **diagonal
  da planície leste** + cadeia de **poços de colapso**; **35 marcos** (5 mesas reais achadas no DTM, 10 cavernas de tipos
  diferentes); **Mirante da Sentinela** no cume da borda oeste com trilha de 3,3 km pela crista norte (rota de menor custo).
- **D16 — Base no centro, B2 "Terraço do Lago"** (imagens 17–19): zona de 4,1 km² aplainada com um tipo novo de edição,
  **Mesa do Terraço** reforçada (+45 m), início no pad de pouso, **Abrigo do Terraço** como caverna-tutorial nova; a base
  antiga vira o pouso de uma missão anterior.

### Pipeline do terreno (`ferramentas/terreno/`, ainda não regenerado)
- `mapa.json`: polígono Variante A + corredor de 300 m da trilha e círculo no cume; `inicio_km` exato no pad
  (14,25; 13,50) — o exportador não procura mais o início no fundo do lago. Tiles continuam **28×25**.
- `edicoes.json`: canyon movido; tipos novos **`nivelamentos`**, **`mesas`** (stamp da Kodiak do CTX), **`pocos`**,
  **`trilhas`**; platôs do pad e do cume com `altura_m: null` (mediana do terreno já editado); ordem de aplicação única
  em `aplicar_edicoes`. Autoverificação (`verificar_edicoes`) vai para `metadata.json`.
- Canyon processado em faixas (a diagonal cobre ~7×7 km) e com cache pelo nome da fonte.
- `marcos.json`: 41 marcos (37 numerados + base, início, início da trilha, pouso da missão anterior) para o Unity.
- `preview_edicoes.py`: aplica tudo com as mesmas funções sobre o CTX 20 m (roda sem os tiles) → imagens 20–22.
  Resultado no CTX: base com inclinação mediana **0,9° no jogo**, chão ≥ **62,6 m** acima da água; Mesa do Terraço
  −2449 → −2404 m (+45 m); trilha com máximo de **24°** no jogo (antes 33°), corte máximo 3,6 m.

### Pendências
- **No PC Xeon:** renomear `cache/stamp_canyon_norte.*` → `stamp_DTEEC_069071_2020_063847_2020_A01.*` (evita baixar 94 MB), regenerar (`exportar_heightmap.py`, `exportar_fundo.py`), conferir `verificacao_edicoes` e reimportar
  no Unity (Import Jezero + Setup World). Conferir a trilha no HiRISE (crista estreita) e o aviso de sinal no corredor.
- O canto oeste (bolsão de Cheyava Falls em x = 3,2 km e o cume em x = 3,8 km) fica a < 1 km da borda dos tiles:
  se a vista do Mirante para oeste parecer cortada, crescer o mapa 1–2 km para oeste.
