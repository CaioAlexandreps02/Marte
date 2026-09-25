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
- Remoto `origin` do Git estava sem endereço nesta máquina, e nenhuma chave SSH local entra como
  CaioAlexandreps02 (ver CLAUDE.md → Git).
