# Jogo de Marte — Base de Conhecimento

> Documento de **conhecimento**, não de plano. Reúne o que já foi pesquisado e aprendido.
> As decisões serão tomadas depois, uma de cada vez, e registradas em outro documento (visão).
> Criado em 24/09/2026.

---

## 1. Conceito (como está hoje)

**Mistura de três jogos:**

| Jogo | O que pegar dele |
|---|---|
| **Surviving Mars** | **Referência de funcionalidades** (terraformação e outras mecânicas de Marte) e do foco em construir a colônia. Sobrevivência em **segundo plano**. Não é referência de câmera: o jogador fica no chão (ver [DECISOES.md](DECISOES.md) D1). |
| **Satisfactory** | A **automação**: cadeias de produção, máquinas, logística, ideias de progressão. |
| **Subnautica** | A **base de jogabilidade**: câmera no chão, exploração, mundo imersivo, descoberta, progressão ligada a explorar. |

**Frase-guia:** *simples e intuitivo por fora, complexo por trás, com muita coisa pra fazer.*

**Ainda em aberto:** 1ª ou 3ª pessoa, engine, single ou co-op, profundidade da automação, estrutura do mundo (ver seção 11).

> ✅ Resolvido (D1): o jogador administra tudo do chão. Surviving Mars entra só como fonte de funcionalidades.

---

## 2. Como planejar um jogo (filosofia de trabalho)

- Jogo se descobre **jogando**. Um GDD completo feito antes do protótipo quase sempre é reescrito. O jeito do Caio de "ir ajustando no caminho" está certo, **desde que** as decisões caras estejam fixas.
- **Portas de mão única** (caro mudar depois → decidir cedo):
  1. Single-player ou multiplayer/co-op (colocar multiplayer depois ≈ reescrever o jogo)
  2. 1ª ou 3ª pessoa (câmera, animação, modelo, UI, construção)
  3. Engine
  4. Estrutura do mundo (mapa contínuo x zonas; feito à mão x procedural)
  5. Pilares (3–4 frases do que o jogo é e **não** é)
  6. Core loop e escopo do MVP
- **Portas de mão dupla** (barato mudar → deixar solto): árvore de tecnologia, receitas, números, história detalhada, biomas, criaturas, máquinas, UI, áudio, arte final.
- Com IA isso importa mais: o Claude Code precisa de uma "estrela-guia" estável, senão cada sessão puxa o jogo pra um lado.

---

## 3. Aprendizados do vídeo — Stefan 3D AI

**Vídeo:** "I'm Finally Making My Dream Game - With AI From Scratch" — canal Stefan 3D AI (Stefan Vaskevich), 12/09/2026, 36min.
**Link:** https://www.youtube.com/watch?v=mNjBBO1gWFI
**Transcrição completa:** [referencias/transcricao-video-stefan-3d-ai.txt](referencias/transcricao-video-stefan-3d-ai.txt)
**Contexto:** 1 semana de um RTS de conquista de castelos, feito com Claude (CLI) + Unity 6 URP + MCPs (Unity, Blender, geração de assets). ⚠️ Vídeo patrocinado (Customuse) e ele vende curso — descontar o entusiasmo com essas ferramentas.

### 3.1 Processo
- **Dia 1 inteiro só no conceito** com o agente, até resumir o jogo em poucas frases.
- **Mecânica antes da arte**: até o dia 3, só primitivas (cubos). Validou o gameplay primeiro.
- Protótipo em **passos mínimos** (um elemento por vez).
- **Stats/valores num documento separado do código**, sempre sincronizados. (Para um jogo de receitas estilo Satisfactory, isso é essencial.)
- **Playtest muito frequente** (~200 vezes) com feedback concreto pro agente ("forte demais", "fraco demais").
- Meta é uma **baseline divertida**, não balanceamento perfeito.
- **Atacar primeiro o que dá mais medo** (pra ele: terreno).
- Ferramentas de **debug cedo** (ex: spawn de coisas).
- Polish (cursor, minimapa) só no fim.

### 3.2 Trabalho com o agente de IA
- **"Não delegue o que você não entende."** Usar o Claude como professor, passo a passo.
- Workspace do agente com **memória persistente, versionado no Git**. Cada tarefa que dá certo vira instrução reutilizável → as skills nascem da prática.
- **Ritual de fim de dia**: agente consolida conhecimento, revisa estrutura do projeto, lista pendências e salva.
- **Git desde o dia 1** (projeto + documentos de design).
- Pedir resultados como **página HTML** pra revisar rápido.
- Deixar o agente **tirar screenshot da cena** pra decidir o que combina.
- Misturar modelos por tarefa (ele citou GPT-6 pra rigging).

### 3.3 Engine
- **Unity > Unreal para trabalhar com agentes de IA**, segundo ele (usou Unreal 2 anos). Motivo: MCP do Unity funciona melhor e mais rápido.
- URP basta pra visual estilizado; HDRP/Unreal só se o alvo for realismo pesado.
- ⚠️ Conflita com a escolha de Unreal 5 do documento anterior → pesquisa completa na seção 9.
- ⚠️ O MCP que ele usa (AnkleBreaker) tem licença que exige crédito/logo no produto final.

### 3.4 Assets e arte
- Assets complexos gerados **em partes definidas por você**, separando o que muda com o estado do jogo (no nosso caso: luz de status, esteira, porta das máquinas).
- Agente manda peças pro Blender via MCP; montagem/UV/acabamento manual nos assets "hero" (~2h cada) — é a parte autoral.
- Texturização: Tripo retexture ou Meshy com imagem de referência; Nano Banana (image edit) pra alinhar paleta.
- Bom asset sai na **2ª a 5ª tentativa** — sempre dizer o que gostou e o que não.
- **Otimizar o que repete muito** (performance é prioridade) — numa fábrica com centenas de máquinas, isso é crítico.
- Não reinventar a roda: comprar o plugin padrão do mercado (ex: MicroSplat ~US$20) não é "trapaça".

### 3.5 Terreno e ambiente
- Terreno do Unity URP: máx. 8 layers antes de artefatos → MicroSplat resolve (até 32).
- **Decals** (PNGs gerados) = muito visual por pouco esforço (rachaduras, trilhas, bases em volta de construções).
- **Sombra de nuvens** passando pelo terreno quebra a iluminação plana — em Marte: sombra de poeira/tempestade.
- Shaders de vento/água feitos 100% pelo Claude.
- Post-processing mínimo (color correction) já ajuda muito.
- Mudar terreno quebra pathfinding → retestar navegação sempre.

### 3.6 Design
- **Leitura visual comunica a mecânica**: só de olhar, o jogador entende "o que tem aqui".
- Fog of war / visão limitada tornam exploração divertida.
- Level design: rota principal difícil + atalhos escondidos que recompensam explorar.

### 3.7 Marketing (dele)
- Devlog diário no X + vídeo semanal no YouTube + pedir ideias da audiência.

---

## 4. Concorrente direto — 687 Days on Mars

**Steam:** https://store.steampowered.com/app/3850980/687_Days_on_Mars/

| Item | Dado |
|---|---|
| Dev / publisher | Frozen Cave Studio + Games Incubator / PlayWay (Polônia) |
| Perspectiva | 1ª pessoa, single-player, sem combate |
| Status | Não lançado ("2026", sem data). Não é Early Access. |
| Demo | Grátis desde 02/10/2025 — **82% positivas (90 reviews)**; "+20 mil jogaram" (segundo o dev) |
| Seguidores Steam | ~3.400 (wishlists estimadas 25–40k, não verificado) |
| Engine | Não confirmada (provável Unity) |
| Idiomas | 13, inclui PT-BR |

**Loop:** coletar regolito/gelo → O₂, água, energia → expandir base → cultivar comida → pesquisar com amostras de expedições → preparar pro clima → expedições maiores → história (mistério da tripulação).

**Mecânicas:** stats O₂/água/energia/comida + dieta (vitaminas afetam desempenho); radiação em tempestade solar; base por segmentos; painéis solares acumulam poeira; manutenção; 4 estações com ameaças diferentes + previsão do tempo; rover → "Mobile Shelter" (base móvel); mapa procedural; pesquisa que leva vários sóis.

**Automação:** só **drones** levando recursos entre prédios. **Sem esteiras, sem cadeia de fábrica.**

**Elogiado:** atmosfera "*The Martian*", loop sólido, acessível, sobrevivência sem combate, devs responsivos.

**Criticado:** demo curta; **linear/guiado demais, pouca descoberta**; inventário apertado; falta QoL (airlock manual, sem "unstuck", sem timer de recurso); **UI confusa** (status de prédio, energia); bugs (cair do mapa, crash); falta co-op; estigma da PlayWay ("asset-flip").

**Marketing (playbook replicável):** página Steam cedo → playtest aberto → demo 2 semanas antes do Steam Next Fest → devlog a cada 4–6 semanas sempre com CTA de wishlist → Discord + formulário de feedback → dev stream na Twitch → festivais temáticos do Steam → YouTubers médios fazendo "First Look" → press release.

---

## 5. Mercado — jogos parecidos (Steam, set/2026)

| Jogo | O que é | Reviews |
|---|---|---|
| **The Planet Crafter** | Sobrevivência 1ª pessoa + terraformação + automação leve | 74k — 96% |
| Surviving Mars | Colônia top-down | 29k — 79% (*Relaunched*: 2,5k — 56%) |
| Stranded: Alien Dawn | Colony sim top-down | 11k — 84% |
| Mars First Logistics | Sandbox de física/logística com veículos | 3,8k — 95% |
| Occupy Mars | Sobrevivência realista 1ª pessoa, base modular, co-op; 1.0 criticado por bugs | 3,2k — 70% |
| Mars Horizon | Gestão de programa espacial | 3,1k — 84% |
| Deliver Us Mars | Aventura narrativa 3ª pessoa | 3k — 75% |
| Memories of Mars | Sobrevivência multiplayer/PvP | 1,7k — 60% |
| **Referências do mashup** | | |
| Subnautica | | 380k — 97% (*Subnautica 2* EA: 128k — 91%) |
| Satisfactory | | 280k — 97% |
| Astroneer | | 139k — 92% |
| Techtonica | "Satisfactory subterrâneo" — mostra que misturar não garante sucesso | 3,3k — 65% |

**Leituras:**
- Existe demanda (Planet Crafter).
- Jogos de Marte "realistas" ficaram Mixed por bugs → público carente de algo **polido**.
- Co-op fez Satisfactory, Planet Crafter e Astroneer crescerem.

---

## 6. Oportunidades de diferenciação

1. **Colônia + fábrica de verdade, jogada do chão, em Marte — ninguém tem.** 687 só tem drones; Occupy Mars e Planet Crafter têm automação rasa; Surviving Mars é top-down sem automação física. O mashup dos três é o espaço vazio.
2. **Mundo que vale explorar** (lição Subnautica): cavernas, tubos de lava, gelo profundo, bases abandonadas, áreas que só se alcançam com equipamento melhor. O 687 é criticado justamente por pouca descoberta.
3. **Mundo feito à mão com história ambiental** (logs, destroços) > procedural linear.
4. **QoL e UI claras desde o dia 1** — é o que mais derruba notas dos concorrentes, e é barato de acertar. Casa com "simples e intuitivo por fora".
5. **Polimento técnico** — demo curta e estável vale mais que muita feature.
6. **Co-op** — pedido pelos jogadores do 687; decidir cedo (porta de mão única).

**Ideias boas pra aprender com os outros:**
- Estações do ano + previsão do tempo → planejamento antecipado (687).
- Base móvel / Mobile Shelter ≈ Seamoth/Cyclops do Subnautica (687).
- Poeira nos painéis solares e manutenção → pressão leve de sobrevivência (687).
- Progressão visível no mundo — o planeta muda (Planet Crafter).
- Identidade visual forte e sensação de descoberta > realismo (Subnautica/Satisfactory).

---

## 7. Técnico (do documento anterior, ainda válido)

Detalhes completos em [referencias/projeto-jogo-marte-mcp.md](referencias/projeto-jogo-marte-mcp.md). Resumo:

- **Terreno:** ~~dado real MOLA-HRSC~~ → **ver seção 10** (versão Unity, com correções de fontes e licenças).
- **Texturas grátis:** Poly Haven, ambientCG (CC0). Megascans não é mais grátis.
- **Assets de IA (Meshy/Rodin/Tripo) servem pra decoração**; peças que encaixam/animam/têm lógica (base modular, máquinas, veículos) precisam de geometria controlada (Blender via MCP ou kit pronto) + lógica no engine.
- **Kits modulares grátis:** Kenney Space Station Kit (CC0), Sketchfab sci-fi modular, Fab (grátis por tempo limitado).
- **Licenças comerciais** a checar antes de escalar: Meshy (Pro $20), ElevenLabs (Starter $6), Rodin.
- **Skills/agentes:** Claude Code Game Studios, jeffallan/game-developer, DavinciDreams/3d-design, GameDevelopmentAudit (polimento). Obs: o vídeo sugere que as melhores skills nascem da prática — instalar com moderação.
- **Método de trabalho:** Spec-Driven Development (spec curta + critérios de aceite testáveis antes do código); CLAUDE.md curto (<250 linhas) com detalhes em `.claude/rules/`.
- ⚠️ A parte de engine (Unreal 5) desse documento está em revisão (ver 3.3).

---

## 8. Marketing — ativo do Caio

Marketing é a área do Caio, então é vantagem competitiva real. Combinando o vídeo e o 687:
- Página no Steam **cedo** (wishlists acumulam desde o dia 1).
- Devlog frequente (X/TikTok/Instagram/YouTube) — o próprio desenvolvimento com IA é conteúdo.
- Playtest aberto → demo antes de um Steam Next Fest → festivais temáticos (ex: PvE Survival Crafting Fest).
- Discord + formulário de feedback; responder a comunidade (elogiado no 687).
- YouTubers médios de survival/automação fazendo "First Look".

---

## 9. Engine — Unity 6 x Unreal 5 (pesquisa de 24/09/2026)

### 9.1 PC de desenvolvimento
- **Máquina alvo:** Intel Xeon (modelo a confirmar) + GTX 1660 (6 GB) + 32 GB RAM em **um pente só**.
- **Xeon usado:** muitos núcleos (bom pra compilar shaders), mas núcleo individual lento (ex: E5-2680 v4 ≈ metade do single-core de um Ryzen 5600G). O dia a dia do editor depende do núcleo individual.
- **Risco:** Xeon E5 v1/v2 (X79) não tem AVX2 → relatos de crash no UE5. v3/v4 (X99) OK. Checar no CPU-Z (aba CPU → Instructions).
- **RAM em 1 pente = single-channel** → gargalo grande em placa Xeon (X99 é quad-channel). **Upgrade mais barato e mais útil:** 4×8 GB (placa com 4+ slots) ou 2×16 GB (placa com 2 slots). Mais RAM não precisa.
- **Coletar do PC:** modelo do CPU, placa-mãe, nº de slots, canais ativos (CPU-Z aba Memory → "Channel #").
- **Veredito:** Unity roda com folga. Unreal roda com sofrimento: Lumen só software e lento no editor, Lumen hardware não roda (exige RTX), VRAM abaixo dos 8 GB recomendados, C++/Live Coding lentos no Xeon.

### 9.2 Jogadores (Steam Survey ago/2026)
- ~15–20% dos jogadores têm GTX 1660 ou mais fraca. UE5 com Lumen/Nanite obrigatórios corta essa base.
- Subnautica 2 (UE5) tem GTX 1660 como **mínimo**.

### 9.3 MCP e IA — Unreal
- **MCP oficial da Epic existe e vem no UE 5.8** (plugins ModelContextProtocol + AllToolsets; plugin de skills pra Claude Code `EpicGames/unreal-engine-skills-for-claude-code-plugin`). Centenas de tools. **Status: Experimental** ("incompleto, APIs podem mudar"); já quebrou compatibilidade em mai/2026.
- **Blueprints = ponto fraco com IA.** `.uasset` é binário; IA não lê fora do editor. MCPs criam/editam, mas grafos ficam bagunçados e tipos complexos quebram. Nenhum MCP automatiza Blueprint com segurança total (set/2026).
- **Caminho viável: C++ como fonte da verdade**, Blueprints só como dados. Claude vai bem em C++ de UE. Custos: compilação lenta; mudar header exige fechar o editor e rebuild.
- **Comunidade:** melhor hoje é `db-lyon/ue-mcp` (ativo). `chongdashu/unreal-mcp` (o mais famoso) está abandonado.
- **Alternativa em texto:** UnrealSharp (C# no UE, MIT, ativo, 3 jogos na Steam).
- **Risco de versão:** UE 5.8 é a última grande versão do UE5; UE6 (linguagem Verse) em desenvolvimento → possível migração no meio do projeto.
- Nenhum jogo lançado feito majoritariamente por agente em UE documentado.

### 9.4 MCP e IA — Unity
- **Plugin oficial da Unity pra Claude Code** (09/09/2026): `Unity-Technologies/unity-agent-plugin`, 29 skills + `unity` CLI (beta): testes headless, build, controle do editor, screenshots.
- **Unity AI Assistant / MCP nativo:** no plano Personal exige assinatura de **US$10/mês** e foi mal recebido. Não é necessário (usar plugin oficial + MCP comunitário).
- **MCPs comunitários:**
  - **CoplayDev/unity-mcp** — 14k★, MIT, ~47 tools, o mais maduro (desligar telemetria).
  - **IvanMurzak/Unity-MCP** — 4k★, Apache, 70+ tools, screenshots; configurar modo local (padrão aponta pra nuvem).
  - **CoderGamester/mcp-unity** — enxuto e estável.
  - **AnkleBreaker** (o do vídeo do Stefan) — 268+ tools, **mas a licença exige mostrar "Made with AnkleBreaker MCP" + logo no produto** → evitar num jogo comercial.
- **C# é texto puro** → IA vai muito bem. Cenas/prefabs são YAML, mas **não editar à mão** (GUIDs dos `.meta` quebram) → criar via editor scripts.
- **Ponto fraco:** cada mudança de C# recompila e recarrega o domínio, derrubando a conexão MCP por alguns segundos. Unity 7 (CoreCLR, 2027) deve eliminar isso.
- **Testes headless funcionam bem** → lógica da fábrica testável sem abrir o editor.
- **Preço:** Personal grátis até US$200k/ano; Runtime Fee cancelada (2024); splash opcional. LTS atual: 6.3.
- Relato real: artista sem experiência fez jogo solo com Claude Code em Unity em ~10 meses — funcionou, mas precisou de documento de visão e supervisão constante porque o Claude "desvia da intenção".

### 9.5 Pontos que valem pras duas engines
- **Esteiras com milhares de itens são código próprio em qualquer engine**: simulação em arrays com tick fixo + renderização instanciada. Nunca um objeto por item. (Satisfactory: ISM + shader; DSP: compute shader; Unity: Jobs/Burst + GPU instancing — referência de 1 milhão de itens a 60 fps.)
- **Co-op de fábrica:** replicar construções e comandos, não cada item. A arquitetura da D5 importa mais que a engine.
- UE tem replicação pronta (vantagem no jogador/movimento); na fábrica é trabalho custom nas duas. Em Unity: NGO ou Mirror (mais exemplos → IA erra menos) ou FishNet.

### 9.6 Jogos do gênero por engine
- **Unity:** Subnautica, Planet Crafter, Dyson Sphere Program, Captain of Industry, Shapez 2, Timberborn, Occupy Mars, Techtonica.
- **Unreal:** Satisfactory, Subnautica 2, Astroneer (UE4).

### 9.7 Resumo comparativo

| Critério | Unity 6 | Unreal 5 |
|---|---|---|
| Rodar no PC do Caio | ✅ folga | ⚠️ sofrido |
| IA lê/edita toda a lógica | ✅ C# texto | ⚠️ só se for C++ puro |
| Maturidade do MCP | ✅ comunidade madura + plugin oficial | ⚠️ oficial experimental |
| Velocidade de iteração | ✅ (reload de alguns segundos) | ⚠️ compilação C++ lenta no Xeon |
| Gráfico máximo | Bom | ✅ melhor |
| Co-op futuro | Biblioteca externa | ✅ nativo |
| Mundo aberto / PCG | Terrain + ferramentas | ✅ World Partition + PCG |
| Jogos do gênero | ✅ maioria | Satisfactory, Subnautica 2 |
| Risco de migração | Unity 7 em 2027 (melhora, sem reescrita) | UE6/Verse |
| Alcance de jogadores | ✅ roda em PC fraco | ⚠️ Lumen/Nanite cortam PCs fracos |

---

## 10. Terreno real de Marte no Unity (pesquisa de 24/09/2026)

> Substitui a seção de terreno do documento antigo (que era pra Unreal). Algumas fontes antigas estavam erradas; ver 10.6.

### 10.1 Fontes de dados

| Dado | Resolução | Licença | Uso |
|---|---|---|---|
| **HiRISE DTM** (USGS) | 1 m/px, áreas pequenas | CC0 (pedem citação) | ✅ Núcleo jogável |
| **CTX DTM** (USGS) | ~20 m/px | CC0 (citar Laura et al. 2023) | ✅ Bordas e horizonte |
| Orthoimages HiRISE/CTX (USGS) | 0,25–1 m | CC0 | Máscara de albedo/cor |
| MOLA | ~463 m | CC0 | Pano de fundo distante |
| HRSC (ESA) e Blend HRSC+MOLA 200 m | 50–200 m | **CC BY-SA** (share-alike) | ⚠️ Evitar na área jogável |
| **Mosaico CTX Murray Lab** (aparece no Mars Trek/JMARS) | 5 m | **CC BY-NC-ND — proibido em jogo comercial** | ❌ Não usar |
| Mars Human Exploration Zone DEM Archive 2023 | 1.354 DEMs HiRISE + 1.354 CTX | Sem restrição (citar) | Garimpar biomas extras |

- **Mars Trek** é só visualizador: a licença é a de cada camada → sempre conferir a fonte antes de exportar.
- Na escala do jogo (1–10 km), só HiRISE e CTX servem. O Blend de 200 m é liso demais.

### 10.2 Regiões candidatas

1. **Jezero** — DTM HiRISE 1 m de ~21×21 km. Cratera que foi lago, com delta e rio seco (Neretva Vallis). **Perfeita pra terraformação encher de água.**
2. **Gale / Aeolis Mons** — DTM HiRISE 1 m de ~57×33 km. Morros estratificados + montanha de 5 km no horizonte. Também foi lago.
3. Hadriacus Palus (borda de Hellas) — candidato real a local de exploração humana; relevo menos icônico.
4. Valles Marineris — paredões dramáticos, mas DTMs em faixas estreitas → usar como "stamp".
5. Arsia Mons (entradas de cavernas/tubos de lava) e Korolev (gelo) — sem DTM confirmado → esculpir inspirado nelas.

**Estratégia "real + feito à mão":** base contínua de uma região real + formações de outras regiões coladas como stamps (morro de Gale, paredão de Valles, poço de Arsia). Deixa de ser 100% real, mas dá variedade num mapa compacto.

### 10.3 Pipeline no Unity

| # | Passo | Quem |
|---|---|---|
| 1 | Instalar GDAL + QGIS | Manual (1 vez) |
| 2 | Escolher o recorte olhando o terreno | **Manual** (decisão de design) |
| 3 | Baixar GeoTIFFs da USGS | Claude Code |
| 4 | Reprojetar, recortar, preencher buracos (GDAL) | Claude Code |
| 5 | Converter em RAW 16-bit em tiles (2049 ou 4097) | Claude Code |
| 6 | Erosão e micro-detalhe no World Creator ou Gaea | Manual |
| 7 | Editor script cria os tiles de Terrain e pinta por inclinação/altura | Claude Code |
| 8 | Espalhar pedras (MicroVerse / GPU Instancer) | Claude configura, ajuste manual |
| 9 | Céu, névoa, cor | Manual + iteração com Claude |

- Unity: heightmap máx. 4097 por tile; Terrain Toolbox importa vários RAW em grade.
- **Exagero vertical de 1,5–2,5×**: Marte na escala humana é plano; o relevo interessante está em escarpas e bordas.

### 10.4 Ferramentas (preços set/2026)

| Ferramenta | Pra quê | Preço |
|---|---|---|
| **World Creator Indie** (recomendada) | Importa GeoTIFF direto, erosão, **bridge pra Unity** | US$149 perpétuo ou US$59/ano; receita < US$100k; até 8K |
| Gaea Indie (alternativa) | Erosão/detalhe (import via conversão) | US$99 perpétuo; até 8K; teto de receita a confirmar |
| **MicroVerse** | Stamps, texturas e spawn não destrutivo dentro do Unity | US$70 |
| **MicroSplat** | Shader de terreno (anti-repetição, umidade, riachos → terraformação) | Core grátis, módulos pagos; fixar versão do Unity |
| GPU Instancer Pro | Milhares de pedras com performance | ~US$128 |
| Unity Terrain Tools | Import em tiles, erosão básica | Grátis |
| ❌ Vegetation Studio Pro | — | Descontinuado |

### 10.5 Assets prontos
- **Poly Haven** (CC0): coleção Namaqualand (rochas e solos de deserto escaneados) — ótima pra Marte. **ambientCG** também CC0.
- **Megascans/Fab**: não é mais grátis desde 2025.
- **Asset Store**: pacotes de Marte baratos (US$10–95), sem avaliações e sem dado real → usar só como fonte de rochas/texturas.
- **NASA 3D Resources**: rovers e landers reais, uso livre, **mas sem logo da NASA e sem sugerir endosso**.
- Fotos dos rovers (JPL): referência de cor livre; uso comercial com crédito "NASA/JPL-Caltech".

### 10.6 Correções ao documento antigo
- ❌ Sketchfab "Mars Terrain Model" (John Davies): planeta inteiro a 5 km/px com exagero de 20× e licença CC BY-SA → **inútil na escala do jogo**.
- ❌ Mosaico CTX do Mars Trek/JMARS (Murray Lab): **proibido uso comercial**.
- ⚠️ CGTrader "16K Mars Landscape": licença não verificada.
- ⚠️ Blend HRSC+MOLA 200 m: share-alike; só pano de fundo, se tanto.

### 10.7 Visual de Marte
- **Céu:** caramelo/"butterscotch" de dia; **pôr do sol azul** em volta do sol (poeira fina).
- URP 6.3 **não tem névoa volumétrica nativa** → Volumetric Fog & Mist 2 (Kronnect, pago) ou open source (URP-Volumetric-Light, PhysicallyBasedSky URP).
- Na GTX 1660: névoa de altura simples + céu em gradiente custom; volumetria em resolução reduzida; tempestade = névoa densa + partículas perto da câmera + menos sol.

### 10.8 Terraformação visual (referência Planet Crafter)
- Planet Crafter: céu azul, chuva e lagos em limiares fixos do índice; transição gradual; cada bacia tem nível final de água próprio.
- No Unity: plano de água por bacia com altura = progresso; rios com Splines seguindo o leito; máscara global de umidade/vegetação no shader do terreno; céu/névoa/cor do sol interpolados por um valor global `_Terraform`.
- Em Jezero isso é natural: o lago e o rio "voltam".

### 10.9 Tamanho do mapa e mundo contínuo

| Jogo | Tamanho |
|---|---|
| Subnautica | ~3,5–4 km de lado |
| Planet Crafter | ~4–4,5 km de lado |
| Satisfactory | ~8×7 km (47 km²) |
| Mars 2030 (HiRISE real) | 40 km² |

- **Recomendação da pesquisa: 6×6 a 8×8 km**, origem no centro, **sem floating origin** (em URP, floating origin faz o terreno piscar).
- Tiles: 4×4 de 2 km (2049) ou 2×2 de 4 km (4097). ~33 MB por heightmap 4097 → terreno cabe fácil em 6 GB; o gargalo serão texturas e props.
- Streaming: terreno sempre carregado; props, interiores e detalhes em cenas aditivas por célula.
- **Precedente mais próximo:** *Mars 2030* (NASA/Fusion) fez 40 km² de Mawrth Vallis a partir de DTM HiRISE.
- Occupy Mars usa terreno procedural com marcos reais; Surviving Mars e Planet Crafter são fictícios.

### 10.10 Desvantagens do mapa contínuo (e mitigação)
1. Precisão numérica longe da origem → mapa ≤ 8 km, origem no centro.
2. Streaming de pedaços → terreno sempre carregado; só props/interiores em streaming.
3. Fábricas longe do jogador precisam continuar funcionando → simulação separada da cena (D5).
4. Terraformação em áreas não carregadas → estado do mundo como dados (D5).
5. Mais trabalho de conteúdo (transições entre regiões sem tela de loading).
6. Performance menos previsível (visão longa, construção em qualquer lugar) → LOD, distância de visão, limites.
7. Bugs difíceis (save/load, veículos e drones cruzando células).

---

> **Atualização (24/09/2026):** a recomendação de 10.9/10.10 (mapa ≤ 8 km, sem floating origin, terreno sempre
> carregado) foi **superada** pelo D8: o mapa agora é 28×25 km com floating origin e streaming (ver 12). O risco
> citado ("floating origin faz o terreno piscar em URP") continua a ser observado em teste.

---

## 11. Decisões em aberto (responder uma de cada vez)

- [x] Engine: Unity ou Unreal? → Unity 6 URP (D6)
- [x] 1ª ou 3ª pessoa? → 1ª a pé, 3ª nos veículos (D7)
- [x] Single-player ou co-op? → single no lançamento, co-op depois, base pronta desde o início (D5)
- [x] Profundidade da automação → híbrida, esteiras protagonistas (D4) — **detalhar depois** cadeias, peças e suprimento da Terra
- [x] Como gerir uma colônia estando no chão? → do chão, sem visão de cima (D1)
- [x] Quem vive na colônia? → população abstrata (B); protótipo só com robôs (A) (D2)
- [x] Como funciona a terraformação (simples)? → híbrida: cúpulas locais + medidores globais (D3)
- [x] Papel da sobrevivência → traje leve, colonos estilo Surviving Mars, dificuldade define rigor (D10)
- [x] Estrutura do mundo → contínuo, Jezero real + feito à mão (D8); **tamanho atualizado para 28×25 km** com streaming e fundo só visual
- [x] Nivelamento de terreno → D14
- [x] Pilares → D9 (sem combate)
- [x] Core loop → D11 (história, pesquisa e suprimentos: sessões futuras)
- [x] Escopo do MVP → "do pouso ao primeiro domo" (D13)
- [x] Estilo visual → semi-realista estilizado (D12)
- [ ] Nome do jogo

---

## 12. Terreno na prática (sessão de 24/09/2026)

### 12.1 Dados usados de fato
| Fonte | Cobertura real | Observações |
|---|---|---|
| Mosaico **HiRISE 1 m** Mars 2020 (`JEZ_hirise_soc_006...`) | ~21×21 km, mas com **buracos** (14% da janela de 16 km; nordeste sem dado) | TIFF em faixas de 1 linha (não é COG) → leitura por HTTP Range. No 28×25 cobre **~33%** do mapa |
| Mosaico **CTX 20 m** Mars 2020 | ~32×30 km (lat 18,21–18,72) | Base de 20 m; acaba ao norte de 18,72° |
| **DTMs CTX do catálogo STAC** USGS (`mro_ctx_controlled_usgs_dtms`) | Dezenas em volta de Jezero | CC0. **Desvio vertical entre DTMs de −60 a +5 m** → cada um alinhado pela mediana contra o mosaico; descartados os com dispersão > 15 m; junção pela mediana. Deixa **linhas retas fracas** onde cada DTM acaba |
| **DTMs HiRISE do catálogo STAC** (`mro_hirise_socet_dtms`) | 1.262 DTMs no planeta, CC0 | Usados para stamps (canyon) |
| **MOLA 463 m** (`Mars_MGS_MOLA_DEM_mosaic_global_463m.tif`, USGS) | Global | **CC0**. Leitura por janela via `/vsicurl` (120 km em ~11 s). Desvio vs CTX: −2,6 m |

- HiRISE e CTX Mars 2020 estão relativos ao areoide MOLA ("DeltaGeoid") → compatíveis com MOLA sem conversão.
- Todos os produtos usados estão na mesma projeção (equiretangular, esfera R = 3.396.190 m), então não precisa reprojetar.

### 12.2 Paredões e canyons reais (escolha do stamp)
- Filtrados 16 candidatos pelo texto do catálogo; medido o desnível e a inclinação em 4 m **só em janelas 100% com
  dado** (preencher buracos com valor médio cria paredões falsos na borda do DTM).
- Mais íngremes: **Hephaestus Fossae** (fissura reta, até 79°, ~350 m de desnível), parede de cratera com basalto
  colunar (73°), escarpa da base do Olympus Mons (53°). Mesas de Protonilus e o "grand canyon" de Gale são bem menos íngremes do que parecem.
- **Visualização:** o 3D do matplotlib desenha na ordem errada e engana; renderizar como terreno no próprio Unity
  (`Marte → Terrain → Render Stamp Previews`) é o jeito confiável de comparar.
- Paredões de DTM têm **trechos interpolados** (triângulos lisos) onde o estéreo falhou.
- Esticar um vale no comprimento não muda a inclinação das paredes (usado para ir de 5,9 para 10 km).

### 12.3 Mundo grande sem parecer "bugado" (técnica adotada)
| Camada | Distância | Implementação |
|---|---|---|
| Tiles completos (1 m, colisão) | raio 2,5 km, descarrega a 3,2 km | `TerrainStreamer`: `Resources.LoadAsync`, 2 cargas simultâneas, 1 colisor por quadro, carregamento antecipado na direção do movimento (4 s) |
| Horizonte (mapa inteiro, 31 m) | sempre | 1 malha por tile, some quando o tile carrega; "saia" de 40 m nas bordas contra frestas |
| Fundo (100×100 km, 100 m) | sempre, só visual | CTX até 8 km da borda, MOLA além; células dentro do mapa ficam de fora |
| Névoa de poeira + céu | — | Névoa exponencial 0,00012 (some tudo por volta de 40 km); céu em gradiente cuja parte de baixo tem a cor da névoa → a borda do mundo nunca aparece, nem vista do alto |

- Nome da técnica em outras engines: "World Partition + HLOD" (Unreal). Na Unity foi montado à mão.
- **Floating origin:** recentraliza todos os objetos raiz a cada 1 km; os tiles ficam filhos de um objeto raiz, então a
  posição local deles = posição verdadeira no mapa.
- **Horizonte real de Marte:** ~3,5 km para quem está em pé num chão plano (planeta menor). O mundo do jogo é plano,
  então a névoa ajuda a parecer real. Curvar o fundo para baixo fica como ideia.
- **Limite do mapa:** barreira invisível + aviso no traje ("sinal da base fraco") + barreiras naturais (borda da cratera,
  canyon). O fundo continua do outro lado.
- Memória na largada: ~650 MB com 9 tiles; 1 tile = 1025² (2 MB de altura + colisor).

### 12.4 Tamanho de mapas de referência
Complementa 10.9: GTA V ~80 km²; Minecraft praticamente infinito (procedural). O nosso 28×25 km = 700 km² — o
tamanho percebido depende de conteúdo por km² e da velocidade (a pé 5 m/s: ~1h30 para cruzar 28 km).

### 12.5 Unity MCP (CoplayDev) — pegadinhas da instalação
- O Unity não enxerga o `uv` recém-instalado (PATH antigo) → apontar o **UVX Path** na aba Advanced.
- Modo **HTTP Local** falha (`uv: unexpected argument '--from'`) → usar **stdio** com o `.mcp.json` do projeto.
- "Configure" para Claude Code exige o `claude` CLI; com o app desktop basta o `.mcp.json`.
- **Telemetria vem ligada no lado do Unity** (`EditorPrefs`) → desligada com `TelemetryHelper.DisableTelemetry()`;
  no servidor, `DISABLE_TELEMETRY=1`.
- Com a janela do Unity **sem foco**, o Play quase não avança (o editor reduz a atualização).
- Mudanças de cena feitas **durante o Play** se perdem → sempre checar o estado antes de importar/montar.

### 12.6 Tempos e tamanhos (PC de desenvolvimento)
- Geração 28×25 (dados em cache): ~9 min; fundo: ~1 min; 1ª execução baixa ~1,5 GB (HiRISE) + ~50 DTMs CTX.
- Importação no Unity: ~4,5 min para 700 tiles (~1,4 GB de TerrainData, fora do Git).
