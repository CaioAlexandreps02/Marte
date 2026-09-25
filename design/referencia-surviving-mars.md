# Surviving Mars — inventário de funcionalidades e o que trazer

> Feito em 25/09/2026. Pesquisa de **tudo** o que o Surviving Mars (Haemimont/Paradox, 2018) tem, incluindo DLCs
> (Space Race, Green Planet, Project Laika, Below & Beyond, In-Dome Buildings Pack, Martian Express, Mysteries
> Resupply, Colony Design Set) e o **Surviving Mars: Relaunched** (10/11/2025, com Martian Assembly, e os DLCs
> novos Feeding the Future, Interplanetary Codex e Machine Utopia).
> Obs.: "Laika" e "Project Laika" são o mesmo pacote (pets + animais de fazenda, 2019).
>
> **Nada aqui é decisão.** É material para o Caio aprovar item a item. Decisões ficam em [DECISOES.md](../DECISOES.md).
> Cruzar com [lista-desejos.md](lista-desejos.md) (seção 0 = visão do Caio) e [catalogo-materiais.md](catalogo-materiais.md).

## Legenda

| Coluna | Valores |
|---|---|
| **Rec.** (recomendação) | **TP** = Trazer parecido · **AD** = Adaptar (diz como) · **CN** = Criar novo (o SM inspira, mas o nosso é outra coisa) · **NT** = Não trazer (diz por quê) |
| **Fase** | **MVP** = entra na fatia vertical da D13 (ou na versão mínima dela) · **Cedo** = logo depois do MVP (Early Access) · **Depois** = meio/fim de jogo · **Talvez** = só se sobrar tempo |
| **D#** | Decisão que o item confirma (✔) ou com que conflita (⚠) |

**Filtro usado (pilares D9):** sem combate · não é city builder visto de cima · não é sobrevivência hardcore ·
não é simulação rigorosa · não é procedural (D8). O jogador está no chão (D1), colonos são números (D2),
automação é o coração (D4).

---

## Resumo

### Contagem

| Categoria | Itens | TP | AD | CN | NT |
|---|---|---|---|---|---|
| 1. Estrutura e loop | 18 | 2 | 11 | 1 | 4 |
| 2. Recursos | 20 | 4 | 13 | 1 | 2 |
| 3. Construções | 110 | 36 | 55 | 0 | 19 |
| 4. Unidades | 26 | 2 | 16 | 3 | 5 |
| 5. Colonos | 24 | 6 | 13 | 0 | 5 |
| 6. Pesquisa | 9 | 1 | 5 | 1 | 2 |
| 7. Desastres e manutenção | 14 | 5 | 8 | 1 | 0 |
| 8. Terraformação | 30 | 14 | 12 | 1 | 3 |
| 9. Mistérios e narrativa | 11 | 2 | 4 | 2 | 3 |
| 10. Interface e gestão | 17 | 4 | 11 | 0 | 2 |
| **Total** | **279** | **76** | **148** | **10** | **45** |

Leitura: **~84% do Surviving Mars entra de alguma forma**, mas a maior parte precisa ser **adaptada** porque o SM é
jogado de cima com drones fazendo tudo, e o nosso é jogado a pé com o jogador (e depois a fábrica) fazendo tudo.
O que fica de fora é quase só: combate/crime, camadas políticas pesadas, microgestão de colono individual e
aleatoriedade (mapa/árvore sorteados).

### A grande tradução (SM → nosso jogo)

| No Surviving Mars… | No nosso jogo… |
|---|---|
| Câmera de cima, clica e drones constroem | Jogador anda, constrói com a ferramenta; drones **ajudam** e depois automatizam (D1, D4) |
| Recursos são "pilhas" que drones carregam | Recursos são itens em **esteiras** e canos entre máquinas (D4) |
| Colono é um indivíduo com traços, idade, nome | Colono é **número + necessidades + vagas**; traços viram **perfis agregados** (D2) |
| Dinheiro (Funding) compra foguetes | Precisa de moeda de troca com a Terra → proposta: **créditos da missão** ganhos com metas e exportações |
| Mapa sorteado, árvore sorteada | Mapa real fixo de Jezero (D8), árvore fixa |
| Anomalias = pontos no mapa que o rover analisa | Anomalias = **lugares reais** (marcos D15) que o jogador visita a pé ou de rover |
| Terraformação por 4 medidores | Igual, e o mundo muda visualmente (D3, D9 pilar 1) |

### Top 15 para trazer (quase como é)

1. **Domos como bolhas habitáveis** com vagas internas para prédios (D3) — MVP (1 domo pequeno).
2. **Grade de energia / água / O₂ com consumo por prédio** e aviso de déficit (D4, D10) — MVP (energia), Cedo (água/O₂).
3. **Foguete de suprimento da Terra com limite de carga (kg) e tempo de viagem**; lista de compra por item (notas D4, lista-desejos §13) — MVP simplificado.
4. **Foguete de passageiros com candidatos da Terra** (escolher quantos/quais especialidades) — MVP (os 5 colonos da D13).
5. **4 medidores de terraformação** (Atmosfera, Temperatura, Água, Vegetação) com marcos que mudam o mundo (D3) — MVP 1 medidor, resto Depois.
6. **Marcos de terraformação com efeito concreto**: 25% temperatura = água líquida; 50% atm/temp = céu azul e fim das ondas de frio; 95% atm = ar respirável → colonos fora do domo (D3) — Depois.
7. **Prédios de terraformação caros e lentos** (fábrica de gases estufa, processador de carbonatos, convector de calor, gerador de campo magnético, plantação de florestas) — Depois.
8. **Tempestade de poeira com previsão** + acúmulo de poeira/manutenção (D10) — MVP.
9. **Onda de frio e meteoritos** com proteção por tecnologia (aquecedor subterrâneo, reforço) (D10) — Depois.
10. **Especialidades de colono** (engenheiro, cientista, botânico, geólogo, médico, oficial) como **vagas preferidas**, não indivíduos (D2) — Cedo.
11. **Conforto → colono quer voltar pra Terra ("earthsick")**; falta de O₂/água/comida mata (D10) — MVP simplificado.
12. **Nascimentos e marcianos natos** (não ficam earthsick) como meta de colônia — Depois.
13. **Ligação de domos por passagens** (grade compartilhada) — Cedo.
14. **Metas da missão** (5 objetivos com recompensa, ex: "30 colonos", "pesquisar 10 techs") (D11 "objetivos de missão") — MVP (2–3 metas).
15. **Maravilhas (Wonders)** como projetos de fim de jogo gigantes que você *vê*: Elevador espacial, Sol artificial, Mina Mohole, Capital City a céu aberto — Depois.

### Top coisas para adaptar (e como)

| SM | Como adaptar |
|---|---|
| **Drone Hub + drones que constroem tudo** | Drones como **ajudantes do jogador** no começo ("robôs que ajudam" — lista §0): carregar itens entre baús, limpar poeira, consertar. Hub com raio visível no chão. Construção continua sendo do jogador. Cedo. |
| **RC Explorer (analisa anomalias)** | É o **rover do jogador** (D7, 3ª pessoa) com scanner; anomalias são marcos reais (D15). MVP. |
| **RC Transport (rotas automáticas)** | **Caminhão de carga** que o jogador dirige **ou** programa numa rota entre dois baús (grava o trajeto dirigindo). Cedo. |
| **RC Dozer + ferramentas de paisagismo** | Já é a D14: ferramenta manual (camada 2) e **drone/veículo de terraplanagem autônomo** (camada 3) — o "carro de terraplanagem" da visão do Caio. Depois. |
| **RC Harvester / Driller** | **Minerador móvel** que o jogador leva até um nó longe da base (D8: recursos distantes). Depois. |
| **Construções dentro do domo** | O jogador **entra no domo a pé** e posiciona os módulos em vagas (grade S/M/L). Visual interno é recompensa (pilar 3). MVP: 1 habitat + 1 fazenda. |
| **Filtros de domo (quem mora onde)** | Painel no **terminal do domo**: vagas por especialidade e "aceitar só X". Sem microgerir indivíduo. Cedo. |
| **Traços de colono (perks/flaws)** | Viram **modificadores agregados da população** do domo ("12% engenheiros veteranos: +10% produção"). D2 permite evoluir. Depois. |
| **Sanidade / conforto / saúde / moral** | Colapsar em **2 barras por domo**: Saúde (vida) e Bem-estar (conforto+sanidade+moral). D10. MVP: só Bem-estar. |
| **Funding (dinheiro)** | **Créditos da missão**: renda fixa do patrocinador + metas cumpridas + **exportação** de metais raros/deutério (catalogo §28). Usado só na Terra (foguetes). Cedo. |
| **Patrocinadores e perfis de comandante** | 3–4 **patrocinadores** que viram modo de dificuldade + bônus temático (ex: "Agência espacial" = mais créditos; "Empresa mineradora" = exporta mais; "Iniciativa de terraformação" = medidores mais rápidos). Perfil do comandante = **traje/ferramenta inicial**. Depois. |
| **Pesquisa por pontos de laboratório** | Pesquisa gasta **amostras físicas** da exploração + pontos de lab (D11). Anomalias dão amostras raras. MVP: 3–5 techs. |
| **Subterrâneo (Below & Beyond)** | Nossas **cavernas reais** (D15): gelo, abrigo do Terraço, poços de colapso. Sem "mapa separado com elevador" — é o mesmo mundo contínuo. Desabamento vira escoramento opcional. Cedo (caverna-tutorial). |
| **Água de depósito subterrâneo** | ⚠ Nosso é diferente (notas D, lista §0): **H₂ da Terra + CO₂ (Sabatier)** no começo → **gelo das cavernas** depois → argila/gipsita. Mesma grade de água do SM. MVP/Cedo. |
| **Trens (Martian Express)** | D4 já prevê trens para longas distâncias; jogador **anda** no trem em 1ª pessoa. Depois. |
| **Lagos e bomba d'água** | O **lago de Jezero volta** (D8, nível −2560 m) com aviso de alagamento já decidido. Depois. |

### O que NÃO trazer (e por quê)

| SM | Motivo |
|---|---|
| Torreta de defesa, Experimental Vehicle, invasão do mistério Marsgate | **Sem combate** (D9). Meteoros: escudo/reforço passivo, não tiro. |
| Renegados, crime, Security Station | Colono como número (D2) e pilar 3 é "cuidar", não policiar. Insatisfação já vira "voltar pra Terra". |
| Câmera de cima, seleção em caixa, ordens por clique | D1. |
| Mapa e árvore de tecnologia sorteados ("Chaos Theory") | D8 (não é procedural); mapa real fixo. |
| Martian Assembly (leis, facções, votação) e independência política | Camada de gestão de cidade pesada; não serve a nenhum pilar. **Talvez** uma versão mínima de "políticas do domo" muito depois. |
| Colônias rivais com IA (Space Race) | Muito custo de IA; o conflito vira competição. Se vier, só como **evento narrativo** (pedido de socorro). |
| Colono individual com nome, idade, ciclo de vida, escola, faculdade, asilo | D2 (só com opção C, "se der"). |
| Cassino, bar, cassino-spire, Game Developer (Paradox), Corporate Office | Humor/sátira do SM, fora do tom realista-estilizado (D12). |
| Pets (Project Laika) como sistema | Não serve a pilar; no máximo **1 mascote** de ambientação (ver seção 4). |
| Mistérios alienígenas (cubos, esferas, wisps, Dredgers, IA, Metatron) | Tom sci-fi fantástico; nossa história será mais pé no chão (Cheyava Falls, missão anterior). Estrutura de mistério sim, conteúdo não. |

---

## 1. Estrutura do jogo e loop principal

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 1.1 | Patrocinador (13 no original + Interplanetary Codex) | Define dinheiro inicial, dificuldade, prédio/veículo/tech único, metas | **AD** | 3–4 patrocinadores como "modo de jogo" com bônus temático e metas próprias. Sem prédios exclusivos (custo de arte). | D11 | Depois |
| 1.2 | Perfil do comandante (~18) | Bônus pequeno (foguetes extras, +20% dinheiro, drones mais rápidos…) | **AD** | Vira **origem do personagem**: traje/ferramenta/pacote inicial diferente. | D10 | Talvez |
| 1.3 | Local de pouso (mapa sorteado, dificuldade por região) | Escolhe coordenada; recursos/desastres variam | **NT** | Mapa único real (D8). O equivalente é escolher **onde** na Variante A montar bases secundárias. | ⚠ D8 | — |
| 1.4 | Metas da missão (5 por patrocinador) | Objetivos com recompensa (prefab, dinheiro, pesquisa) | **AD** | Metas encadeadas que dão direção (D11). Recompensa = créditos, peças da Terra, techs. | ✔ D11 | MVP (2–3) |
| 1.5 | Marcos (Milestones) com pontuação | "Primeiro nascimento", "1000 colonos"… somam pontos | **AD** | Vira **conquistas/diário da colônia** (sem pontuação competitiva). | D11 | Cedo |
| 1.6 | Pontuação final / ranking | Score por marcos × dificuldade | **NT** | Não é jogo de score; progresso é a terraformação. | D9 | — |
| 1.7 | Dificuldade (% de desafio) | Soma de patrocinador + regras + mistério | **AD** | Presets simples (Tranquilo/Normal/Difícil) que mexem no que mata colono e na velocidade (já em D10). | ✔ D10 | Cedo |
| 1.8 | Regras de jogo (Game Rules) | ~30 modificadores (sem desastres, foguete lento, inflação…) | **AD** | Subconjunto útil como opções: sem desastres, construção grátis (criativo), foguetes rápidos, colonos resistentes. | D10 | Depois |
| 1.9 | Modo desafio (semanal) | Cenário fixo com meta e prazo | **NT** | Custo de conteúdo; pode virar DLC futura. | — | — |
| 1.10 | Funding (dinheiro da Terra) | Paga foguetes e importações | **AD** | **Créditos da missão**, só para trocas com a Terra (ver resumo). | notas D4 | Cedo |
| 1.11 | Exportação (metais raros, etc.) | Foguete leva recurso → dinheiro | **AD** | Exportar **metais raros, deutério, amostras científicas** (catalogo §28). Dá sentido a recursos de fim de jogo. | D4 | Depois |
| 1.12 | Terceirização de pesquisa (Outsourcing) | Paga dinheiro → pontos de pesquisa | **AD** | Trocar créditos por pesquisa da Terra; bom atalho no início. | D11 | Depois |
| 1.13 | Prefabs (prédios prontos da Terra) | Chegam por foguete, drones montam sem material | **TP** | Exatamente o "atalho caro" da D4: importar domo/painel pronto vs fabricar. | ✔ D4 | MVP |
| 1.14 | Supply pod (cápsula barata de uso único) | Entrega pequena, sem foguete reutilizável | **AD** | Cápsula de emergência (mais cara por kg, chega rápido). | notas D4 | Cedo |
| 1.15 | Independência da Terra (Relaunched) | Fim de jogo político | **CN** | Nossa "independência" = **colônia autossuficiente** (produz tudo que importava). Meta de campanha, sem política. | D4 | Depois |
| 1.16 | Sol (dia marciano) como unidade de tempo | Ciclo dia/noite, contagem de sols | **TP** | Ciclo dia/noite com sols; afeta energia solar. | D10, D12 | MVP |
| 1.17 | Velocidade do tempo (pausa, 3×) | Controle de tempo do city builder | **NT** | Jogo em 1ª pessoa tem tempo real; no máximo **dormir/pular noite** numa cama. | D1 | — |
| 1.18 | Vitória (metas completas) e "sandbox" depois | Continua jogando após metas | **AD** | Campanha termina num marco de terraformação/história; depois modo livre. | D11 | Depois |

## 2. Recursos

| # | Item SM | Como é produzido/usado no SM | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 2.1 | Metais | Extrator em depósito (com geólogos) ou automático; construção, manutenção | **AD** | Ferro/magnésio/alumínio separados (catalogo). Minerador em nó → fundição → esteira. | ✔ D4 | MVP (ferro) |
| 2.2 | Concreto | Extrator de concreto (depósito) ou processador de rocha residual | **AD** | **Marscrete** de solo marciano + enxofre/aglomerante (catalogo §1). | D4 | MVP/Cedo |
| 2.3 | Água (grade) | Extrator de água em depósito, vaporizador, reciclador | **AD** | ⚠ Nossa rota: H₂ da Terra + CO₂ (Sabatier) → gelo de caverna → argila/gipsita. Canos. | ✔ notas | MVP |
| 2.4 | Oxigênio (grade) | MOXIE (CO₂ → O₂), fazenda hidropônica | **TP** | MOXIE/eletrolisador é real. Canos para o domo. | ✔ D10 | MVP |
| 2.5 | Energia (grade) | Solar, eólica, Stirling, fusão; cabos; baterias | **TP** | Cabos + baterias; solar primeiro. | ✔ D13 | MVP |
| 2.6 | Comida | Fazendas, hidropônica, rancho; 0,2/colono/sol; estraga 4%/sol | **AD** | Estufa/hidropônica dentro do domo; consumo por colono; sem estragar (sim. leve D9). | D2 | MVP (1 fazenda) |
| 2.7 | Metais raros | Extrator de raros → eletrônicos; exportável | **AD** | Temos lista real (Ni-Cu, terras-raras, platinoides — catalogo §raros/meteoríticos). Exportável. | D4 | Depois |
| 2.8 | Polímeros | Refinaria: combustível + água | **AD** | Plástico do **metano** (Sabatier) + CO₂ → rota real. | notas D | Cedo |
| 2.9 | Eletrônicos | Fábrica: metais raros | **AD** | **Só da Terra no começo** (lista §13), depois fabricado com silício + cobre. Ótima progressão D4. | ✔ D4 | MVP (importado) |
| 2.10 | Peças de máquina | Fábrica: metais | **AD** | Montadora (lista §3): aço → peças. Usado em manutenção. | D4 | Cedo |
| 2.11 | Combustível | Refinaria: água → combustível; foguetes e shuttles | **AD** | **Metano + O₂** (Sabatier) — pedido do Caio (lista §0). Abastece foguete de volta e veículos. | ✔ lista §0 | Cedo |
| 2.12 | Minerais exóticos (B&B) | Só em asteroides; prédios especiais | **CN** | Nosso "exótico" = **meteorito ferro-níquel / palasito** (catalogo, Phippsaksla real) + material de Fobos no fim. | catalogo | Depois |
| 2.13 | Sementes (Green Planet) | Importadas ou de árvores; plantação de florestas | **TP** | Sementes/esporos da Terra → musgo/líquen → plantas. | ✔ lista §7 | Depois |
| 2.14 | Rocha residual (Waste Rock) | Subproduto de extração; paisagismo; vira concreto/metais | **AD** | ✔ D14 já diz "cortar gera regolito". Rejeito de mineração = mesmo material (aterro/marscrete). | ✔ D14 | Cedo |
| 2.15 | Pontos de pesquisa | Labs, anomalias, patrocinador | **AD** | Pontos + **amostras físicas** (D11). | ✔ D11 | MVP |
| 2.16 | Data Samples (asteroides, B&B) | Recurso de pesquisa raro | **AD** | Amostras científicas de marcos (Cheyava Falls etc.). | D11 | Cedo |
| 2.17 | Comidas elaboradas (Feeding the Future, Relaunched) | Pão, manteiga, pratos; restaurantes | **NT** | Sim. leve (D9); no máximo "comida variada dá +bem-estar". | D9 | — |
| 2.18 | Depósitos com qualidade/tamanho finitos | Depósito esgota; deep deposits com tech | **AD** | Nós **infinitos** estilo Satisfactory com pureza (baixa/média/alta); "profundo" = mineradora melhor. | D4 | MVP |
| 2.19 | Recursos como pilhas no chão (drones carregam) | Tudo transportado por drone em unidades | **NT** | Nosso transporte é esteira/cano/veículo (D4). Pilhas no chão só para itens soltos (notas D). | ⚠ D4 | — |
| 2.20 | Estoque de grade (tanques de água/O₂, baterias) | Armazenamento separado para grade | **TP** | Tanques e baterias (lista §4/§5). | ✔ | MVP (bateria) |

## 3. Construções

### 3.1 Infraestrutura

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 3.1.1 | Drone Hub | Central com 4 drones, raio de ação, até 20 drones | **AD** | "Estação de drones" com raio **visível no chão**; drones fazem logística curta e manutenção. | ✔ D4, D10 | Cedo |
| 3.1.2 | Drone Hub Extender | Aumenta alcance | **AD** | Antena repetidora (também é o "sinal da base" do traje, D8). | D8 | Depois |
| 3.1.3 | Drone Assembler | Fabrica drones (eletrônicos) | **TP** | Montadora de drones (magnésio + eletrônicos, notas D). | ✔ notas | Cedo |
| 3.1.4 | Recharge Station | Recarrega e limpa drones | **TP** | Posto de recarga (serve drone **e traje** do jogador, D10). | ✔ D10 | Cedo |
| 3.1.5 | Rocket Landing Site | Local de pouso | **TP** | Pad de pouso já no mapa (D16, raio 250 m). | ✔ D16 | MVP |
| 3.1.6 | Landing Pad | Evita poeira do foguete nos prédios | **AD** | O pad da D16 já existe; poeira do pouso suja painéis próximos (pequeno detalhe). | D16 | Cedo |
| 3.1.7 | Universal Depot / depósitos por recurso | Armazéns ao ar livre | **AD** | Baús e armazéns (D13) com esteira de entrada/saída. | ✔ D13 | MVP |
| 3.1.8 | Mechanized Depot | Depósito grande automatizado | **AD** | Armazém industrial (fim de jogo). | D4 | Depois |
| 3.1.9 | Power Cables | Grade de energia | **TP** | Cabos com encaixe automático. | ✔ D4 | MVP |
| 3.1.10 | Power Switch / Pipe Valve | Corta trecho da grade | **TP** | Disjuntor/válvula (barato e útil). | D4 | Cedo |
| 3.1.11 | Life-Support Pipes | Canos de água e O₂ | **TP** | Canos (D4). Mesma lógica de vazamento se quebrar. | ✔ D4 | Cedo |
| 3.1.12 | Tunnel / Universal Tunnel | Liga grades atravessando montanhas | **AD** | Cabo/cano **subterrâneo** que atravessa terreno. | D8 | Depois |
| 3.1.13 | Sensor Tower | Acelera scan, antecipa desastres | **AD** | Estação meteorológica: previsão de tempestade (D10) + revela recursos no mapa. | ✔ D10 | Cedo |
| 3.1.14 | Triboelectric Scrubber | Tira poeira dos prédios em volta | **TP** | Real-ish e resolve a poeira de forma automática (D10 "automatizável"). | ✔ D10 | Depois |
| 3.1.15 | Subsurface Heater | Aquece área contra onda de frio | **TP** | Aquecedor de área (usa água). | D10 | Depois |
| 3.1.16 | MDS Laser | Destrói meteoros | **AD** | ⚠ Tiro em meteoro não é combate, mas prefira **escudo/cúpula de proteção** e reforço (D10). | D10 | Depois |
| 3.1.17 | Defensive Turret | Atira em meteoros **e veículos** | **NT** | Combate (D9). | ⚠ D9 | — |
| 3.1.18 | Shuttle Hub | Naves que levam recursos/colonos entre depósitos | **AD** | Vira **drone de carga voador de longa distância** (D4 "drones para longas distâncias"). | ✔ D4 | Depois |
| 3.1.19 | Tracks + Station + Large Station (Martian Express) | Trem de carga/passageiros | **AD** | Trem (D4), jogador pode embarcar. | ✔ D4 | Depois |
| 3.1.20 | Trade Pad (Space Race) | Comércio com colônias rivais | **NT** | Sem rivais. | — | — |
| 3.1.21 | Recon Center (B&B) | Detecta asteroides | **AD** | Telescópio/observatório — só se houver asteroides no fim. | catalogo | Talvez |
| 3.1.22 | Elevator (B&B) | Liga superfície e subterrâneo | **NT** | Mundo contínuo; se entra na caverna andando (D15). | D15 | — |
| 3.1.23 | Support Strut (B&B) | Reduz risco de desabamento | **AD** | Escora opcional em caverna (se houver desabamento). | D15 | Talvez |
| 3.1.24 | Light Tripod (B&B) | Iluminação subterrânea | **TP** | Luminária de caverna (ajuda a exploração e o visual). | D15 | Cedo |
| 3.1.25 | Passage (passagem entre domos) | Corredor que une domos | **TP** | Corredor pressurizado (lista §1). Jogador anda por ele. | ✔ lista §1 | Cedo |
| 3.1.26 | Fuel Storage, Water Tower, Oxygen Tank | Estoque de grade | **TP** | Tanques. | lista §4 | Cedo |

### 3.2 Energia

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 3.2.1 | Solar Panel / Large Solar Panel | Energia de dia; poeira reduz | **TP** | Primeiro gerador (D13). | ✔ D13 | MVP |
| 3.2.2 | Solar Array (SpaceY) | Painel gigante | **AD** | Fazenda solar de fim de jogo. | — | Depois |
| 3.2.3 | Wind Turbine / Large / Shrouded (Relaunched) | Mais forte em tempestade e em altitude | **AD** | Eólica fraca em Marte (ar fino) mas **melhora com a terraformação da atmosfera** — ótimo "mundo muda". | D3 | Depois |
| 3.2.4 | Stirling Generator / Advanced | Nuclear-ish, fecha contra poeira | **AD** | **Kilopower** (lista §5), vem da Terra. | ✔ lista §5 | Cedo |
| 3.2.5 | Fusion Reactor | Muita energia, fim de jogo | **TP** | Fusão com **deutério de Marte** (catalogo §28). | ✔ lista §5 | Depois |
| 3.2.6 | Power Accumulator / Atomic Accumulator | Baterias | **TP** | Baterias (Na-íon do sal-gema, catalogo §21). | ✔ | MVP |
| 3.2.7 | Artificial Sun (Wonder) | 600 energia + calor + solar à noite | **AD** | Maravilha de fim de jogo. | D3 | Depois |

### 3.3 Produção e extração

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 3.3.1 | Metals Extractor (precisa de trabalhadores) | Mina de metal em depósito | **AD** | Minerador em nó (D4) — **sem precisar de colono** no começo; colonos aumentam produção depois (D3). | ✔ D4 | MVP |
| 3.3.2 | Automated Metals Extractor | Mina sem trabalhador | **AD** | Versão avançada (upgrade). | D4 | Cedo |
| 3.3.3 | Concrete Extractor | Concreto de depósito | **AD** | Escavadeira de solo marciano → Marscrete. | D4 | Cedo |
| 3.3.4 | Rare Metals Extractor | Metais raros | **AD** | Mineradora em veio raro longe da base (D8). | D8 | Depois |
| 3.3.5 | Water Extractor | Água de depósito | **AD** | Perfuratriz de gelo em caverna (lista §2). | ✔ notas | Cedo |
| 3.3.6 | Moisture Vaporator | Água do ar (melhora com terraformação) | **TP** | Coletor atmosférico (lista §2), melhora com o medidor de Água. | D3 | Cedo |
| 3.3.7 | Metals Refinery / Rare Metals Refinery (Índia/Brasil) | Refina minério | **TP** | Fundição (D4). | ✔ D4 | MVP |
| 3.3.8 | Fuel Refinery | Água → combustível | **AD** | Reator de Sabatier (lista §3). | ✔ lista §3 | Cedo |
| 3.3.9 | Polymer Factory | Polímeros | **AD** | Planta de plástico (metano). | D4 | Cedo |
| 3.3.10 | Electronics Factory (+ small, dentro do domo) | Eletrônicos | **AD** | Fábrica fora do domo (fábrica é fora, colônia é dentro — separa os pilares 2 e 3). | D4 | Depois |
| 3.3.11 | Machine Parts Factory (+ small) | Peças | **AD** | Montadora (lista §3). | D4 | Cedo |
| 3.3.12 | Concrete Plant (Rússia) | Concreto a partir de combustível | **NT** | Redundante. | — | — |
| 3.3.13 | Waste Rock Processor | Rejeito → concreto | **AD** | Britador: regolito cortado (D14) → Marscrete. | ✔ D14 | Cedo |
| 3.3.14 | Mohole Mine (Wonder) | Metais sem depósito | **AD** | Poço profundo de fim de jogo; também **calor geotérmico** (ajuda Temperatura). | D3 | Depois |
| 3.3.15 | The Excavator (Wonder) | Concreto infinito | **AD** | Escavadeira gigante (visual impressionante em 1ª pessoa). | — | Talvez |
| 3.3.16 | Micro-G Extractor / Mining Station (asteroides) | Mina em asteroide | **NT** | Asteroides fora do escopo (1ª pessoa no chão). | D1 | — |
| 3.3.17 | Asteroid Lander | Prédio-foguete que pousa em asteroide | **NT** | Idem; talvez **Fobos** no pós-lançamento. | — | Talvez |
| 3.3.18 | Research Lab / Hawking Institute | Pesquisa com colonos | **AD** | Laboratório (lista §11) que processa amostras. | ✔ D11 | MVP |
| 3.3.19 | Biolab / Bottomless Pit Lab | Pesquisa especial | **AD** | Lab de biologia para Cheyava Falls. | notas D | Depois |
| 3.3.20 | Omega Telescope (Wonder) | Pesquisa + breakthroughs | **AD** | Radiotelescópio no **mirante** (D15) como maravilha. | D15 | Depois |
| 3.3.21 | Space Elevator (Wonder) | Troca com a Terra barata | **TP** | Maravilha máxima de logística Terra↔Marte (dá pra ver o cabo subindo). | notas D4 | Depois |

### 3.4 Suporte à vida

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 3.4.1 | MOXIE | CO₂ → O₂ | **TP** | Nome real, manter. | ✔ lista §3 | MVP |
| 3.4.2 | Oxygen Tank | Estoque O₂ | **TP** | — | — | Cedo |
| 3.4.3 | Water Tower | Estoque de água | **TP** | — | — | Cedo |
| 3.4.4 | Water Reclamation (spire) | Reduz consumo de água do domo | **AD** | Reciclador de água/ar (lista §6) como **módulo do domo**. | ✔ lista §6 | Cedo |
| 3.4.5 | Oxygen consumption por domo | Domo gasta O₂/água/energia | **TP** | Cada domo consome grade. | ✔ D10 | MVP |

### 3.5 Domos

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 3.5.1 | Micro Dome (3 vagas grandes) | Domo inicial pequeno | **TP** | O **primeiro domo** do MVP. | ✔ D13 | MVP |
| 3.5.2 | Basic Dome (6) | Domo padrão | **TP** | Segundo tamanho. | D3 | Cedo |
| 3.5.3 | Barrel Dome (formato longo) | Domo alongado | **AD** | Domo-túnel (encaixa em faixas planas estreitas — nosso terreno é irregular, D8). | D8 | Depois |
| 3.5.4 | Trigon / Mega Trigon | Estrutural de metal | **AD** | Variação de estética (não precisa ser igual). | — | Depois |
| 3.5.5 | Medium Dome (+ vagas pequenas p/ spire) | Domo médio | **TP** | — | D3 | Cedo |
| 3.5.6 | Mega Dome (24) | Domo grande | **TP** | Domo grande com **cidade visível dentro**. | D3 | Depois |
| 3.5.7 | Oval / Diamond | Formatos especiais | **AD** | 1–2 formatos especiais como recompensa de tech. | — | Depois |
| 3.5.8 | Geoscape Dome (Wonder) | Domo com paisagem natural, +conforto | **TP** | Maravilha: domo com **terreno, lago e árvores** — "pedaço da Terra". | D3 | Depois |
| 3.5.9 | Capital City (Wonder, pós-terraformação) | Cidade aberta sem O₂ | **AD** | Clímax: cidade **a céu aberto** quando atmosfera ≥ 95% (D3 "colonos saem dos domos"). | ✔ D3 | Depois |
| 3.5.10 | Naturalist Habitat (Relaunched) | Casa externa sem grade | **AD** | Casa ao ar livre pós-terraformação. | D3 | Depois |
| 3.5.11 | Micro-G Habitat (asteroide) | — | **NT** | Sem asteroides. | — | — |
| 3.5.12 | Vagas S/M/L e spire | Grade interna fixa por domo | **AD** | Grade interna (jogador posiciona a pé). | D2 | MVP |
| 3.5.13 | Abrir domo (Open Domes law) | Remove vidro após terraformação | **TP** | Evento lindo: vidro do domo se abre (pilar 1). | ✔ D3 | Depois |
| 3.5.14 | Dome skins (Stellaris, etc.) | Cosméticos | **NT** | Custo de arte; DLC futura. | — | — |
| 3.5.15 | Rachadura no domo (meteoro) → vazamento | Domo perde O₂ até consertar | **TP** | Ótimo gancho de manutenção em 1ª pessoa (o jogador vai consertar). | ✔ D10 | Depois |

### 3.6 Dentro do domo (casas, serviços, spires)

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 3.6.1 | Living Quarters (4) / Living Complex (14) / Apartments (24) | Casas por capacidade | **AD** | 3 tamanhos de habitat (capacidade é número, D2). | ✔ D2 | MVP (1) |
| 3.6.2 | Smart Home / Smart Complex / Smart Apartments (In-Dome Pack) | Casa com +conforto (eletrônicos) | **AD** | Upgrade de habitat (mais conforto). | D2 | Depois |
| 3.6.3 | Arcology (spire) | Moradia vertical | **AD** | Torre habitacional no centro do domo grande. | — | Depois |
| 3.6.4 | Nursery / Large Nursery | Crianças | **NT** | Sem ciclo de vida individual (D2). Nascimentos viram número. | D2 | — |
| 3.6.5 | Retirement Home (In-Dome) | Idosos | **NT** | Idem. | D2 | — |
| 3.6.6 | Playground / School / School Spire | Traços em crianças | **NT** | Idem. | D2 | — |
| 3.6.7 | Martian University | Treina especialidade | **AD** | "Centro de treinamento": converte colonos sem especialidade → especialistas (número). | D2 | Depois |
| 3.6.8 | Hydroponic Farm / Farm (dentro do domo) | Comida (+O₂ na hidropônica) | **TP** | Estufa (lista §7). | ✔ lista §7 | MVP |
| 3.6.9 | Ranch (Laika) | Animais para carne | **NT** | Complexidade de sim. Talvez só "proteína" de insetos/fungos (real e simples). | D9 | Talvez |
| 3.6.10 | Fungal Farm / Insect Farm | Comida com pouca água | **AD** | Alternativa de comida (combina com a água escassa do começo). | notas | Depois |
| 3.6.11 | Grocer / Diner / Mega Mall | Serviço de comida | **AD** | Agregado em 1 módulo "Refeitório" (serviço de comida → bem-estar). | D2 | Cedo |
| 3.6.12 | Medical Post / Infirmary / Hospital (In-Dome) / Medical Spire | Saúde | **AD** | **Enfermaria** (lista §6), 2 níveis. | ✔ lista §6 | Cedo |
| 3.6.13 | Sanatorium | Remove traços ruins | **NT** | Sem traços individuais. | D2 | — |
| 3.6.14 | Spacebar / Casino / Gambling | Lazer | **AD** | 1 módulo de lazer genérico ("Área comum"). Sem cassino. | D12 | Cedo |
| 3.6.15 | Gym / Open Air Gym / Park / Garden / Hanging Gardens / Tai Chi Garden | Conforto, saúde, decoração | **AD** | Parque/jardim (conforto + visual verde dentro do domo, pilar 3). | lista §6 | Cedo |
| 3.6.16 | Art Workshop / Amphitheater / Temple (Church) | Lazer temático | **NT** | Excesso de variedade de serviço; agregar em "Área comum". | — | — |
| 3.6.17 | Security Station | Contra renegados/crime | **NT** | Sem crime (D9/D2). | ⚠ D9 | — |
| 3.6.18 | Network Node (spire) | +pesquisa | **AD** | Upgrade do lab. | D11 | Depois |
| 3.6.19 | Martian Assembly (spire, Relaunched) | Leis e facções | **NT** | Ver resumo. | — | — |
| 3.6.20 | Law Office (Interplanetary Codex) | Política | **NT** | Idem. | — | — |
| 3.6.21 | Corporate Office / Game Developer | Gera dinheiro | **NT** | Sátira; exportação cobre isso. | D12 | — |
| 3.6.22 | Olympus Hotel / turismo | Hotel para turistas | **AD** | Turismo como **fonte de créditos** tardia (ver 5.x). | — | Talvez |
| 3.6.23 | Decorações (Colony Design Set, ~25) | Estátuas, fontes, luzes | **AD** | Poucas decorações que dão conforto; o jogador gosta de enfeitar em 1ª pessoa. | pilar 3 | Depois |
| 3.6.24 | Project Morpheus (Wonder) | Dá perks aleatórios | **NT** | Sem perks individuais. | D2 | — |
| 3.6.25 | Pets passeando (Project Laika) | Animais no domo, +conforto | **AD** | 1–2 animais de **ambientação** (ex: cachorro da base) — carisma barato. | D12 | Talvez |

### 3.7 Terraformação (Green Planet) — ver também seção 8

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 3.7.1 | GHG Factory | Gases estufa → Temperatura | **TP** | Fábrica de gases super-estufa (PFC com flúor real, catalogo). | ✔ lista §10 | Depois |
| 3.7.2 | Carbonate Processor | Libera CO₂ → Atmosfera | **TP** | Processador de carbonatos (Jezero tem carbonatos reais, catalogo §13). | ✔ | Depois |
| 3.7.3 | Core Heat Convector | Calor do núcleo → Temperatura | **AD** | Poço geotérmico profundo (fundir com Mohole). | — | Depois |
| 3.7.4 | Magnetic Field Generator | Reduz perda de atmosfera | **TP** | Gerador de campo magnético. | D3 | Depois |
| 3.7.5 | Forestation Plant | Espalha plantas → Vegetação | **TP** | Plantadeira (lista §10 musgo/líquen). | ✔ | Depois |
| 3.7.6 | Water Pump / Lake (small → huge) | Enche lagos → Água | **AD** | O **lago de Jezero** (D8) é o lago; bombas em pontos reais. | ✔ D8 | Depois |
| 3.7.7 | Soil Enricher / Soil Decontamination | Melhora solo | **AD** | **Biorreator de perclorato** (lista §7) — ciência real. | ✔ lista §7 | Depois |
| 3.7.8 | Tree Farm / Open Farm | Plantas ao ar livre (sementes) | **TP** | Fazenda a céu aberto pós-temperatura. | D3 | Depois |
| 3.7.9 | Amplify (upgrade de terraformação) | +50% por polímero | **TP** | Upgrade simples, bom sumidouro de produção (D3 "só sobe com escala"). | ✔ D3 | Depois |
| 3.7.10 | Landscaping: Flatten / Ramp / Texture / Rock Formation | Ferramentas de terreno | **AD** | D14 camadas 2–3. Textura e "criar rochas" como extra decorativo. | ✔ D14 | Cedo |
| 3.7.11 | Remove Rocks / Clean up | Limpa obstáculos | **TP** | Remover pedras do campo de rochas (D16) gera material. | ✔ D16 | MVP |

## 4. Unidades

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 4.1 | Drone comum | Constrói, carrega, conserta; bateria | **AD** | Ajudante: carrega entre baús, limpa painéis, conserta; **não constrói no lugar do jogador** no início. | ✔ D4, lista §0 | Cedo |
| 4.2 | Bateria do drone + recarga | Drone para quando acaba | **TP** | Simples e visível (drone volta ao posto). | D10 | Cedo |
| 4.3 | Raio do hub, controle de drones | Área de serviço ajustável | **TP** | Raio visível. | — | Cedo |
| 4.4 | Wasp Drone (Japão) | Drone voador | **AD** | Drone voador = versão avançada (longa distância, D4). | ✔ D4 | Depois |
| 4.5 | Biorobots (Inner Light / tech) | Robô humanoide colono | **AD** | Base do "Machine Utopia": robôs ocupam vagas de trabalho → combina com **protótipo A (só robôs)** da D2. | ✔ D2 | Depois |
| 4.6 | Drones como prefab em estoque global | Drone "guardado" | **NT** | Tudo físico no mundo (D5, ID único). | D5 | — |
| 4.7 | RC Explorer | Analisa anomalias, scan | **AD** | Rover do jogador com scanner (D7). | ✔ D7, D13 | MVP |
| 4.8 | RC Transport | Carrega recursos, rotas automáticas | **AD** | Caminhão de carga (lista §8), rota gravada. | ✔ lista §8 | Cedo |
| 4.9 | RC Commander | Carrega e comanda drones em campo | **AD** | **Rover-base móvel**: recarrega traje e drones fora da base (expedições longas, D8). | D10 | Depois |
| 4.10 | RC Harvester | Coleta concreto de superfície | **AD** | Minerador móvel. | D8 | Depois |
| 4.11 | RC Constructor | Constrói e carrega | **AD** | Veículo de construção remota (constrói blueprint longe). | D4 | Depois |
| 4.12 | RC Dozer | Terraplanagem | **AD** | **Carro de terraplanagem autônomo** (visão do Caio, D14 camada 3). | ✔ D14 | Depois |
| 4.13 | RC Driller | Metal de subsolo | **AD** | Perfuratriz móvel para gelo de caverna. | — | Talvez |
| 4.14 | RC Generator / Seeker | Rover com solar / sensor | **AD** | Módulos acopláveis no rover (solar, sensor). | — | Depois |
| 4.15 | RC Safari | Turismo | **NT** | — | — | — |
| 4.16 | Experimental Vehicle (atira meteoros) | — | **NT** | Combate. | ⚠ D9 | — |
| 4.17 | Shuttle / Jumper Shuttle | Transporte aéreo | **AD** | Drone de carga pesado (D4). | D4 | Depois |
| 4.18 | Trem (Martian Express) | Carga + passageiros | **AD** | Trem (D4). | ✔ D4 | Depois |
| 4.19 | Rocket (cargo 50 t + 12 passageiros) | Vai e volta da Terra, precisa reabastecer | **AD** | Foguete que **volta à Terra com combustível produzido aqui** — ciclo real (Mars Direct). Primeiro sem precisar reabastecer. | ✔ notas | MVP |
| 4.20 | Tipos de foguete por patrocinador (Zeus, Dragon) | Capacidades diferentes | **AD** | Upgrade de foguete por tech/créditos. | — | Depois |
| 4.21 | Supply Pod | Cápsula única | **AD** | Cápsula de emergência. | — | Cedo |
| 4.22 | Expedições (foguete para anomalia planetária) | Missão fora do mapa, texto com escolhas | **CN** | "Missão de sonda": manda drone/foguete a um lugar fora do mapa (Olympus Mons, polo) → evento em texto + recompensa. Barato de produzir. | D11 | Depois |
| 4.23 | Pets (25 tipos, Project Laika) | Cosmético/conforto | **NT** | Ver 3.6.25. | — | — |
| 4.24 | Animais de fazenda (Laika) | Rancho | **NT** | Ver 3.6.9. | — | — |
| 4.25 | Jogador | (não existe no SM) | **CN** | O jogador é a unidade principal: traje, ferramentas, veículos (D1, D10). | ✔ D1 | MVP |
| 4.26 | Robôs do começo (lista §0) | (não existe no SM) | **CN** | 1–2 robôs iniciais que chegam no foguete com o jogador (protótipo A da D2). | ✔ D2 | MVP |

## 5. Colonos

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 5.1 | Saúde | 0–100; <30 não trabalha | **AD** | Barra de **Saúde por domo** (média). | ✔ D2 | Cedo |
| 5.2 | Sanidade | 0–100; baixa → colapso/suicídio | **AD** | Fundir em **Bem-estar**. Sem suicídio (tom). | D2, D9 | Cedo |
| 5.3 | Conforto | 0 → earthsick | **AD** | Bem-estar baixo → colonos pedem pra voltar. | ✔ D10 | MVP |
| 5.4 | Moral (derivado) | Afeta produtividade ±1/ponto | **AD** | Bem-estar alto → +produção dos prédios com colonos. | D3 | Cedo |
| 5.5 | Especialidades (7 + turista) | Vaga preferida, −50 fora dela | **TP** | 5–6 especialidades como tipo de vaga. | ✔ D2 | Cedo |
| 5.6 | Perks (~12) | Traços bons | **AD** | Agregados ("% veteranos") — ver resumo. | D2 | Depois |
| 5.7 | Flaws (~13) | Traços ruins | **NT** | Microgestão de indivíduo; gera frustração sem pilar. | D2 | — |
| 5.8 | Quirks (Founder, Martianborn, Clone…) | Marcadores especiais | **AD** | Só **Fundador** (os 5 primeiros, D13) e **Marciano nato** (contagem). | D13 | Depois |
| 5.9 | Idades (criança → idoso) | Ciclo de vida | **NT** | D2. População só cresce/diminui. | D2 | — |
| 5.10 | Nascimentos (pontos de fertilidade) | Precisa conforto e moradia | **AD** | Taxa de nascimento por domo se Bem-estar alto e vaga livre. | D2 | Depois |
| 5.11 | Mortes (fome, sufocação, desidratação, frio, idade) | — | **TP** | Causas letais já na D10 (depende da dificuldade). | ✔ D10 | MVP |
| 5.12 | Earthsick → vai embora no foguete | — | **TP** | Exatamente D10. | ✔ D10 | MVP |
| 5.13 | Candidatos da Terra (pool de applicants) | Lista para escolher | **AD** | Tela "próximo voo": quantos e quais especialidades (sem ficha individual). | ✔ lista §13 | MVP |
| 5.14 | Turistas | Ficam alguns sols, pagam | **AD** | Fonte de créditos no fim (precisa hotel/lazer). | — | Talvez |
| 5.15 | Renegados / crime | Moral baixa → crime | **NT** | Ver resumo. | ⚠ D9 | — |
| 5.16 | Trabalho: turnos (3 × 8 h), turno noturno −sanidade | Vagas por turno | **AD** | Prédio tem vagas; opcional "operação 24h" com custo de bem-estar. Sem turnos individuais. | D2 | Depois |
| 5.17 | Distância casa-trabalho (mesmo domo ou ligado) | −10 fora do domo | **AD** | Prédio precisa estar no **alcance de um domo** (raio). Simples e espacial. | D2 | Cedo |
| 5.18 | Serviços por interesse (lazer, comida, saúde…) | Colono visita serviços que combinam | **AD** | Domo tem "cobertura de serviços" (comida, saúde, lazer) → soma no Bem-estar. | D2 | Cedo |
| 5.19 | Sem-teto (homeless) | Sem casa → penalidades | **TP** | Colono sem vaga de moradia = alerta. | D2 | MVP |
| 5.20 | Desempregado | Sem vaga de trabalho | **TP** | Número visível. | D2 | Cedo |
| 5.21 | Colonos andando visíveis | Simulação individual | **AD** | "Poucos visíveis, só ambientação" (D2). | ✔ D2 | Cedo |
| 5.22 | Colonos trabalhando fora (open-air) pós-terraformação | Vivem fora dos domos | **TP** | Clímax da terraformação (D3). | ✔ D3 | Depois |
| 5.23 | Colonos "presos"/não usam passagem (bug famoso) | Pathfinding ruim | **NT** | Lição: como são números, **não há pathfinding de colono** — elimina a crítica nº 1. | ✔ D2 | — |
| 5.24 | Suicídio, crime, infecção (mistério) | Temas pesados | **NT** | Tom do jogo. | D9 | — |

## 6. Pesquisa

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 6.1 | 5 campos (Biotech, Engineering, Physics, Robotics, Social) + Recon/Expansion (B&B) | Colunas da árvore | **AD** | 4–5 ramos ligados aos pilares: Fábrica, Colônia, Exploração, Terraformação (+ Energia). | ✔ D11 | Cedo |
| 6.2 | ~216 techs + 66 breakthroughs | Árvore enorme | **AD** | Árvore **menor e fixa**, com cada tech liberando algo que se vê. | D11 | Cedo |
| 6.3 | Árvore sorteada (ordem aleatória por coluna) | Replay | **NT** | D8 (não procedural). | ⚠ D8 | — |
| 6.4 | Custo crescente por tech | +10% por nível | **TP** | — | — | Cedo |
| 6.5 | Breakthroughs (techs especiais achadas em anomalias) | Descobertas raras | **AD** | **Techs escondidas em marcos/cavernas** — recompensa de exploração (pilar 4). Relaunched deixa escolher 1 de 3 — bom. | ✔ D11, D15 | Cedo |
| 6.6 | Pesquisa do patrocinador (fluxo da Terra) | Pontos passivos | **AD** | Pequeno fluxo da Terra + terceirização (1.12). | — | Cedo |
| 6.7 | Labs com retornos decrescentes | Diminui a cada lab igual | **NT** | Regra opaca; nosso custo é amostras. | — | — |
| 6.8 | Scan de setores / deep scan | Revela recursos por setor | **AD** | Scanner do traje/rover + torre (3.1.13). | D11 | MVP |
| 6.9 | Pesquisa gerando amostras | (não existe no SM) | **CN** | **Amostras físicas** carregadas até o lab (D11). | ✔ D11 | MVP |

## 7. Desastres, eventos e manutenção

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 7.1 | Tempestade de poeira (normal) | +poeira, foguete não decola | **TP** | D10, com previsão. | ✔ D10 | MVP |
| 7.2 | Tempestade eletrostática | Raios desligam prédios | **AD** | Variante rara; raio desliga um prédio que o jogador religa. | D10 | Depois |
| 7.3 | Grande tempestade | Longa, severa | **AD** | Evento de campanha ("a grande tempestade" — Perdido em Marte). | D10 | Depois |
| 7.4 | Onda de frio | Energia ×3, congela | **TP** | Aquecimento + mais consumo. | D10 | Depois |
| 7.5 | Meteoros / chuva de meteoros | Destroem prédios, racham domo | **AD** | Raros (D10); escudo/reforço; cratera nova vira marco com meteorito ferroso (catalogo). | ✔ D10 | Depois |
| 7.6 | Dust devil (redemoinho) | Suja tudo por onde passa | **TP** | Visual lindo em 1ª pessoa e **real em Jezero** (Perseverance filmou). | ✔ D12 | Cedo |
| 7.7 | Marsquake (terraformação) | Enche manutenção | **AD** | Efeito colateral de projetos de terraformação. | D3 | Depois |
| 7.8 | Chuva tóxica (terraformação) | Mata plantas, poças tóxicas | **AD** | Fase intermediária da terraformação; drones limpam. | D3 | Depois |
| 7.9 | Desabamento de caverna (B&B) | Destrói construções | **AD** | Só em cavernas não escoradas, com aviso. | D15 | Talvez |
| 7.10 | Tempestade solar / radiação | (não existe no SM) | **CN** | Já na D10: abrigo temporário. | ✔ D10 | Depois |
| 7.11 | Manutenção (barra que enche; drones consertam com recurso) | Prédios quebram sem manutenção | **AD** | Manutenção pede **peças de máquina**; jogador conserta no começo, drones depois (D10). | ✔ D10 | Cedo |
| 7.12 | Poeira acumulada (reduz produção) | Painéis sujos | **TP** | D10. | ✔ D10 | MVP |
| 7.13 | Falha de cabo/cano (vazamento) | Grade quebra, drone conserta | **TP** | Ótima tarefa em 1ª pessoa. | D10 | Cedo |
| 7.14 | Story Bits (eventos com escolha) | Pop-ups narrativos aleatórios | **AD** | Eventos **pelo rádio** da Terra/colônia, poucos e escritos à mão. | D11 | Cedo |

## 8. Terraformação (Green Planet)

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 8.1 | Atmosfera (0–100%) | Densidade/composição | **TP** | Medidor 1. | ✔ D3 | MVP (1 medidor) |
| 8.2 | Temperatura | Temperatura global | **TP** | Medidor 2. | ✔ D3 | Depois |
| 8.3 | Água | Água superficial | **TP** | Medidor 3 — liga ao **lago de Jezero** (D8). | ✔ D3, D8 | Depois |
| 8.4 | Vegetação | Plantas/bactérias | **TP** | Medidor 4. | ✔ D3 | Depois |
| 8.5 | Perda natural de atmosfera | Atmosfera cai sem campo magnético | **AD** | Leve; só se não construir o gerador de campo. | D3 | Depois |
| 8.6 | Limiares com efeito (25/50/80/95%) | Muda clima, céu, desastres | **TP** | Marcos visuais (D3, D12 céu caramelo → azul). | ✔ D3, D12 | Depois |
| 8.7 | Céu azul (50% atm/temp) | Visual | **TP** | ✔ paleta D12. | ✔ D12 | Depois |
| 8.8 | Chuva (água + atm) | Chuva real | **AD** | Chuva enche o lago e rio (Neretva Vallis volta a correr — D9 pilar 1). | ✔ D9 | Depois |
| 8.9 | Chuva tóxica | Ver 7.8 | **AD** | — | D3 | Depois |
| 8.10 | Lagos (pequeno → enorme) | +Água | **AD** | Lago de Jezero + crateras menores que enchem (cratera-atol, D15). Aviso de alagamento já decidido. | ✔ D8 | Depois |
| 8.11 | Gelo permanente derrete (50% temp) | Libera água | **AD** | Gelo das cavernas derrete → muda onde tem gelo (efeito colateral bom de narrar). | D15 | Depois |
| 8.12 | Qualidade do solo | Plantas precisam | **AD** | Perclorato no solo (catalogo §9) → biorreator limpa. | ✔ lista §7 | Depois |
| 8.13 | Estágios de vegetação (líquen → grama → arbusto → árvore → floresta mista) | Progressão visual | **TP** | Paleta musgo da D12. | ✔ D12 | Depois |
| 8.14 | Sementes espalhadas por plantadeira | Área de plantio | **TP** | — | — | Depois |
| 8.15 | Vegetation resilient (tech) | Reduz requisitos | **TP** | Tech. | — | Depois |
| 8.16 | Projeto: Derreter calotas polares | Grande +Água, efeito colateral | **AD** | **Projetos especiais** = missões fora do mapa (como 4.22) com evento narrado + mudança global. | ✔ lista §10 | Depois |
| 8.17 | Projeto: Capturar asteroides de gelo | +Água, marsquakes | **AD** | Idem (impacto visível no horizonte). | — | Depois |
| 8.18 | Projeto: Espelho espacial | +Temperatura | **TP** | Real (proposta científica) — lista §10 "espelhos". | ✔ lista §10 | Depois |
| 8.19 | Projeto: Importar gases estufa | +Atm, chuva tóxica | **AD** | Custa créditos (usa o sistema da Terra). | — | Depois |
| 8.20 | Projeto: Semear vegetação | +Vegetação | **AD** | — | — | Depois |
| 8.21 | Escudo magnético (L1) | Protege atmosfera | **AD** | Pode ser projeto especial em vez de prédio. | D3 | Depois |
| 8.22 | Colonos ao ar livre (95% atm) | Fim do domo | **TP** | D3. | ✔ D3 | Depois |
| 8.23 | Terraformação local (Geoscape, Localized Terraforming) | Bolha verde | **TP** | D3 "local" = domos/estufas desde cedo. | ✔ D3 | MVP |
| 8.24 | Fim das ondas de frio / dust devils / meteoros com terraformação | Recompensa sistêmica | **TP** | Ameaças mudam com o planeta. | D10 | Depois |
| 8.25 | Taxa em %/sol extremamente lenta, depende de muitos prédios | Escala | **AD** | ✔ D3 "só sobe com escala" — mas **mostrar ETA** para não parecer parado (crítica). | ✔ D3 | Depois |
| 8.26 | Flatten/Ramp/Remove rocks com Dozer | Paisagismo | **TP** | D14. | ✔ D14 | Cedo |
| 8.27 | Resultado sem visual no MVP | — | **CN** | D13: 1 medidor sem mudança visual. | ✔ D13 | MVP |
| 8.28 | Animais soltos no planeta (Laika) | Fauna | **NT** | Fora do realismo; no máximo líquen/musgo/árvores. | D9 | — |
| 8.29 | Toxic pools | Poças para drones limparem | **NT** | Microtarefa sem valor em 1ª pessoa. | — | — |
| 8.30 | Terraformation rewards visuais só parciais (critica) | — | **NT** | Lição: nosso visual precisa ser **dramático** (pilar 1). | ✔ D9 | — |

## 9. Mistérios e narrativa

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 9.1 | Mistérios de Marte (13: cubos negros, esferas, wisps, Dredgers, IA, guerra na Terra, praga Wildfire, Marsgate, Metatron…) | Arcos longos com escolhas | **AD** | **Estrutura** sim (arco com gatilhos e escolhas); **conteúdo** nosso, pé no chão: missão anterior (D16), Cheyava Falls (notas), a história do Caio (D11). | ✔ D11, D16 | Depois |
| 9.2 | Mistérios de asteroide (5) | — | **NT** | Sem asteroides. | — | — |
| 9.3 | 1 mistério por partida, sorteado | Replay | **NT** | Campanha com história fixa (crítica ao 687 Days: falta história). | D11 | — |
| 9.4 | Anomalias de evento | Disparam história | **AD** | **Marcos** do mapa (D15) disparam capítulos. | ✔ D15 | Cedo |
| 9.5 | Story Bits | Ver 7.14 | **AD** | Rádio. | — | Cedo |
| 9.6 | Rádio (estações de música, locutor) | Ambiente | **AD** | Rádio da base com **mensagens da Terra** (entrega narrativa barata em 1ª pessoa). | D11 | Cedo |
| 9.7 | Recompensa do mistério (maravilha/breakthrough) | Prêmio | **TP** | — | — | Depois |
| 9.8 | Escolhas morais (ex: destruir/estudar) | Dilemas | **TP** | Cheyava Falls: preservar × minerar (já nas notas). | ✔ notas | Depois |
| 9.9 | Logs/registros encontrados | (quase ausente no SM) | **CN** | Registros da missão anterior (lista §12, D16). | ✔ D16 | Cedo |
| 9.10 | Guerra/refugiados/invasão armada | Temas de conflito | **NT** | Sem combate (D9). | ⚠ D9 | — |
| 9.11 | Narrativa por pop-ups de texto | — | **CN** | Nosso meio: rádio, logs, lugares — o jogador **está lá** (D1). | D1 | Cedo |

## 10. Interface e gestão

| # | Item SM | O que é | Rec. | Como / por quê | D# | Fase |
|---|---|---|---|---|---|---|
| 10.1 | Filtros de domo (especialidade, idade, traços) | Quem entra em cada domo | **AD** | Por especialidade apenas, no terminal do domo. | D2 | Cedo |
| 10.2 | Prioridade de prédio (baixa/normal/alta) | Drones/colonos priorizam | **TP** | Prioridade de energia/manutenção (quem desliga primeiro no déficit). | D4 | Cedo |
| 10.3 | Ligar/desligar prédio, trocar turno | Controles | **TP** | — | — | MVP |
| 10.4 | Notificações (sem O₂, sem casa, desastre chegando) | Alertas no canto | **AD** | **HUD do traje** + alerta âmbar (D12); nada de pilha de pop-ups. | ✔ D12 | MVP |
| 10.5 | Overlays (energia, água, O₂, alcance de drones) | Visões especiais | **AD** | Overlays no **modo construção** (D14 já tem inclinação). | ✔ D14 | Cedo |
| 10.6 | Overview da colônia (tabelas) | Painel de gestão | **AD** | **Tablet/terminal** do traje com a visão geral (D1 — no chão, mas com informação). | ✔ D1, D9 pilar 2 | Cedo |
| 10.7 | Painel de colonos (lista individual) | Ficha de cada um | **NT** | D2. | D2 | — |
| 10.8 | Gráficos/estatísticas (produção ao longo do tempo) | Relatórios | **AD** | Gráfico simples de produção e dos medidores de terraformação. | D9 pilar 2 | Depois |
| 10.9 | Resupply UI: escolher itens, peso, custo, preview | Tela de pedido | **AD** | Terminal de comunicação: carrinho com **kg e créditos**, tempo de viagem. | ✔ notas D4 | MVP (simples) |
| 10.10 | Tipo de foguete: carga × passageiros | Não mistura | **TP** | Dois voos distintos — simples e cria decisão. | — | MVP |
| 10.11 | Tempo de viagem e janela | Horas/sols | **AD** | Sem janela orbital rigorosa (D9); tempo fixo por dificuldade. | D9 | MVP |
| 10.12 | Candidatos: tela de seleção por especialidade | — | **AD** | Ver 5.13. | — | MVP |
| 10.13 | Ferramenta de salvage (desmontar prédio e recuperar parte) | Desconstruir | **TP** | Desmontar devolve material (itens caem no chão, notas D). | ✔ notas | MVP |
| 10.14 | Copiar/colar/blueprint (mods) | QoL | **AD** | Blueprints estilo Satisfactory (pilar 2). | D4 | Depois |
| 10.15 | Encyclopedia / tutorial | Ajuda | **AD** | Tutorial na caverna do Terraço (D16) + codex no tablet. | ✔ D16 | Cedo |
| 10.16 | Mod support | Workshop | **AD** | Dados em JSON em `Data/` já facilitam (CLAUDE.md). | ✔ | Depois |
| 10.17 | Controles de tempo (pausa/velocidade) | — | **NT** | Ver 1.17. | D1 | — |

## 11. O que os jogadores elogiam e criticam — lições

### Elogios (manter o espírito)
| Elogio | Lição para nós |
|---|---|
| Visual e atmosfera de Marte "bonitos e calmos", trilha sonora/rádio | Pilar 4 + D12: luz, poeira, pôr do sol azul; rádio. |
| Satisfação de ver a colônia crescer do nada | Loop D11: foguete → domo → colonos. Primeiros 30 min têm que entregar isso. |
| Variedade de mistérios (rejogabilidade) | Nossa rejogabilidade vem da fábrica e do mundo, não de sorteio; mas **história forte** compensa. |
| Terraformação (Green Planet) como meta de longo prazo — "ver ficar verde" | ✔ pilar 1. Visual precisa ser mais dramático que no SM. |
| Drones fazendo o trabalho sozinho (automação relaxante) | Nossa automação é esteira + drone; manter a sensação "vivo sozinho". |
| Relaunched: Martian Assembly elogiado pela crítica | Endgame precisa de **objetivo novo** — nosso é terraformação + independência de produção. |

### Críticas (evitar)
| Crítica | Fonte | Lição para nós |
|---|---|---|
| **Meio/fim de jogo repetitivo**: após ~4 domos/60 colonos "bate num muro", só repetir domos e labs | Steam (discussões) | Cada fase precisa de **nova mecânica** (novo veículo, nova região, novo medidor mudando o mundo). Evitar "mais do mesmo" como progressão. |
| **Microgestão tediosa** (centenas de cliques pra mover combustível) | Steam | Automação clara (esteiras, rotas) desde cedo; nada de ordem manual repetida. |
| **Pathfinding de colonos** (não usam passagens, morrem de fome, ficam presos) | Steam, Relaunched | Colonos como números (D2) resolvem isso por construção. |
| **Drones sem ordens diretas** (só prioridade) | Steam | Jogador pode **fazer ele mesmo** e dar ordens simples aos drones. |
| Terraformação **lenta e pouco visível** | Steam (Green Planet) | Mostrar ETA e mudar o mundo em marcos claros. |
| Relaunched: **bugs antigos mantidos**, travamentos no fim do jogo, pouco novo pelo preço (42% positivo no Steam) | PCGamesN, Metacritic | Testes da simulação (`dotnet test`), performance com base grande (itens em arrays, CLAUDE.md regra 8). |
| Relaunched: lentidão com colônias grandes | Reviews | Tick fixo + simulação em dados (D5) — medir cedo com base grande. |
| Dificuldade fácil sem desafio depois de aprender | Steam | Presets de dificuldade que mudam **regras**, não só números. |
| Sátira/humor às vezes quebra imersão (cassino, Game Developer, igreja) | percepção geral | Tom semi-realista (D12). |

---

## Conflitos e alinhamentos com decisões

| D# | Alinha (✔) | Conflito (⚠) e resolução |
|---|---|---|
| D1 (no chão) | Domos, grade, foguetes funcionam em 1ª pessoa | ⚠ Câmera de cima, pausa/velocidade, overviews → tablet/terminal (10.6) |
| D2 (colonos números) | Especialidades, conforto→earthsick, nascimentos como taxa | ⚠ Traços, idades, escola, crime, fichas → não trazer ou agregar |
| D3 (terraformação híbrida) | 4 medidores do Green Planet, local (domo) + global | — |
| D4 (esteiras + drones/trens longe) | Drones, trem, shuttle | ⚠ No SM drones fazem **tudo**; aqui fazem só logística curta/manutenção |
| D5 (arquitetura) | — | ⚠ Drones como prefab "invisível" (4.6) → não |
| D8 (mapa real fixo) | Lago de Jezero ↔ lagos do SM | ⚠ Mapa/árvore/mistério sorteados → não |
| D9 (pilares) | Ameaças ambientais | ⚠ Torretas, invasão, crime → não |
| D10 (sobrevivência) | Mortes por causa, earthsick, tempestades, manutenção | — |
| D11 (loop) | Metas da missão, pesquisa, anomalias | — |
| D13 (MVP) | Micro domo, 5 fundadores, 1 medidor, rover | — |
| D14 (terraplanagem) | Flatten/Ramp/Dozer, rocha residual | — |
| D15/D16 (marcos, cavernas) | Anomalias → marcos; B&B → cavernas | ⚠ Elevador/mapa subterrâneo separado → não |
| Notas (água) | Grade de água igual | ⚠ Fonte diferente: H₂+Sabatier → gelo (proposital) |

## Itens MVP (D13) vindos do Surviving Mars

Micro domo · 1 habitat · 1 estufa · MOXIE · grade de energia/O₂ · solar + bateria · poeira + 1 tempestade prevista ·
5 fundadores (número) com Bem-estar e earthsick · 1 foguete de carga (lista com kg) + 1 de passageiros · prefab importado ·
2–3 metas de missão · 1 medidor de terraformação (Atmosfera) · rover com scanner · pesquisa com amostras (3–5 techs) ·
remover pedras · desmontar devolvendo material · alertas no HUD do traje.

---

## Fontes

- Surviving Mars Wiki (Paradox): [Resources](https://survivingmars.paradoxwikis.com/Resources) · [Colonist](https://survivingmars.paradoxwikis.com/Colonist) · [Sponsors](https://survivingmars.paradoxwikis.com/Sponsors) · [Commander profile](https://survivingmars.paradoxwikis.com/Commander_profile) · [Game rules](https://survivingmars.paradoxwikis.com/Game_rules) · [Mission goals](https://survivingmars.paradoxwikis.com/Mission_goals) · [Domes](https://survivingmars.paradoxwikis.com/Domes) · [Dome buildings](https://survivingmars.paradoxwikis.com/Dome_buildings) · [Exterior buildings](https://survivingmars.paradoxwikis.com/Exterior_buildings) · [Wonder](https://survivingmars.paradoxwikis.com/Wonder) · [RC vehicles](https://survivingmars.paradoxwikis.com/RC_vehicles) · [Drones](https://survivingmars.paradoxwikis.com/Drones) · [Spacecraft](https://survivingmars.paradoxwikis.com/Spacecraft) · [Research](https://survivingmars.paradoxwikis.com/Research) · [Anomaly](https://survivingmars.paradoxwikis.com/Anomaly) · [Mystery](https://survivingmars.paradoxwikis.com/Mystery) · [Disaster](https://survivingmars.paradoxwikis.com/Disaster) · [Terraforming](https://survivingmars.paradoxwikis.com/Terraforming) · [Food](https://survivingmars.paradoxwikis.com/Food) · [Laws](https://survivingmars.paradoxwikis.com/Laws) · [Below and Beyond](https://survivingmars.paradoxwikis.com/Below_and_Beyond) · [Space Race](https://survivingmars.paradoxwikis.com/Space_Race) · [Downloadable content](https://survivingmars.paradoxwikis.com/Downloadable_content)
- Steam: [Surviving Mars: Relaunched](https://store.steampowered.com/app/3215050/Surviving_Mars_Relaunched/) · [Prime Mission](https://store.steampowered.com/app/3889470/Surviving_Mars_Relaunched__Prime_Mission/) · [Discussão "Late game extremely boring"](https://steamcommunity.com/app/464920/discussions/0/3020122487780547895/) · [Discussão "Mid to end game is boring"](https://steamcommunity.com/app/464920/discussions/0/1696043806577604716/)
- Paradox: [Green Planet e Project Laika](https://www.paradoxinteractive.com/media/press-releases/press-release/surviving-mars-green-planet-and-project-laika-now-available) · [Relaunched em 10/11](https://www.paradoxinteractive.com/games/surviving-mars-relaunched/news/surviving-mars-relaunched-is-landing-on-november-10)
- Imprensa: [PC Gamer — Below and Beyond](https://www.pcgamer.com/surviving-mars-below-and-beyond/) · [PC Gamer — Green Planet](https://www.pcgamer.com/surviving-mars-green-planet-is-live-allowing-you-to-send-all-geese-to-mars/) · [PCGamesN — recepção do Relaunched](https://www.pcgamesn.com/surviving-mars/remastered-reception) · [Metacritic — Relaunched](https://www.metacritic.com/game/surviving-mars-relaunched/) · [But Why Tho — review Relaunched](https://butwhytho.net/2025/11/surviving-mars-relaunched-review-paradox/) · [TheGamer — terraformação](https://www.thegamer.com/surviving-mars-terraforming-strategy-guide-tips/) · [Wikipedia](https://en.wikipedia.org/wiki/Surviving_Mars)
- Observação: alguns nomes/valores de construções vêm de conhecimento geral do jogo e foram conferidos por amostragem na wiki; números exatos (custos, taxas) podem variar entre o original e o Relaunched.
