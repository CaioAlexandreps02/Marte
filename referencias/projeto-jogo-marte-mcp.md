# Projeto: Jogo de Sobrevivência em Marte (Automação via Claude Code + MCP/APIs)

> Documento de referência consolidando tudo que foi definido e pesquisado sobre o projeto. Última atualização: 17/09/2026 (revisão com base modular, skills de IA e roteiro de fases).

---

## 1. Conceito do jogo

- **Gênero**: Sobrevivência, em primeira pessoa, 3D.
- **Referências**: mistura de *Surviving Mars* (mecânica de sobrevivência/gestão de base) com *Subnautica* (estilo visual, exploração, sensação de mundo hostil e imersivo) — só que em Marte em vez de debaixo d'água.
- **Objetivo**: lançamento comercial (não é só hobby/portfólio).
- **Visual-alvo**: ambientação científica/sci-fi, instalações e construções em estilo Subnautica (metal, tubulações, painéis), terreno marciano realista (crateras, dunas, canyons, leitos de rios secos).

---

## 2. Engine recomendada

**Unreal Engine 5**, pelos seguintes motivos:
- Lumen (iluminação) e Nanite (geometria densa) entregam visual realista sem trabalho manual pesado de otimização.
- Suporte a mundos grandes via **World Partition** (carrega o terreno em pedaços conforme o jogador anda).
- Ecossistema de MCP mais maduro e com suporte **oficial da própria Epic** (ver seção 3).

Unity foi considerado como alternativa (mais leve, iteração mais rápida), mas fica mais dependente de asset store pra alcançar o nível gráfico desejado.

---

## 3. Automação: MCPs e APIs por categoria

A ideia central: usar **Claude Code e Codex** como "operadores" que controlam o engine, o Blender e os geradores de assets via MCP, minimizando trabalho manual — exceto pela geração manual de assets únicos na Meshy (decisão tomada: itens específicos são gerados manualmente no site da Meshy, não via MCP automatizado).

### 3.1 Controle do Engine (Unreal Engine)
| Ferramenta | O que faz | Custo |
|---|---|---|
| **Plugin MCP oficial da Epic** (`unreal-engine-skills-for-claude-code-plugin`) | Centenas de tools via ToolsetRegistry: actors, blueprints, materiais, Niagara, Control Rig, Sequencer, Gameplay Ability System | Grátis (engine é grátis até faturar; royalty de 5% acima de certo faturamento) |
| **ClaudeUnreal** (comunidade) | 496 comandos via CLI + MCP típico | Grátis |
| **UE MCP** (cwilcox) | 215 tools, 13 recursos, 10 prompts guiados | Grátis |
| **UEMCP** | Sem plugin — usa Python remoto nativo do UE, zero instalação | Grátis |

### 3.2 Controle do Engine (Unity — alternativa não escolhida, mas documentada)
| Ferramenta | O que faz | Custo |
|---|---|---|
| **Unity MCP Server** (oficial, beta) | Integração nativa da Unity com IDEs de IA | Grátis |
| **unity-mcp** (CoplayDev) | 47 tools MIT | Grátis |
| **mcp-unity** (CoderGamester) | Compatível também com Codex CLI | Grátis |

### 3.3 Modelagem 3D / cena (Blender como "mãos" do agente)
| Ferramenta | O que faz | Custo |
|---|---|---|
| **blender-mcp** (ahujasid) | Cria/edita objetos, materiais, executa Python no Blender; já integra Poly Haven, Sketchfab e geração de modelos via Hyper3D Rodin/Hunyuan3D | Grátis (Blender é open source) |

### 3.4 Geração de assets 3D via IA (texto/imagem → malha) — uso manual decidido
| Ferramenta | Free | Pago (entrada) | Observação |
|---|---|---|---|
| **Meshy** (**escolhida para uso manual**) | 100 créditos/mês, mas licença CC BY (modelo fica público) | $20/mês (Pro) — libera uso comercial e privacidade do modelo | Tem MCP próprio também, caso decida automatizar depois |
| **Hyper3D Rodin** | Créditos iniciais grátis; "pague só se baixar" ($0,50–1,50/download) | $30/mês (Creator) | Já integrado ao blender-mcp |
| **Tripo3D** | — | — | Geração muito rápida (~10s) |
| **Kaedim** | — | — | Foco em texturização automática (Projection/Stylized/PBR) |

### 3.5 Texturas PBR (albedo, normal, roughness, AO)
| Ferramenta | Custo |
|---|---|
| **Meshy Texture** | Junto ao plano Meshy |
| **Scenario** | ~$15–20/mês, mantém consistência de estilo artístico entre assets |
| **Polycam** | Textura baseada em scans reais, boa pra rocha/terreno |
| **Poly Haven** (**recomendado como base gratuita**) | 100% CC0, grátis pra sempre |
| **ambientCG** | Outra biblioteca CC0 grátis |

### 3.6 Áudio (voz, música, efeitos sonoros)
| Ferramenta | Free | Pago (entrada) |
|---|---|---|
| **ElevenLabs MCP** | 10.000 créditos/mês (~10min), mas **sem uso comercial liberado** | $6/mês (Starter) — libera uso comercial + clonagem de voz |

> É a única ferramenta que junta voz + efeitos sonoros + música numa API/MCP só — útil pra ambientação (vento, alarmes, rádio da base).

### 3.7 Regra geral de custo dos MCPs
Os **MCPs em si são gratuitos e open source** (são só a "ponte" técnica). O que custa é o **serviço por trás** que o MCP está chamando (a API de geração de IA). Ex: `blender-mcp` não cobra nada, mas se ele gerar um modelo via Hyper3D Rodin, quem cobra é a Hyper3D.

### 3.8 Alternativa sem gastar (ou quase)
- **Modelagem manual no Blender**: 100% grátis, mais lento, mas assets totalmente seus.
- **Geração manual sem MCP**: usar Meshy/Rodin direto pelo site (decisão já tomada pro projeto), gerar nos créditos grátis mensais, baixar e importar manualmente.
- **Assets prontos gratuitos**: ver seção 5 — é o maior atalho de economia.

---

## 4. Vídeo de referência

- **"I Spent 1B Tokens with GPT-6 to Create This…"** — https://youtu.be/9lFE4T7iZKM
- O criador gastou +3 bilhões de tokens e +3 dias tentando construir jogos completos só via prompt, usando Higgsfield MCP + plugin Higgsfield pra Blender.
- Não foi possível confirmar o nome do canal via busca (YouTube bloqueia raspagem de metadados) — recomenda-se checar o histórico de uploads do canal direto pelo app pra achar vídeos semelhantes.

---

## 5. Estratégia de assets: prontos + personalizados

**Lógica geral**: usar assets prontos gratuitos pra tudo que for estrutura genérica (base, corredores, terreno, texturas), e gerar manualmente na Meshy só o que for **específico da história** (rover, criaturas, equipamentos únicos).

### 5.1 Base / instalações (visual sci-fi estilo Subnautica)
| Fonte | Link | Licença |
|---|---|---|
| **Kenney "Space Station Kit"** | kenney.nl/assets/space-station-kit | CC0 (uso livre total) |
| **Sketchfab — "Sci-Fi Space Station Interior Pack: Modular"** | sketchfab.com | Grátis, comercial liberado (não pode revender sem modificar) |
| **Fab (loja da Epic)** | buscar "modular sci-fi" filtrando preço 0 | Varia — pacotes AAA aparecem grátis por tempo limitado, checar sempre |

### 5.2 Texturas/materiais PBR (metal industrial, ferrugem, rocha)
| Fonte | Link | Licença |
|---|---|---|
| **Poly Haven** | polyhaven.com | CC0 |
| **ambientCG** | ambientcg.com | CC0 |

> ⚠️ Correção importante: **Quixel Megascans não é mais 100% grátis** desde 2025 (migrou pro Fab com licença paga na maior parte, alguns itens grátis pontuais). Não contar com ele como fonte gratuita garantida.

### 5.3 Itens específicos/únicos (gerados manualmente)
- Rover, criaturas alienígenas, equipamentos exclusivos da narrativa → gerar manualmente no site da **Meshy** (decisão do usuário), baixar e importar no Blender/Unreal.

---

## 6. Terreno de Marte — pipeline detalhado

### 6.1 Contexto importante
- Dado científico real (NASA/USGS) tem resolução de **~200m/pixel no nível global** — bom pro formato de cratera/canyon, mas **liso demais de perto**.
- Dado de altíssima resolução existe (HiRISE, ~25cm/pixel), mas só cobre **áreas pequenas específicas** — inviável pra um mapa gigante nesse detalhe.
- Muitos modelos prontos (Sketchfab, CGTrader) aplicam **exagero vertical proposital** (ex: 20x) — não são 100% fiéis, são "dramatizados" visualmente.
- Cor de superfície (foto real) e dado de elevação vêm de fontes diferentes — combinar exige alinhamento manual.

**Conclusão**: usar o dado real como **macro-relevo** (formato geral cientificamente correto) e complementar com **detalhe de perto feito no engine** (essa é a abordagem padrão da indústria).

### 6.2 Fontes de dados de terreno

**Portais pra explorar e baixar a área**
- **NASA Mars Trek** — https://trek.nasa.gov/mars/ — portal visual, mais fácil. Escolher região, baixar elevação (GeoTIFF) + imagem de satélite. **Ponto de partida recomendado.**
- **JMARS (Arizona State University)** — https://jmars.asu.edu/download — ferramenta desktop mais robusta/científica, permite recorte fino de área grande. Curva de aprendizado maior.
- **USGS Astrogeology — HRSC/MOLA Blend DEM Global** — https://astrogeology.usgs.gov/search/map/Mars/Topography/HRSC_MOLA_Blend/Mars_HRSC_MOLA_BlendDEM_Global_200mp — dado bruto oficial, cobre o planeta inteiro.

**Regiões específicas recomendadas (pra dar variedade de relevo)**
- **Valles Marineris** — canyon de 4.000 km de comprimento, 7 km de profundidade; tem os canais/leitos de rio secos.
- **Olympus Mons** — maior vulcão do sistema solar.
- **Cratera Gale / Jezero** — onde pousaram os rovers Curiosity e Perseverance; dunas, rocha sedimentar, sinais de rio antigo, com dado em altíssima resolução (HiRISE) disponível.

**Malhas/heightmaps já prontos (mais rápido, área fixa)**
- Sketchfab — "Mars Terrain Model" (John Davies) — malha 3D pronta, gratuita, baseada em MOLA/HRSC.
- CGTrader — "16K Seamless Mars Landscape Terrain" — heightmap 16K grátis, já com crateras/dunas/erosão modeladas.

### 6.3 Pipeline técnico (execução via Claude Code)

**Passo 1 — Aquisição do dado (manual, fora do Claude Code)**
Baixar a área escolhida em GeoTIFF via NASA Mars Trek ou JMARS. Nenhum MCP acessa esses portais diretamente — esse passo é feito no navegador.

**Passo 2 — Conversão GeoTIFF → heightmap (automatizável via Claude Code)**
- Ferramenta: **GDAL** (open source, gratuita, linha de comando).
- `gdal_translate` converte o GeoTIFF em PNG 16-bit em escala de cinza.
- Redimensionar pra resolução aceita pelo Unreal (formato "potência de 2 + 1": ex. 2017×2017, 4033×4033).

**Passo 3 — Importar no Unreal (via Unreal MCP)**
- Claude Code instrui o MCP: `Landscape Mode → Manage → Import from File`.
- Calcular a escala Z com a fórmula oficial da Epic: `(altura máxima em metros) × 100 × 0.001953125`.
- Ativar **World Partition** para permitir área grande sem travar (carrega em pedaços conforme o jogador se movimenta).

**Passo 4 — Textura automática por altura/inclinação (ferramenta pronta encontrada)**
- **LandscapeAutoMaterial** — https://github.com/Kiriql/LandscapeAutoMaterial — projeto **gratuito e open source** para UE 5.7. Lê inclinação e altura do terreno e aplica textura automaticamente (rocha em parede íngreme, poeira/areia no plano) — sem pintura manual.
- Alimentar esse material com texturas do **Poly Haven** (buscar "red rock", "desert sand", "rust metal"), ajustando cor pro tom avermelhado/ferruginoso de Marte.

**Passo 5 — Detalhe de pedra/seixo (nativo do engine)**
- **PCG Framework** (Procedural Content Generation) — nativo do Unreal Engine 5, gratuito, produção-pronta desde a versão 5.7.
- Claude Code monta o grafo do PCG via MCP para espalhar pedras automaticamente com regras (ex: mais densidade em inclinação baixa, menos perto de crateras).
- Gerar manualmente só 5–10 variações de malha de pedra na Meshy — o PCG varia escala/rotação de cada instância, evitando repetição óbvia.

**Passo 6 — Nanite para detalhe geométrico de perto**
- Ativar Nanite nas malhas de pedra e no material do chão — dá detalhe rico de perto sem pesar performance (ajusta nível de detalhe pela distância automaticamente).

### 6.4 Resumo — ferramentas prontas para o terreno
| Item | Link | Custo |
|---|---|---|
| GDAL (conversão de dado) | gdal.org | Grátis |
| LandscapeAutoMaterial | github.com/Kiriql/LandscapeAutoMaterial | Grátis |
| Poly Haven (texturas) | polyhaven.com | Grátis (CC0) |
| PCG Framework | nativo do Unreal 5.4+ (produção-pronta na 5.7) | Grátis (já no engine) |

---

## 7. Base modular funcional — como fazer certo

### 7.1 Por que gerar a base inteira na Meshy não funciona
Geração de IA (Meshy/Rodin) devolve **uma malha única e sólida**, com uma textura só. Isso é ótimo pra objeto decorativo estático, mas quebra a modularidade porque faltam três coisas:
1. **Peças separadas** (parede, chão, teto, porta, esquina) — não uma peça só.
2. **Medida consistente** entre peças — duas gerações separadas na Meshy nunca saem com a escala exatamente igual (é aleatório).
3. **Pontos de encaixe (sockets) e lógica de jogo** — isso é metadado técnico + código, não vem de geração de IA nenhuma.

> Confirmado por análise técnica do setor (2026): ferramentas de geração 3D por IA são **especificamente fracas** em "peças dimensionalmente exatas, kits modulares reutilizáveis, e qualquer asset cujo comportamento de colisão precise ser previsível". Não é falha de ferramenta — é limitação conhecida da tecnologia generativa.

### 7.2 O pipeline correto (100% conduzido via Claude Code, sem trabalho manual do usuário)
| Etapa | Quem faz | Ferramenta |
|---|---|---|
| 1. Geometria da peça (medida exata, encaixe) | Claude Code escreve o script | **blender-mcp** — cria via Python cada peça com a mesma medida de grid e já marca os pontos de encaixe |
| 2. Visual bonito e personalizado | IA generativa de textura | **Scenario** (treina um "modelo próprio" com 10-50 imagens de referência do estilo Subnautica+Marte e gera texturas consistentes em lote) ou **Meshy modo retexture** (aplica textura nova em cima de malha existente, mantendo o UV) |
| 3. Import + funcionalidade no engine | Claude Code + MCP do engine | **Unreal MCP** — importa cada peça, configura sockets, liga ao sistema de snap |

### 7.3 Dois caminhos possíveis
- **Caminho A (recomendado, mais rápido/seguro)**: usar a geometria de um kit modular pronto (Kenney/Sketchfab — seção 5.1, já testada e com medida certa) e só trocar a "pele" via Scenario/Meshy retexture. Menos risco de bug.
- **Caminho B (100% original, mais trabalho)**: Claude Code constrói a geometria do zero via blender-mcp, com medidas definidas pelo usuário. Identidade visual totalmente própria, mas mais iteração/ajuste necessário.

### 7.4 Sistema de encaixe/construção (código, não arte)
- **Grid Snap nativo do Unreal**: simples, só alinha por posição, não "sabe" que peças estão conectadas.
- **Modular Snap System** (plugin, baseado em sockets): bom pra montar cenário estático na mão/via MCP.
- **Sistema tipo "Ultimate Building System"**: necessário quando o **jogador** constrói em tempo real (estilo Surviving Mars/Rust) — precisa de snap por socket + validação estrutural + replicação de rede se for multiplayer. Isso é Claude Code escrevendo Blueprint/C++ via Unreal MCP, não uma ferramenta pronta plug-and-play.

### 7.5 Regra prática de decisão (vale pra qualquer asset, não só a base)
Pergunta a fazer: **"esse objeto vai ser mexido/animado/encaixado por lógica de jogo?"**
- **Sim** (base modular, veículo, personagem) → precisa de estrutura técnica por trás; geração de IA sozinha não basta.
- **Não** (decoração, rocha, prop parado) → pode gerar direto na Meshy e importar, sem preocupação.

---

## 8. Skills para Claude Code / Codex (aceleram o processo)

Skills são pastas de instruções em markdown que o Claude carrega dinamicamente — são portáveis: funcionam em Claude Code, Codex CLI, Gemini CLI e Cursor sem modificação. Instalação padrão:
```
npx skills add <owner>/<repo> --skill <nome> --agent claude-code
```
(adicionar `--global` no final pra ficar disponível em todo projeto, não só o atual).

### 8.1 "Estúdio de jogos" simulado inteiro (achado mais importante)
- **Claude Code Game Studios** (repositórios `mespinro-lab/GameLab` e `Donchitos/Claude-Code-Game-Studios`) — **49 agentes + 72 skills + 12 hooks**, MIT License, grátis.
- Estrutura de estúdio real: diretores de visão, líderes de departamento, especialistas técnicos.
- Tem um **agente específico pra Unreal Engine 5** (`unreal-specialist`): GAS (Gameplay Ability System), Blueprints, Replicação de rede, UMG/CommonUI.
- Comandos por área: `/team-combat`, `/team-narrative`, `/team-ui`, `/team-audio`, `/team-level`, `/team-live-ops`, `/team-polish`.
- Cobre também produção (`/sprint-plan`, `/milestone-review`), QA (`/qa-plan`, `/regression-suite`), lançamento (`/release-checklist`, `/patch-notes`), localização (`/localize`).

### 8.2 Lógica de jogo / programação
- **jeffallan/claude-skills** — skill `game-developer` (403 estrelas, MIT). Unity C#, Unreal C++, Godot: arquitetura ECS, física, colisão, networking multiplayer, shaders, Object Pooling, State Machines. Ativa sozinha com palavras como "Unreal Engine", "física de jogo".
- **Skill oficial da Epic** (`unreal-mcp`, já incluída no plugin MCP da seção 3.1) — ensina convenções corretas de código Unreal (C++/UObject, Slate, UHT).

### 8.3 Pipeline 3D completo
- **DavinciDreams/Agent-Team-Plugins** (`teams/3d-design/`) — time de design 3D com **9 skills + 7 subagentes**: modelagem, escultura, retopologia, rigging, pintura de peso, animação, configurações de exportação corretas pra Unity (escala 1.00, -Z frente) e Unreal (escala 0.01, -X frente) — evita erro clássico de escala na importação.
- **kevinbadi/blender-skills** — image-to-3D via Meshy, animações de câmera, toolkit de automação do Blender.

### 8.4 Qualidade e "sensação" do jogo (fase de polimento)
- **Lagunaswift/GameDevelopmentAudit** — 11 skills que **auditam** o design depois de feito: `emotion-engine-audit`, `game-feel-audit` (resposta/"juice" do combate), `reward-psychology-audit` (checagem ética de loot), `skill-curve-audit` (curva de dificuldade). Não cria conteúdo, revisa e aponta problema.

### 8.5 Ordem sugerida de instalação
1. Claude Code Game Studios (orquestra tudo, inclusive chamando as outras skills)
2. jeffallan/game-developer (lógica de Unreal)
3. DavinciDreams/3d-design (pipeline de Blender)
4. Lagunaswift/GameDevelopmentAudit (só na fase de polimento, mais pra frente)

---

## 9. Processos de criação do jogo — ordem de implementação

> Regra de ouro: **nunca pular pra frente antes de validar o passo anterior**. O erro mais comum (inclusive o que o vídeo de referência da seção 4 parece ter cometido) é gerar arte bonita antes do *core loop* estar provado divertido.

**0. Documento de design** — antes de qualquer código/arte: definir o *core loop* (explorar → coletar recurso → voltar pra base → construir/sobreviver → explorar mais longe), as 3-5 mecânicas centrais, e o que diferencia o jogo de Surviving Mars/Subnautica.

**1. Protótipo cinza ("greybox")** — cubos/cápsulas/terreno provisório, sem arte final. Validar se a mecânica é divertida: personagem anda/interage, sobrevivência básica funciona (oxigênio caindo), construção modular funciona (mesmo com caixas cinza).

**2. Sistemas centrais (código/lógica)** — ainda sem arte final: inventário, crafting, física do traje/oxigênio, IA das criaturas, sistema de construção com snap. Aqui entram pesado os agentes `game-developer` e `unreal-specialist`.

**3. Terreno e ambientação** — pipeline completo da seção 6 (relevo real de Marte, material automático, PCG de pedras). Só faz sentido depois do passo 2 estar minimamente andando.

**4. Conteúdo visual (assets prontos + customizados)** — base modular (seção 7), personagem, criaturas, veículo, props. Ordem: primeiro o que é jogável/testável (base, personagem), depois o "flavor" (criaturas, decoração).

**5. UI/HUD** — inventário, barra de oxigênio, mapa, menu de construção. Frequentemente subestimado.

**6. Áudio** — música ambiente, efeitos sonoros (passos, vento, alarmes), dublagem se tiver (ElevenLabs, seção 3.6). Entra tarde porque depende das mecânicas já estarem fechadas.

**7. Progressão e conteúdo de longo prazo** — árvore de tecnologia, objetivos, narrativa, variedade de criaturas/biomas.

**8. Polimento ("alpha")** — skills de auditoria da seção 8.4: sensação do jogo, resposta de input, juice visual, curva de dificuldade.

**9. Testes (QA)** — bugs, balanceamento, performance em hardware fraco. Ideal ter gente de fora jogando.

**10. Otimização de performance** — checar frame rate, tempo de carregamento, memória — especialmente importante num mundo aberto grande.

**11. Preparação de lançamento** — página na loja (Steam etc.), trailer, capturas de tela, preço, marketing. Trabalho separado do desenvolvimento, comumente subestimado em tempo.

**12. Pós-lançamento** — patches, correção de bugs reportados, conteúdo novo se o jogo performar bem.

---

## 10. Próximos passos em aberto
- Definir o prompt/instrução exata pro Claude Code executar o Passo 2 (conversão GDAL) e Passo 3 (import via Unreal MCP) da seção 6.3 em sequência, como script de setup inicial.
- Verificar licenças comerciais de cada ferramenta de geração (Meshy, Rodin, ElevenLabs) antes de escalar produção, dado o objetivo de lançamento comercial.
- Prototipar o game loop de sobrevivência (oxigênio, crafting, exploração) em escala pequena antes de gerar arte em volume (ver seção 9, passos 0-1).
- Instalar as skills da seção 8 no ambiente de Claude Code/Codex.
- Definir a instrução pro Claude Code montar a base modular via blender-mcp (seção 7.2) — Caminho A ou B.

---

## 11. Metodologia de prompting para os coders (Claude Code/Codex) — Spec-Driven Development

### 11.1 Por que "prompt solto" não é confiável num projeto grande
- Investigação de 2026 documentou que Claude Code frequentemente **lê as regras de um arquivo (ex: CLAUDE.md), consegue recitá-las, mas não as segue** durante a execução — principalmente conforme o contexto enche de código no meio da sessão.
- A Anthropic documentou que tentativas "soltas" (sem estrutura) têm **~33% de taxa de sucesso** em tarefas não-triviais.
- Projetos que adotam **Spec-Driven Development (SDD)** reportam **3 a 10x mais sucesso** na primeira tentativa (dados de relatórios da GitHub/AWS de 2026).

### 11.2 Como funciona o SDD na prática
1. Escrever uma **spec** curta da funcionalidade: o que ela precisa fazer + **critérios de aceite testáveis** (ex: "o oxigênio cai X%/min, alarme dispara abaixo de 20%, morte abaixo de 0%").
2. Claude Code quebra a spec em tarefas menores — **revisão do plano acontece antes de qualquer código ser escrito** (mudar uma spec leva 10 minutos; mudar código já implementado errado leva dias).
3. Implementação tarefa por tarefa, com **hooks automáticos** (scripts de teste/lint que rodam sozinhos) garantindo que a regra foi seguida de verdade — regra só escrita em texto **não é confiável sozinha**.

**Ferramenta recomendada**: **GitHub Spec Kit** — funciona nativamente com Claude Code, é a opção mais portável entre ferramentas.

### 11.3 Estrutura recomendada de CLAUDE.md / AGENTS.md
- **CLAUDE.md**: arquivo carregado automaticamente pelo Claude Code toda sessão (memória persistente do projeto — stack, estrutura de pastas, convenções, comandos de build).
- **Manter curto**: abaixo de 200-250 linhas. Quanto mais longo, pior é seguido (cada linha consome atenção do agente).
- Detalhe técnico específico (ex: convenção de nomeação de Blueprint) deve ficar em arquivos separados dentro de `.claude/rules/`, carregados só quando relevante — não tudo junto na raiz.
- **AGENTS.md**: padrão cross-tool que funciona também no Codex (e na maioria das outras ferramentas de IA). O Claude Code ainda lê CLAUDE.md primeiro, mas pode importar o AGENTS.md com uma linha `@AGENTS.md` no topo do arquivo — assim mantém um arquivo só de instruções válido pros dois.

### 11.4 Outras 4 pesquisas/preparos recomendados antes de começar
1. **GDD com critérios de aceite testáveis** — evoluir o conceito atual (core loop, seção 9) pra specs formais: cada mecânica (oxigênio, crafting, construção) precisa virar uma especificação com número/regra concreta, não só ideia solta. É a matéria-prima das specs do SDD.
2. **Moodboard/art bible visual** — documento com imagens de referência reais (screenshots de Subnautica + fotos reais de Marte), usado tanto pra treinar o Scenario (seção 7) quanto como "regra visual" pro Claude Code seguir ao gerar/ajustar cenário.
3. **Escopo MVP (vertical slice)** — pesquisar como devs solo/pequenos cortam escopo de jogos de mundo aberto pra algo entregável, definindo o "menor jogo completo" que prova o conceito antes de mirar no jogo inteiro.
4. **Aspectos legais de lançamento comercial** — checar se o nome do jogo não colide com marca registrada existente, requisitos da Steam pra publicar, classificação etária, e formalização pra receber receita no Brasil (CNPJ/MEI).
