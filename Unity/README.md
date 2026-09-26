# Unity — apresentação do jogo

Unity **6000.3.25f1 (6.3 LTS)**, URP. Só apresentação, input, câmera, UI e áudio; a lógica do jogo vive em
`../Simulation/` (D5). Nunca editar `.unity`/`.prefab`/`.meta` à mão — tudo é montado por editor scripts.

## Montar o projeto do zero (clone novo)

Os tiles de terreno, o horizonte, o fundo e os materiais gerados **não estão no Git** (~1,4 GB). Para recriar:

1. Gerar o terreno: `ferramentas/terreno/` → `python exportar_heightmap.py` e depois `python exportar_fundo.py`
   (1ª vez ~25 min, baixa os dados da USGS).
2. Abrir o projeto no Unity 6.3 e rodar os menus:
   - **Marte → Terrain → Import Jezero** (~4,5 min, 700 tiles) — cria `Assets/Resources/Terrain/` e `Assets/Terrain/`;
   - **Marte → Scene → Setup World, Water and Player** — monta a cena (`Assets/Scenes/SampleScene.unity`).
3. Salvar a cena.

Outros menus: **Import Landmarks Only** (só os marcos, depois de mudar `marcos.json`), **Import Backdrop Only** (só o fundo), **Render Stamp Previews** (compara stamps de relevo).

## Controles (teste)

| Tecla | Ação |
|---|---|
| W A S D + mouse | andar / olhar |
| Shift | correr (60 m/s — valor de teste para explorar) |
| Espaço | pular |
| **F** | liga/desliga **voo**: WASD na direção do olhar, Espaço sobe, Ctrl desce, Shift acelera (80 → 400 m/s) |
| **M** | nomes dos marcos: próximos (3 km) → todos → esconder |
| Esc / clique | solta / prende o mouse |

## Arquitetura do mundo (`Assets/Scripts/World/`)

| Script | O que faz |
|---|---|
| `JezeroWorldInfo` | ScriptableObject gerado pelo import: tamanho do mapa (tiles X/Z), altura, água, início, área jogável, horizonte e fundo |
| `TerrainStreamer` | No objeto **World** (raiz, na origem). Carrega tiles completos (`Resources/Terrain/Jezero/Jezero_x_z`) num raio de 2,5 km, com antecipação na direção do movimento, e descarrega a 3,2 km. Monta o **horizonte** (1 malha de 31 m por tile, some quando o tile carrega) e o **fundo** (100×100 km, só visual). Roda também fora do Play, em volta da câmera da aba Scene (objetos `DontSave`, nunca salvos na cena) |
| `HorizonBuilder` | Gera as malhas do horizonte e do fundo, com "saia" nas bordas e normais contínuas entre pedaços |
| `FloatingOrigin` | No jogador: a cada 1 km recentraliza todos os objetos raiz. Posição verdadeira = `FloatingOrigin.ToTrueWorld(pos)` |
| `MapBoundary` | No jogador: mantém dentro do retângulo do mapa (−300 m) e do **polígono jogável**; desliza ao longo do limite; aviso "SINAL DA BASE FRACO" a menos de 900 m (OnGUI provisório), **exceto a menos de 2 km da antena do Mirante** (corredor da trilha, D15) |
| `LandmarkMarkers` + `Landmark` | Objeto **Landmarks**: um poste colorido por tipo em cada marco de `ferramentas/terreno/marcos.json` (41) e o nome com a distância na tela (tecla M). Na aba Scene os nomes aparecem sempre. Provisório até cavernas, destroços e estações ganharem modelo |

`Assets/Scripts/Player/FirstPersonController.cs` — controle em 1ª pessoa (Input System). Olhos a **1,75 m** do chão; o jogador nasce no pad de pouso olhando para a Mesa do Terraço (D16, `JezeroWorldInfo.startYaw`).
`Assets/Shaders/MarsSky.shader` — céu em gradiente (paleta D12); a parte abaixo do horizonte tem a cor da névoa.

### Coordenadas
- **Unity:** origem no centro do mapa (antes do floating origin), x → leste, z → norte, 1 unidade = 1 m.
  Altura: `y = (h_real − min_codificado) × 2` (exagero vertical D8).
- **Mapa (pipeline):** metros a partir do canto sudoeste do mapa atual.
- **Referência (edições, início, área jogável):** metros a partir do canto sudoeste do mapa 25×25 original.
  `mapa = referência + desloc` (`metadata.json → referencia`; hoje desloc_x = −3000 m).

## Editor scripts (`Assets/Editor/`)
`JezeroMetadata` (lê `ferramentas/terreno/saida/metadata.json`), `JezeroTerrainImporter`, `JezeroSceneSetup`,
`StampPreview`.

## MCP
`CoplayDev/unity-mcp` (pacote em `Packages/manifest.json`), modo **stdio**, telemetria desligada. Configuração do
cliente em `../.mcp.json`. Na janela **Window → MCP for Unity**: Transport = Stdio, sessão ativa.
