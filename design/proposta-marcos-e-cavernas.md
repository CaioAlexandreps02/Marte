# PROPOSTA — Marcos, cavernas, área jogável menor e canyon realocado

> **Status (25/09/2026): decidido (D15 + D16) e APLICADO no pipeline do terreno** — falta regenerar os tiles e reimportar no Unity no PC com o cache completo (ver `ferramentas/terreno/README.md`). Variante A + corredor do Mirante e início no pad em `mapa.json`; canyon na diagonal, `pocos`, `mesas` (Terraço +45 m, Pico Farol, Mesas Estratificadas), `nivelamentos` (base B2), `trilhas` (Mirante) e platôs do pad/cume em `edicoes.json`; lista de marcos em `ferramentas/terreno/marcos.json`. Diferenças do texto abaixo: os stamps de mesa usam a **forma da Kodiak** (CTX 20 m, real) em vez de um morro de Gale (trocar quando houver fonte); os poços têm profundidade 45–90 m reais; a trilha usa **rampa escavada** (limite 22° no jogo) em vez de zigue-zague; o mapa gerado **continua 28×25** (não 28×22). Preview: [`20_edicoes_aplicadas.png`](../referencias/terreno/20_edicoes_aplicadas.png), [`21_base_depois.png`](../referencias/terreno/21_base_depois.png), [`22_trilha_do_mirante.png`](../referencias/terreno/22_trilha_do_mirante.png).
> Mapas: [`12_proposta_marcos.png`](../referencias/terreno/12_proposta_marcos.png) (visão geral, variantes A/B),
> [`13_proposta_canyon.png`](../referencias/terreno/13_proposta_canyon.png) (zoom do canyon),
> [`14_mapa_marcos_nomes.png`](../referencias/terreno/14_mapa_marcos_nomes.png) (**Variante A com todos os nomes**),
> [`15_vista_do_mirante.png`](../referencias/terreno/15_vista_do_mirante.png) (vista 3D do cume) e
> [`16_rota_do_mirante.png`](../referencias/terreno/16_rota_do_mirante.png) (inclinação + trilha).

**Problema (Caio):** o mapa de 28×25 km (~611 km² jogáveis) parece vazio. O que incomoda é a **falta de marcos**. Ele topa diminuir o mapa e colocar mais marcos. Prioridades: (1) cavernas (gelo escondido = fonte alternativa de água), (2) mesa Kodiak, (3) cratera Belva, (4) tirar o canyon da borda norte.

Pilares atendidos (D9): **4 – Um Marte real pra explorar** (marcos reais, descobertas que valem a caminhada) e **3 – colônia** (gelo nas cavernas alimenta a água). Nada de combate.

Todas as coordenadas estão em **km no sistema de referência das edições** (x → leste, z → norte, origem no canto SW da referência: 77,23378°E / 18,36254°N; L-O corrigido por cos(lat do centro) = 0,94792, igual ao `exportar_heightmap.py`). O canto SW do mapa 28×25 atual fica em x = 3.

---

## 1. Onde ficam os lugares reais de Jezero

Fonte principal: **trajeto oficial do Perseverance** (`M20_waypoints.json`, MMGIS da NASA/JPL, até o sol 1980) e **voos do Ingenuity** (`m20_heli_waypoints.json`). Kodiak e Belva foram localizados no **DTM CTX 20 m** (mosaico Mars 2020 TRN, em `ferramentas/terreno/cache/ctx_20m.tif`) a partir das descrições da NASA.
Conferência: o pouso convertido para km e de volta dá 18,4447°N 77,4511°E, contra 18,4446°N 77,4509°E da NASA (erro ~10 m).

| Lugar | lat / lon | Mapa (x; z) km | No 28×25? | Como foi obtido / incerteza |
|---|---|---|---|---|
| **Octavia E. Butler** (pouso, sol 13) | 18,4446°N 77,4509°E | (12,21; 4,87) | sim | waypoints NASA, ±10 m |
| **Kodiak** (morro-testemunho do delta) | ~18,439°N 77,408°E | (9,80; 4,55) | sim | DTM CTX: único morro isolado a ~2,4 km a OSO do pouso (NASA: "~2,4 km", topo ~130 m de largura, ~77 m acima do fundo). ±100 m |
| **Belva** (cratera ~0,9 km no topo do delta) | ~18,484°N 77,377°E | (8,05; 7,20) | sim | rover na borda oeste nos sóis 766–797 em (7,6; 7,1); centro da cratera pelo DTM. ±100 m |
| **Three Forks** (depósito de amostras, sóis 586–653) | 18,450–18,454°N 77,399–77,408°E | (9,3–9,8; 5,2–5,4) | sim | waypoints dos sóis de largada dos tubos. ±50 m |
| **Séítah** (dunas/olivina) | ~18,430°N 77,435°E | ~(11,3; 4,0), unidade de ~(10,5–12) × (3–4,5) | sim | rover dentro/na borda nos sóis 200–340 em (11,6; 4,15). Limites da unidade aproximados |
| **Máaz** (fundo da cratera, lavas) | em volta do pouso | ~(11–14; 3–6) | sim | é a unidade do fundo onde o rover pousou; sem limite preciso |
| **Frente/escarpa do delta** | ~18,45–18,48°N 77,39–77,41°E | faixa x ≈ 8,5–9,8, z ≈ 4,8–7 | sim | DTM + sóis 420–700 (base da frente do delta). ±200 m |
| **Neretva Vallis** (rio de entrada, oeste) | leito ~18,50–18,53°N | da borda (~x 1, z 9) até o topo do delta (~x 7; z 10) | parcial (a foz na borda fica fora do 28×25, x < 3) | DTM + rover no vale (sóis 1150–1230). Ponto de quebra da borda **estimado** |
| **Bright Angel / Cheyava Falls** (sóis ~1170–1230) | 18,4975°N 77,3051°E | (4,00; 8,00) | sim, mas **fora da área jogável atual** (limite em x ≈ 4,65) | waypoints NASA, ±50 m |
| **Airfield Chi** (Ingenuity, voo 72, sol 1036) | 18,4973°N 77,3225°E | (4,99; 7,99) | sim (dentro, colado no limite) | waypoints oficiais do helicóptero |
| **Borda oeste de Jezero** (crista) | ex.: 18,4606°N 77,2648°E (sol 1400, −1820 m) | crista em x ≈ 0–2 | **fora** (fundo visual). O mapa pega só a subida (x 3–5) | waypoints |
| **Sava Vallis** (entrada norte) | não achei coordenada confiável | — | provavelmente **fora ou na borda norte** | só descrição qualitativa (entra pelo norte, leque norte). Não usar sem confirmar |

Outros achados no DTM que viram marcos: **cratera de ~1,8 km no leste** (27,3; 9,5), cuja borda fica acima da água em −2560 m (vira um **atol** depois da terraformação); **morros-ilha** no lago em (14,3–14,8; 6,3–7,1), 45–50 m acima da água.

---

## 2. Plano de marcos (26 pontos aceitos + 9 novos em §2.1)

Legenda: **visível** = dá pra ver de longe (serve de navegação). **[cav.]** = tem caverna. Variante: onde o marco cabe (A, B).

| # | Nome | Tipo | (x; z) km | lat / lon | Por que está ali (jogo) | Visível | Var. |
|---|---|---|---|---|---|---|---|
| 1 | **Mesa Kodiak** | real | (9,80; 4,55) | 18,4393°N 77,4082°E | Primeiro "quero ir lá" a 1,8 km do início; ~150 m no jogo (2×). Camadas do delta à vista (pista de história: "aqui teve um lago") | sim | AB |
| 2 | **Cratera Belva** [cav.] | real | (8,05; 7,20) | 18,4840°N 77,3771°E | Paredes com camadas expostas → **sílica/argila**; caverna pequena sob a parede norte (sombra = gelo raro) | sim | AB |
| 3 | Sítio de pouso antigo | inspirado no real | (12,21; 4,87) | 18,4447°N 77,4511°E | Rover abandonado de uma missão fictícia (sem logos da NASA), com registro de áudio/log. **Fica abaixo de −2560 m: alaga** com a terraformação → "salve antes" | não | AB |
| 4 | Depósito de amostras | inspirado no real | (9,55; 5,30) | 18,4519°N 77,4037°E | Tubos de amostra fictícios = **pesquisa** (D11: pesquisa com amostras). Missão curta do começo | não | AB |
| 5 | Dunas de Séítah | real | (11,30; 4,00) | 18,4300°N 77,4349°E | Campo de dunas (rover atola/anda devagar); **olivina → magnésio** (já previsto nas notas de recursos) | sim | AB |
| 6 | **Abrigos da escarpa do delta** [cav.] | real + jogo | (8,90; 6,10) | 18,4654°N 77,3922°E | **Caverna do tutorial**: saliências sob camadas do delta, a 2,1 km do início. Pouco gelo, ensina a mecânica | sim | AB |
| 7 | Cheyava Falls / Bright Angel | real | (4,00; 8,00) | 18,4975°N 77,3050°E | Missão de história "possível vida antiga" (preservar × minerar, já nas notas). Pede um **bolsão** no limite oeste (ver §3) | não | AB |
| 8 | Drone de reconhecimento caído | inspirado no real (Ingenuity) | (4,99; 7,99) | 18,4973°N 77,3226°E | Destroço com pá quebrada; dá o **mapa/radar** da região (recompensa de exploração) | não | AB |
| 9 | **Foz do Neretva – tubo de lava** [cav.] | real + jogo | (3,60; 8,60) | 18,5076°N 77,2979°E | Caverna na parede do vale onde o rio corta a borda. Gelo médio, perto dos marcos 7–8 | sim | AB |
| 10 | **Mirante da Sentinela** (era "Mirante da Borda Oeste") | real | **(3,82; 11,46)** (antes (5,40; 13,00), que vira o **início da trilha** em (5,22; 12,54)) | 18,5559°N 77,3018°E | **Cume** do morro da borda na foz do Neretva, −1741 m (+715 m sobre a base; +1430 m no jogo). Antena/farol de sinal (estende o alcance do traje) e plataforma de observação. Ver §6 | sim | A |
| 11 | **Pico Farol** | jogo (stamp de mesa de Gale) | (11,00; 15,80) | 18,6291°N 77,4296°E | **Marco alto de orientação** a 3,9 km da base (NNE): mesa estratificada de ~200–250 m no jogo, fora da planície suavizada. Visível de quase todo o mapa | sim | AB |
| 12 | **Fossas de Hefesto** (canyon) [cav.] | real (stamp HiRISE) | (21,20; 17,30) | 18,6544°N 77,6111°E | Canyon movido para dentro (ver §4). **Principal fonte de gelo em cavernas**, destino de expedição (D8: recursos longe da base) | sim | AB |
| 13 | Mesas Estratificadas | jogo (stamps de Gale) | (16,80; 19,40) | 18,6898°N 77,5328°E | 2–4 mesas pequenas (40–120 m) ao norte da planície; minério em camadas (ferro/enxofre) | sim | AB |
| 14 | Campo de meteoritos ferrosos | jogo | (16,50; 14,20) | 18,6021°N 77,5274°E | **Ferro-níquel** puro (como o "Heat Shield Rock" do Opportunity): atalho de metal no meio da planície de construção | não | AB |
| 15 | **Cratera-atol** [cav.] | real | (27,30; 9,50) | 18,5228°N 77,7197°E | Cratera de ~1,8 km; depois da terraformação vira anel no lago. Caverna na parede interna | sim | só A |
| 16 | Campo de blocos | jogo | (14,80; 9,20) | 18,5177°N 77,4972°E | Blocos grandes no fundo do lago (regolito/basalto fácil); vira recife raso quando alaga | não | AB |
| 17 | **Caverna de fratura das Colinas** [cav.] | real + jogo | (8,60; 16,20) | 18,6358°N 77,3868°E | Fenda nas colinas do norte, 4,3 km da base: segunda caverna de gelo, meio do jogo | sim | AB |
| 18 | Morros-ilha | real | (14,60; 6,70) | 18,4756°N 77,4936°E | Morros ~45–50 m acima da água; viram **ilhas** (bom lugar para a 1ª base "à beira-lago" pós-terraformação) | sim | AB |
| 19 | Leito seco do Neretva | real | (7,20; 9,90) | 18,5296°N 77,3619°E | Canal seco entre a borda e o delta: caminho natural para o rover; argilas | sim | AB |
| 20 | Margem de carbonatos | inspirado no real | (19,50; 12,20) | 18,5684°N 77,5808°E | **Carbonatos** (carbono para aço, já previsto nas notas). Jezero tem carbonatos marginais reais | não | AB |
| 21 | Deslizamento da borda | jogo | (6,00; 3,80) | 18,4266°N 77,3406°E | Leque de detritos/blocos descendo da borda no canto SW | sim | AB |
| 22 | **Poços de colapso** [cav.] | inspirado no real | (24,30; 13,90) | 18,5970°N 77,6663°E | Fim da cadeia de poços (tubo de lava colapsado) saindo do canyon; entradas verticais para cavernas de gelo | sim | AB |
| 23 | Estação meteorológica abandonada | jogo | (24,30; 19,60) | 18,6932°N 77,6663°E | Mastro alto (visível); libera **previsão de tempestade** (D10) | sim | AB |
| 24 | Arco de rocha das Colinas | jogo | (11,80; 20,00) | 18,6999°N 77,4438°E | Arco natural no topo das colinas (silhueta) | sim | só A |
| 25 | Cápsula de carga perdida | jogo | (22,00; 10,90) | 18,5464°N 77,6253°E | Carga da Terra que caiu fora do alvo (Surviving Mars): recompensa de peças | não | AB |
| 26 | Bloco errático gigante | jogo | (13,30; 12,60) | 18,5751°N 77,4705°E | Rocha enorme isolada na planície de construção (ponto de referência estilo Satisfactory), 4,2 km a leste da base | sim | AB |

### 2.1 Marcos novos (proposta de 25/09, depois do D15)

Mesas: primeiro procurei **morros isolados reais** no DTM CTX (relevo acima do entorno com abertura morfológica de 0,8 e 1,6 km; a busca acha a Kodiak sozinha, o que valida o método). As 5 mesas abaixo são **reais**; nenhuma precisa de stamp. Alturas = relevo acima do entorno (real; no jogo ×2). Cavernas: tipos diferentes, todas **[JOGO]** (malha + Terrain Hole, como em §5). "Vista do Mirante" = linha de visada do cume (§6).

| # | Nome | Tipo | (x; z) km | Altura / cota | Por que está ali (jogo) | Vista do Mirante |
|---|---|---|---|---|---|---|
| 27 | **Mesa Santa Cruz** | mesa real | (11,34; 7,07) | 64–73 m acima do entorno (~140 m no jogo), topo −2478 m | Morro-testemunho a 0,9 km NNE do início, 2,4 km do pouso. **Provavelmente** é a colina "Santa Cruz" fotografada pela NASA em 2021 (~2,5 km do rover) — **confirmar** antes de usar o nome real | sim, 8,7 km |
| 28 | **Mesa da Proa** | mesa real | (11,13; 8,91) | 69–75 m (~145 m no jogo), topo −2455 m | Butte na borda do fundo do lago, "proa" apontando para a água: vira promontório depois da terraformação | sim, 7,7 km |
| 29 | **Mesa Âncora** | mesa real | (10,58; 10,97) | 46–55 m (~100 m no jogo), topo −2422 m | A 1,8 km ESE da base: marco de orientação do dia a dia ("a base fica a oeste da Âncora"); topo bom para antena/painéis | sim, 6,8 km |
| 30 | **Grande Mesa do Leste** | mesa real | (25,22; 19,47) | 95–190 m (~200–380 m no jogo), 1,4–2,8 km², topo −2151 m | Maior relevo isolado da planície leste; a Estação meteorológica (23, a 0,9 km) pode subir para o topo. Silhueta visível de quase todo o leste | sim, 22,9 km |
| 31 | **Mesa-ilha do Leste** | mesa real | (26,09; 10,79) | 45–52 m (~100 m no jogo), topo −2539 m (21 m acima da água) | Vira **ilha** depois da terraformação, perto da cratera-atol (1,8 km) — dá vida ao braço leste da variante A | sim, 22,3 km |
| 32 | **Tubo de lava do canyon** [cav.] | caverna — tubo de lava | (20,90; 18,80) | parede NE do canyon, ~−2590 m | Boca de tubo de lava na parede do canyon (mesma história dos poços: tubo colapsado) → galeria longa com **gelo** | não (fica abaixo da borda) |
| 33 | **Gruta de gelo da Face Norte** [cav.] | caverna — gelo (armadilha fria) | (9,56; 20,19) | −1967 m, parede virada para o norte (> 30° no jogo) | Face voltada para o polo nunca pega sol direto → **gelo limpo** em lentes; cobre o "buraco" do canto NO (antes 4,3 km sem marco) | sim, 10,4 km |
| 34 | **Dolina dos Cristais** [cav.] | caverna — mineral (gipsita/sulfatos) | (14,30; 17,00) | −2426 m, na planície norte | Dolina de dissolução de sulfatos (carste de gipsita, como na Terra; Perseverance achou sulfatos de cálcio em Jezero) com **cristais de selenita** → **enxofre/cálcio**; poço estreito (~60 m) no meio da planície de construção | sim, 11,8 km |
| 35 | **Abrigo da Trilha** [cav.] | caverna — abrigo de fratura | (4,18; 12,76) | −1966 m, sela da trilha (1,4 km do início da trilha) | Parada no meio da subida: recarga de O₂/bateria, um pouco de gelo (face N), log de história | não (escondido pela crista) |

Espaçamento (medido na Variante A + corredor): com 27–35 e o Mirante, **99% da área jogável fica a ≤ 3 km de um marco** e 95% a ≤ 2,5 km. O pior ponto passa a ser o fundo do lago em (18,5; 8,6), a 3,7 km — alaga com a terraformação, então tudo bem. O canto NO (antes 4,3 km) fica coberto pela Gruta de gelo e a planície norte pela Dolina.

**Cobertura (medida no plano):** com os marcos acima, **97–98% da área jogável fica a ≤ 3 km de um marco** (87–90% a ≤ 2,5 km; mediana 1,5–1,6 km). Isso sem contar que os marcos altos (1, 11, 12, 13, 23) se veem de bem mais longe. O pior buraco que sobra é o canto NO da variante A, ~(7,5; 20,4), a 4,3 km — a caverna 17 e o Pico Farol estão visíveis de lá.

**Primeira hora (início em (11,0; 6,2)):** Kodiak 1,8 km, depósito de amostras 1,6 km, sítio de pouso 1,8 km, Séítah 2,2 km, caverna-tutorial 2,1 km, Belva 3,2 km. Da base (9,1; 12,05): leito do Neretva 2,9 km, Mirante 3,8 km, Pico Farol 3,9 km, bloco errático 4,2 km.

---

## 3. Nova área jogável (duas variantes)

As duas mantêm o limite oeste atual (meio da subida da borda), cortam o **fundo do lago** no sudeste e a faixa norte do canyon, e ganham um **bolsão** no vale do Neretva para incluir Cheyava Falls: (4,6; 7,0) → (3,3; 7,4) → (3,2; 8,9) → (4,7; 9,4).

| | Variante A — "Delta + Leste" | Variante B — "Compacta" |
|---|---|---|
| **Área** | **~337 km²** (7,2× Satisfactory) | **~269 km²** (5,7× Satisfactory) |
| Água em −2560 m | ~15% (~48 km², inclui a cratera-atol) | ~11% (~29 km²) |
| Plano e seco (< 5° com exagero 2×, escala 100 m) | ~103 km² (medido na parte com CTX) | ~97 km² |
| Marcos | todos os 26 | 24 (sem 15 e 24) |
| Polígono (x; z) km | (4,5; 2,8) (13,8; 2,8) (16,0; 6,8) (19,5; 9,3) (25,5; 7,8) (29,2; 7,8) (29,2; 12,0) (26,6; 13,2) (26,6; 21,0) (7,7; 21,0) (7,4; 20,0) (6,5; 17,0) (5,6; 14,0) (4,8; 11,0) (4,7; 9,4) (3,2; 8,9) (3,3; 7,4) (4,6; 7,0) (4,5; 5,0) | (4,5; 2,8) (13,2; 2,8) (15,2; 6,5) (18,5; 9,5) (26,0; 11,4) (26,0; 20,8) (15,5; 20,8) (13,5; 17,6) (6,5; 17,0) (5,6; 14,0) (4,8; 11,0) (4,7; 9,4) (3,2; 8,9) (3,3; 7,4) (4,6; 7,0) (4,5; 5,0) |
| Prós | Tem a cratera-atol e o arco; mais espaço de expansão | Mais denso (menos caminhada vazia); corta as colinas do NO, que são ruins para construir |
| Contras | Canto NO e braço da cratera-atol mais vazios | Perde a cratera-atol (fica como vista do fundo) |

O mapa gerado pode encolher junto, cortando só o norte (e o leste na B) e mantendo o canto SW: A em x 3–31 × z 0–22 (**28×22 tiles**) e B em x 3–28 × z 0–22 (**25×22 tiles**), com ≥ 1,2 km de terreno em alta resolução além do limite. Menos tiles = geração e streaming mais leves. (Mudar `tiles_x/tiles_z`, `oeste_graus/sul_graus` em `mapa.json`; a referência das edições não muda.)

---

## 4. Canyon: sair da borda norte

**Hoje:** stamp das Hephaestus Fossae de (13,0; 23,6) a (23,0; 23,6), 10 km (5,9 km reais esticados), 2,6 km de largura, só visual, com o limite contornando a beirada sul.

**Proposta (vale para A e B): diagonal NO→SE atravessando a planície leste**, fora da planície suavizada:

- **Eixo:** de **(19,0; 19,6)** a **(23,4; 15,0)** → **6,4 km**, quase o comprimento real (5,9 km), então **quase sem esticar** (fica mais natural que os 10 km atuais).
- **Cadeia de poços de colapso** saindo da ponta SE em direção ao lago: (23,8; 14,6) r 200 m · (24,2; 14,1) r 280 m · (24,6; 13,6) r 220 m · (24,9; 13,2) r 150 m. História: **tubo de lava colapsado** (as Hephaestus Fossae reais são cadeias de poços/fossas, uma das explicações é colapso sobre tubos/diques) → as **cavernas de gelo** ficam nos poços e nas paredes do canyon.
- **Por quê ali:** (1) quebra a parte mais lisa e sem graça do mapa (planície CTX do leste); (2) fica a ~13 km da base = expedição de meio de jogo (D8: alguns recursos bem longe); (3) é **jogável** (dá para descer por rampas nas pontas afinadas e entrar nas cavernas), não mais só visual; (4) não encosta em nenhum limite — a ponta NO fica a ~1,2 km da borda norte e o último poço a ~1,1 km da borda leste da variante B (o corpo do canyon fica a 2–3 km dos limites); (5) não entra na planície suavizada (só encosta no canto leste dela perto de (20,5; 16) — se precisar, afastar o eixo 300 m para leste).
- **Alternativa descartada:** colocar entre a base e as colinas do norte (~(8; 15) → (12; 18,5)): mais perto da base, mas bate com o Pico Farol e com a caverna 17 e fica perto do limite oeste de novo.

**O que o `edicoes.json` precisaria (✅ aplicado em 25/09):**
1. `canyons[0].de_km` → `[19.0, 19.6]`, `ate_km` → `[23.4, 15.0]`; manter `largura_km` 2,6 (ou 2,0 para um vale mais estreito), `profundidade_m` 150, `afinar_pontas_km` 1,5. O script já gira o stamp pelo eixo `de → ate`.
2. Tirar o `_comentario` "só visual" e o recorte do limite norte em `mapa.json` (o polígono novo não contorna mais o canyon).
3. **Tipo novo de edição `pocos`** (não existe no script): lista de `{x_km, z_km, raio_m, profundidade_m, borda_irregular}` — cavar um poço de paredes íngremes (perfil em sino/cilíndrico com borda de colapso). Alternativa sem código novo: cortar 2–3 pedaços curtos do próprio stamp do canyon (cada um um item em `canyons`, 0,5–0,8 km de comprimento) enfileirados.
4. Se quiser segmentos curvos: vários itens em `canyons` com eixos encadeados (ex.: 3 segmentos de ~2 km com 10–15° de diferença), afinando nas junções.
5. Os stamps de mesa (11, 13) também são tipo novo (`mesas`: DTM HiRISE de Gale/Aeolis, posição, rotação, escala, altura) — mesma mecânica do canyon, mas somando relevo em vez de cavar.

---

## 5. Cavernas

| Caverna | Onde | Tipo (justificativa) | Gelo | Fase |
|---|---|---|---|---|
| C1 – Abrigos da escarpa (6) | (8,90; 6,10) | Saliência sob camadas do delta (erosão diferencial de camadas duras sobre moles) | pouco | tutorial / 1ª hora |
| C2 – Belva (2) | (8,05; 7,20) | Reentrância na parede norte (sempre na sombra) | pouco | começo |
| C3 – Foz do Neretva (9) | (3,60; 8,60) | Tubo de lava / fratura na parede da borda [JOGO] | médio | começo–meio |
| C4 – Colinas (17) | (8,60; 16,20) | Fenda de fratura com teto de blocos | médio | meio |
| C5 – Fossas de Hefesto (12) + poços (22) | (19–25; 13–20) | Cadeia de poços = tubo de lava colapsado (justificativa real das fossas) | **muito** (principal) | meio–fim |
| C6 – Cratera-atol (15) | (27,30; 9,50) | Parede interna da cratera | médio | só na variante A |
| C7 – Tubo de lava do canyon (32) | (20,90; 18,80) | **Tubo de lava** aberto na parede NE do canyon (galeria longa) | muito | meio–fim |
| C8 – Gruta de gelo da Face Norte (33) | (9,56; 20,19) | **Caverna de gelo**: armadilha fria em face voltada para o norte (nunca pega sol direto) | muito (gelo limpo) | meio |
| C9 – Dolina dos Cristais (34) | (14,30; 17,00) | **Mineral**: dolina de dissolução de sulfatos, cristais de gipsita/selenita → enxofre, cálcio | nenhum | meio |
| C10 – Abrigo da Trilha (35) | (4,18; 12,76) | **Abrigo de fratura** na sela da trilha do Mirante (parada de recarga) | pouco | qualquer (exploração) |

Gelo em caverna é licença de jogo ([JOGO], já aceito nas notas de recursos).

### Nota técnica (Unity)
- Heightmap não faz teto nem saliência: **caverna = malha**. Cada caverna = (a) **malha de entrada** encaixada na encosta (rocha com a boca) e (b) **interior** como prefab de malhas modulares (túnel, salão, poço) ou **cena aditiva** carregada quando o jogador chega perto (combina com o streaming de tiles).
- Na boca, abrir buraco no terreno com **Terrain Holes** (`TerrainData.SetHoles`, resolução = heightmap − 1; no URP o material de terreno precisa de "Terrain Holes" ativado nas configurações do URP). Criar o buraco por **editor script** (menu `Marte/...`), nunca à mão, e reaplicar a cada importação dos tiles (os buracos ficam num JSON como as outras edições).
- Colisão: o buraco no terreno também tira a colisão, então a malha da caverna precisa de collider próprio.
- Para os poços (C5), o heightmap faz o buraco raso; a parte vertical e a galeria lateral são malha.
- Simulação (D5): a caverna é só geometria; o **nó de gelo** dentro é uma entidade com ID como os outros recursos.

---

## 6. Mirante da borda (rota e vista)

Pedido (D15): subir **um** trecho da borda oeste, pelo lado **menos íngreme**, e ver o mapa lá de cima. Imagens: [`16_rota_do_mirante.png`](../referencias/terreno/16_rota_do_mirante.png) (inclinação + perfil) e [`15_vista_do_mirante.png`](../referencias/terreno/15_vista_do_mirante.png) (vista 3D do cume).

**Método:** DTM CTX 20 m, inclinação medida **com o exagero 2× do jogo**. Rota de menor custo (Dijkstra em grade de 40 m, 16 direções, custo cresce com a rampa **ao longo do caminho**, penaliza forte acima de 22°/27°/33°), saindo de qualquer ponto da Variante A até cada cume candidato. Depois a rota foi reamostrada a cada 10 m no DTM original para achar os degraus curtos.

**Candidatos:**

| Cume | Onde | Cota | Trilha | Rampa (40 m) | Veredito |
|---|---|---|---|---|---|
| **Morro da Sentinela** (norte) | (3,82; 11,46) | −1741 m | 3,26 km, +331 m reais | média 11°, máx 19° | ✅ **escolhido**: dentro do mapa gerado (x ≥ 3), 5,3 km da base, em cima da foz do Neretva |
| Maciço sul | (1,62; 3,57) | −1650 m | 4,47 km, +528 m reais | média 13°, máx 19° | ❌ mais alto, mas fica em x < 3: exigiria crescer o mapa 2–3 km para oeste |

**Rota escolhida (Trilha do Mirante):** sobe pelo **lado norte** do morro — contorna a ponta norte e segue a **crista (espinhaço) norte** até o cume; a face leste (a que se vê da base) é > 30° e fica de fora.

- Polilinha (x; z) km, simplificada a 30 m: **(5,22; 12,54)** início da trilha, −2073 m → (4,86; 12,22) → (4,14; 12,78) **Abrigo da Trilha / sela** → (3,90; 12,66) → (3,98; 12,58) → (3,86; 12,54) → (3,82; 12,42) → (3,90; 12,38) → (3,70; 12,02) → (3,78; 11,86) → (3,86; 11,82) → **(3,82; 11,46) cume**.
- **Cume:** −1741 m real = **+715 m sobre o platô da base** (−2456,5 m) = **+1430 m no jogo**; +331 m (662 m no jogo) sobre o início da trilha, que já fica no meio da subida (o limite atual passa ali).
- **Inclinação ao longo da trilha (jogo, amostra a cada 10 m):** 37% < 10°, 32% 10–15°, 22% 15–20°, 5% 20–25°, **3% > 25°** (mediana 12,5°, p90 19°). Em escala de 40 m, 100% < 20°.
- **Trechos que pedem mão (trilha feita/zigue-zague):** (a) **(3,73; 12,09)**, ~60 m com degraus até **33°** — degrau da crista logo abaixo do cume: 2–3 zigue-zagues ou uma rampa escavada; (b) (5,22; 12,54), 20 m até 26° na saída; (c) (3,94; 12,62), 10 m até 26°. Os três somam ~90 m em 3,26 km.
- **Atenção:** a crista é estreita — a inclinação **do terreno** dos lados passa de 30° (mediana 26° sob a trilha). A trilha precisa de um **leito aplainado de ~6–8 m** (edição tipo "estrada" ou vários platôs pequenos) para o jogador não escorregar de lado. O DTM é 20 m; no HiRISE 1 m a crista vai ter mais pedra/degrau → conferir no jogo.
- **Topo:** crista N-S estreita; propor **platô de ~60 m de raio** (tipo `platos` do `edicoes.json`, altura −1745 m) para a plataforma do mirante (antena/farol).

**Área jogável:** não precisa liberar a borda inteira — só um **corredor de 300 m** (150 m de cada lado da trilha) + **círculo de 300 m** no cume = **+1,1 km²** (Variante A 336,7 → **337,8 km²**). Emenda no polígono da Variante A entre (5,6; 14,0) e (4,8; 11,0), nesta ordem:
(5,23; 12,68) (5,15; 12,68) (4,85; 12,40) (4,61; 12,64) (4,47; 12,70) (4,29; 12,88) (4,21; 12,92) (4,07; 12,92) (3,82; 12,79) (3,68; 12,53) (3,70; 12,31) (3,56; 12,09) (3,56; 11,95) (3,68; 11,73) (3,54; 11,59) (3,52; 11,39) (3,58; 11,27) (3,75; 11,16) (3,95; 11,18) (4,06; 11,27) (4,12; 11,39) (4,10; 11,59) (4,00; 11,71) (4,00; 11,87) (3,88; 11,99) (3,88; 12,03) (4,04; 12,31) (4,04; 12,45) (4,10; 12,49) (4,13; 12,60) (4,31; 12,44) (4,45; 12,38) (4,71; 12,12) (4,79; 12,08) (4,93; 12,08) (5,12; 12,21).
Obs.: o aviso "SINAL DA BASE FRACO" (1,2 km da borda) dispararia na trilha inteira — no corredor, usar a distância até a **antena do mirante** (ou desligar o aviso no corredor). A barreira invisível a 300 m da borda também precisa respeitar o corredor estreito (fazer a barreira no próprio limite do corredor).

**O que se vê do cume** (linha de visada no DTM com exagero 2×, olho a 2 m do chão, alvo 6 m acima do chão, sem curvatura como no Unity; canyon, poços e mesas de stamp aproximados; leste de x ≈ 26 e norte de z ≈ 21 sem DTM em cache, suavizado):

| Visível | Marcos (distância do cume) |
|---|---|
| **sim (24)** | Leito do Neretva 3,7 · Caverna das Colinas 6,7 · Mesa Âncora 6,8 · Abrigos da escarpa 7,4 · Mesa da Proa 7,7 · Pico Farol 8,4 · Mesa Santa Cruz 8,7 · Mesa Kodiak 9,1 · Bloco errático 9,6 · Gruta de gelo 10,4 · Séítah 10,6 · Pouso antigo 10,7 · Campo de blocos 11,2 · Morros-ilha 11,8 · Dolina dos Cristais 11,8 · Meteoritos 13,0 · Carbonatos 15,7 · Cápsula 18,2 · Estação meteorológica 22,0 · Mesa-ilha do Leste 22,3 · Grande Mesa do Leste 22,9 · Cratera-atol 23,6 · **BASE 5,3** · Início 8,9 |
| parcial | Poços de colapso 20,6 (bordas) |
| não | Abrigo da Trilha 1,4 · Tubo da Foz do Neretva 2,9 · Cheyava Falls 3,5 · Drone caído 3,7 · Belva 6,0 · Deslizamento 8,0 · Depósito de amostras 8,4 · Arco de rocha 11,7 · Mesas Estratificadas 15,2 · Fossas de Hefesto 18,3 e Tubo de lava do canyon 18,6 (fundo do canyon; a **borda** aparece) |

O que fica escondido é quase todo para o **sul** (a própria crista tapa o vale do Neretva e o Belva) ou dentro do canyon. Para a vista pegar também o sul, dá para pôr uma segunda plataforma no ombro sul do cume (~(3,75; 11,2)); não medi. Com névoa de poeira (D12) os marcos a mais de ~15 km viram silhueta — bom para dar "vontade de ir".

## 7. Próximos passos
1. ~~Escolher A ou B~~ → **A** (D15). ~~Confirmar os marcos 27–35 e o Mirante da Sentinela~~ → entraram no `marcos.json`.
2. ~~Atualizar `mapa.json` e `edicoes.json`~~ ✅ (25/09). **Regenerar** os tiles no PC com o cache e reimportar no Unity.
3. ~~Implementar `pocos` e `mesas`~~ ✅ (25/09, mais `nivelamentos` e `trilhas`).
4. Primeiro protótipo de caverna: **Abrigo do Terraço (#37)**, a nova caverna-tutorial, com Terrain Hole + prefab de entrada.
5. Trilha do Mirante: ~~corredor, platô do cume, leito aplainado~~ ✅; falta tratar o aviso de sinal e conferir a trilha no HiRISE dentro do jogo.
6. ~~Base no centro (§8)~~ ✅ B2 (D16).

---

## 8. Base no centro (proposta, 25/09/2026)

Pedido do Caio sobre o mapa 14: (1) base **mais para o meio** da Variante A + corredor; (2) área da base **grande e mais plana que o resto** (pouca ondulação, depois muitas pedras espalhadas no Unity); (3) **uma mesa perto da base**.
Imagens: [`17_base_candidatos.png`](../referencias/terreno/17_base_candidatos.png) (3 candidatos), [`18_base_recomendada.png`](../referencias/terreno/18_base_recomendada.png) (zoom, perfil e inclinação antes/depois) e [`19_vista_da_base.png`](../referencias/terreno/19_vista_da_base.png) (vista 3D do pad de pouso olhando para a mesa, **já com o reforço de +45 m**).

**Método:** DTM CTX 20 m + a suavização atual `planicie_norte_do_lago`; varredura em grade de 200–250 m pelo meio da Variante A (centróide em (15,42; 12,73)). Descartei centros onde a zona (com transição) sai da área jogável, fica a < 0,5 km da borda do canyon, engole um marco ou uma mesa real, ou fica abaixo de −2540 m (20 m de margem sobre a água). Inclinação medida **com o exagero 2× do jogo** (escala ~40 m). O aplainamento foi simulado com as mesmas fórmulas do `exportar_heightmap.py`.

**Por que um tipo novo de edição:** com os tipos atuais o resultado não fica plano o bastante. A `suavizacao` (escala 300–1000 m, manter 0,1) só tira ~35% da ondulação: ela preserva as ondas de 1–2 km e a transição fica dentro do polígono. Um `plato` horizontal de 0,8 km de raio precisa cortar e aterrar 20–26 m, porque o terreno tem inclinação natural de ~1,3°, e o anel de transição fica com p90 de 10–12° no jogo (fallback abaixo). Por isso proponho o tipo **`nivelamentos`**: ajusta um **plano** ao polígono, mantém **metade da inclinação natural** (`inclinacao: 0.5`) e **12% da ondulação** (`manter: 0.12`), com transição de **400 m para fora** do polígono.

### 8.1 Candidatos (tudo real, alturas sem exagero)

| | **B1 Planície Central** | **B2 Terraço do Lago ★** | **B3 Margem Leste** |
|---|---|---|---|
| Centro (x; z) km | (14,60; 15,80) | **(14,40; 13,55)** | (18,80; 12,70) |
| Distância ao centro da Var. A | 3,2 km | **1,3 km** | 3,4 km |
| Caráter | planície lisa ao pé das colinas do norte | terraço sobre a escarpa do lago, entre o Bloco errático e os Meteoritos | beira do lago, ao lado dos Carbonatos |
| Zona plana (polígono) / área afetada com transição | 4,2 / 7,6 km² | **4,1 / 7,6 km²** | 3,9 / 7,2 km² |
| Altura no centro | −2456 m | **−2485 m** | −2527 m |
| Acima da água (−2560): centro / ponto mais baixo da zona | 104 / 89 m | **75 / 64 m** | 33 / 24 m |
| Corte + aterro | 23 + 23 Mm³ | **22 + 27 Mm³** | 21 + 18 Mm³ |
| Maior corte / maior aterro | 28 / 20 m | **22 / 20 m** | 19 / 18 m |
| Inclinação mediana (jogo) antes → depois | 4,2° → 1,5° | **4,6° → 0,9°** | 3,9° → 1,0° |
| Chão < 5° (jogo) antes → depois | 64% → 100% | **55% → 100%** | 63% → 100% |
| Ondulação (desvio do plano) antes → depois | 6,2 → 0,8 m | **9,3 → 1,1 m** | 6,5 → 0,8 m |
| Mesa real mais próxima (dist. / altura sobre a base) | morro NO (12,99; 16,57): 1,8 km / +55 m (fica no pé das colinas, não parece isolada); Mesa Vigia (16,08; 14,95): 1,7 km / só +14 m | **Mesa do Terraço (13,05; 13,17): 1,4 km / +35 m** — maior morro isolado real do meio (1,1 km², 54 m de relevo do lado do lago) | morro (17,52; 13,95): 1,8 km / +50 m |
| Marcos perto | Dolina 1,2 · Meteoritos 2,5 · Pico Farol 3,6 | **Bloco errático 1,5 · Meteoritos 2,2 · Dolina 3,5 · Pico Farol 4,1 · Mesa Âncora 4,6** | Carbonatos 0,9 · Meteoritos 2,8 · canyon 3,6 · poços 5,6 |
| Início atual (11,0; 6,2) / caverna-tutorial atual | 10,2 / 11,3 km | **8,1 / 9,3 km** | 10,2 / 11,9 km |
| Início da trilha do Mirante | 9,9 km | **9,2 km** | 13,6 km |
| Fallback só com `platos` (r 700 + transição 500) | corte 13 + aterro 14 Mm³, anel p90 10°, 68% < 5° | corte 12 + aterro 20 Mm³, anel p90 10°, 75% < 5° | corte 8 + aterro 12 Mm³, **chão até −2553 m (7 m de margem)** |

Todos ficam dentro da `planicie_norte_do_lago` (a suavização existente continua valendo em volta).

### 8.2 Recomendação: **B2 Terraço do Lago**

- **É o mais central** (1,3 km do centróide). Fica no alto do terraço, **75 m acima da água**, e a escarpa do lago está 0,8 km ao sul (a escarpa **não é tocada**). Depois da terraformação a base fica **à beira do lago, no alto**: o jogador vê o lago encher da porta de casa (pilar 1).
- **Tem a mesa mais forte do meio**, 1,4 km a oeste, e o Bloco errático e a nova caverna-tutorial logo ao pé dela, a 1,3–1,5 km do pad.
- **Era o terreno mais ondulado dos três** (55% < 5°), então é o que mais ganha com o nivelamento: fica **100% < 5°** no jogo, com inclinação de 0,8° (quase imperceptível) e ~1 m de ondulação. É exatamente o "mais plano que o resto" (o entorno fica com ~50% < 5°).
- Alternativa se o Caio quiser ainda mais folga de altura e um chão naturalmente mais liso: **B1**. O ponto fraco dela é a mesa: a Mesa Vigia fica só 14 m acima da base.

**Zona aplainada (B2):**
- Polígono (x; z) km: (15,94; 13,55) (15,87; 14,08) (15,50; 14,48) (15,05; 14,68) (14,62; 14,77) (14,18; 14,79) (13,73; 14,71) (13,33; 14,45) (13,07; 14,04) (13,64; 13,55) (13,74; 13,31) (13,73; 12,98) (13,97; 12,81) (14,27; 12,80) (14,53; 12,80) (14,77; 12,91) (15,07; 12,98) (15,73; 13,06). A reentrância a oeste contorna a mesa, e o lado sul fica ≥ 0,45 km da beirada da escarpa.
- **4,1 km²** planos + transição de 400 m = **7,6 km²** afetados (a base antiga tinha 0,28 km²).
- Plano: −2487,2 m no centróide (14,49; 13,71), caindo 0,41° real (0,8° no jogo) para nordeste. Mantém 12% da ondulação.
- Corte **22 Mm³** + aterro **27 Mm³**. Maior mudança: **−22 m / +20 m** (real). A mediana é 6 m e o p95 é 18 m. O corte maior está na crista baixa que ligava a mesa ao morrote de 40 m em (15,13; 13,65), e esse morrote é aplainado.
- **Não alaga:** o chão final nunca fica abaixo de −2496 m, ou seja, **64 m acima da água** (127 m no jogo).
- Mesa intacta: mudança < 0,3 m num raio de 300 m em volta do topo. Atenção: fica um **barranco de ~20 m** entre a zona plana e o pé da mesa, porque a crista foi cortada. É bom para pedras/tálus, ou dá para virar rampa.

**Zonas de pedras** (passo do Unity, só definidas aqui; ver mapa 18):
- **Pad de pouso:** raio 250 m em volta do início novo, só cascalho, para a primeira construção sair limpa.
- **Campo de pedras normal:** o resto do polígono, com muitas pedras pequenas e médias.
- **Pedras densas:** o anel de transição (400 m) e um halo de 0,3–0,75 km no pé da Mesa do Terraço (tálus que caiu da mesa).

### 8.3 Mesa perto da base

A Mesa do Terraço **existe** (real), mas vista do pad ela sobe só +35 m reais (+70 m no jogo) e quase some na vista 3D: a crista a sudoeste esconde o pé dela. Proposta: **reforçar a mesa real**, sem mover nada. No tipo novo `mesas` (§4, item 5), somar **+45 m reais** com topo plano de ~220 m de raio e base de ~480 m. O ideal é usar a forma do stamp da Kodiak (DTM CTX, já localizado em (9,80; 4,55)) ou um morro estratificado de Gale. Com isso o topo fica **+80 m sobre a base (+160 m no jogo)**, perto da Kodiak (~150 m). A vista 19 já mostra a mesa reforçada. Efeito colateral: ela passa a tapar o Mirante visto do pad (está atrás dela, a 10,8 km), o que é aceitável porque o Mirante aparece ao sair do pad.

Nome sugerido: **Mesa do Terraço** (marco novo #36, tipo mesa, real + reforço de jogo).

### 8.4 Ponto de início

**Mover o início para a base: (14,25; 13,50)**, no pad de pouso, 150 m a oeste do centro, com a câmera olhando para a mesa.
- O início atual (11,0; 6,2) fica a **8,1 km** da base nova. Uma caminhada dessas logo na primeira hora cansa, e o D8 diz que a base é o foco do jogo. É melhor o módulo pousar onde a colônia vai crescer.
- **Primeira hora a partir do pad:** Mesa do Terraço 1,2 km · Bloco errático 1,3 · **caverna-tutorial nova 1,5** · Meteoritos ferrosos (ferro) 2,2 · Dolina dos Cristais 3,5 · Pico Farol 4,1 · Mesa Âncora 4,6. Todos os primeiros "quero ir lá" ficam a ≤ 2,2 km, e os mais altos (Pico Farol, Mirante, colinas) aparecem no horizonte.
- **Caverna-tutorial nova:** **Abrigo do Terraço** (marco novo #37), saliência na **face sul** da Mesa do Terraço em **(12,90; 12,80)**. É face ao sol, então tem pouco gelo, como o tutorial pede. Os **Abrigos da escarpa do delta (#6)** continuam existindo, mas deixam de ser o tutorial.
- O grupo do sul (pouso antigo, Kodiak, depósito de amostras, Séítah, Abrigos da escarpa, a 8–10 km) vira a **primeira expedição de rover**, atravessando o fundo seco do lago. A história do "rover abandonado / salve antes que alague" fica mais forte assim. A trilha do Mirante fica a 9,2 km.
- A base antiga em (9,1; 12,05) pode sair ou virar um **posto avançado** a caminho do Mirante (fica a 4 km do início da trilha). Isso fica para o Caio decidir.

### 8.5 Mudanças necessárias (✅ aplicadas em 25/09 — ver status no topo)

**`mapa.json`:**
```json
"inicio_alvo_km": [14.25, 13.5]
```

**`edicoes.json`** (ordem de aplicação: `suavizacoes` → `nivelamentos` → `platos` → `mesas`):
```json
"nivelamentos": [
  {
    "nome": "base_central",
    "_comentario": "Terraço do Lago (Caio 25/09): plano ajustado ao poligono, metade da inclinacao natural, 12% da ondulacao; transicao para FORA do poligono. Chao final >= -2496 m (64 m acima da agua).",
    "poligono_km": [[15.94,13.55],[15.87,14.08],[15.5,14.48],[15.05,14.68],[14.62,14.77],[14.18,14.79],[13.73,14.71],[13.33,14.45],[13.07,14.04],[13.64,13.55],[13.74,13.31],[13.73,12.98],[13.97,12.81],[14.27,12.8],[14.53,12.8],[14.77,12.91],[15.07,12.98],[15.73,13.06]],
    "manter": 0.12,
    "inclinacao": 0.5,
    "transicao_m": 400
  }
],
"platos": [
  { "nome": "pad_de_pouso", "x_m": 14250, "z_m": 13500, "raio_m": 250, "transicao_m": 100,
    "altura_m": -2485.0, "detalhe": 0.05, "irregularidade": 0.2, "semente": 11 }
],
"mesas": [
  { "nome": "mesa_do_terraco", "x_km": 13.05, "z_km": 13.17, "somar_m": 45,
    "topo_raio_m": 220, "base_raio_m": 480, "forma": "stamp Kodiak (CTX) ou morro de Gale", "rotacao_graus": 0 }
]
```
- `base_inicial` (9100; 12050): remover ou renomear para `posto_oeste`.
- `pad_de_pouso` usa a altura do plano naquele ponto (−2485,0 m). Serve só para a primeira construção ficar perfeitamente horizontal (o plano tem 0,8° no jogo).
- **Código novo em `exportar_heightmap.py`** (~20 linhas, função `aplicar_nivelamentos`, no mesmo molde de `aplicar_suavizacoes`): dentro da janela do polígono, (1) mínimos quadrados de um plano `z = a·x + b·z + c` sobre as amostras dentro do polígono (dá para fazer numa grade 8× mais grossa); (2) `a, b *= inclinacao`; (3) `alvo = plano + manter·(z − plano)`; (4) peso `w` = smoothstep de 1 (dentro) a 0 a `transicao_m` **fora** do polígono (`distance_transform_edt(~dentro)`); (5) `z = z·(1−w) + alvo·w`. É determinístico e não depende da resolução. O tipo `mesas` é o mesmo já pendente em §4, item 5.
- **Marcos:** #36 Mesa do Terraço (13,05; 13,17), #37 Abrigo do Terraço [cav.] (12,90; 12,80). O #6 perde o papel de tutorial.

Scripts (não versionados, scratchpad da sessão de 25/09, pasta `marcos/`): `flat.py` (simulação das edições), `basefinal.py` (candidatos, estatísticas, visada), `render17.py`, `render18.py`, `vista19.py`.

---

## Fontes
- NASA/JPL MMGIS — trajeto do Perseverance (`https://mars.nasa.gov/mmgis-maps/M20/Layers/json/M20_waypoints.json`, até o sol 1980) e voos do Ingenuity (`.../m20_heli_waypoints.json`).
- NASA/JPL, [PIA24814 – Jezero Crater's Kodiak and Scarps](https://www.jpl.nasa.gov/images/pia24814-jezero-craters-kodiak-and-scarps/); Mangold et al. 2021, [Science 374, eabl4051](https://www.science.org/doi/10.1126/science.abl4051); Caravaca et al. 2024, [JGR Planets – Kodiak butte](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JE008205).
- NASA/JPL, [PIA25889 – Perseverance Takes in View at Belva Crater](https://www.jpl.nasa.gov/images/pia25889-perseverance-takes-in-view-at-belva-crater/) (Belva ~0,9 km).
- NASA/JPL, [PIA25682 – Three Forks Sample Depot Map](https://www.jpl.nasa.gov/images/pia25682-perseverances-three-forks-sample-depot-map/).
- NASA/JPL, [Perseverance's Selfie With Cheyava Falls (PIA26344)](https://www.jpl.nasa.gov/images/pia26344-perseverances-selfie-with-cheyava-falls/); [Wikipedia – Cheyava Falls](https://en.wikipedia.org/wiki/Cheyava_Falls).
- Jodhpurkar et al. 2024, [Northern fan deposits (Sava Vallis)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2024JE008308); USGS SIM 3464, [Geologic Map of Jezero Crater and Nili Planum](https://pubs.usgs.gov/sim/3464/sim3464_pamphlet.pdf).
- Relevo: DTM CTX 20 m do mosaico Mars 2020 TRN (Fergason et al. 2020, USGS, CC0) em cache; faixa norte/leste sem CTX em cache desenhada a partir de `saida/preview.png`.
- Scripts da análise e dos mapas: scratchpad da sessão de 25/09 (`marcos/plan.py`, `render.py`; mirante e marcos novos: `route.py`, `buttes.py`, `mirante.py`, `mapa14.py`, `vista15.py`, `rota16.py`) — não versionados.
