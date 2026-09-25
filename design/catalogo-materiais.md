# Catálogo de materiais de Marte — lado da "oferta"

> Feito em 25/09/2026. Catálogo **completo e sem filtro** de tudo que um jogo de colônia + automação em Marte poderia usar como matéria-prima. O Caio vai cruzar depois com a lista de máquinas/prédios/itens que ele quer. **Nada aqui é decisão** — decisões ficam em [DECISOES.md](../DECISOES.md).
>
> Base anterior: [referencias/recursos-marte-pesquisa.md](../referencias/recursos-marte-pesquisa.md) (processos ISRU, energia, terraformação, MVP). Este documento **estende** aquela pesquisa; não repete processos já descritos lá.
> Marcos citados: [ferramentas/terreno/marcos.json](../ferramentas/terreno/marcos.json) (coordenadas em km no sistema de referência).

## Legenda

| Campo | Valores |
|---|---|
| **Evid.** (evidência) | **RM** = REAL medido (rover/órbita/meteorito, fonte citada) · **RP** = REAL provável (medido em outro lugar de Marte ou inferido com boa base) · **T** = TEÓRICO (proposto em artigo, não observado) · **J** = JOGO-licença (invenção/exagero nosso) |
| **Extr.** (extração/energia) | **B** baixa · **M** média · **A** alta · **MA** muito alta |
| **NOVO** | ✱ = não estava na pesquisa anterior (ou estava só de passagem e agora tem dado novo) |
| **Jezero?** | ✔ medido em Jezero · ≈ plausível em Jezero · ✘ não há em Jezero (só fora do mapa) |

---

## Resumo

| Categoria | Qtd | Novos (✱) | Exemplos |
|---|---|---|---|
| **Comum** (onipresente) | 9 | 5 | solo, poeira magnética, basalto, plagioclásio, magnetita |
| **Regional** (zonas de Jezero) | 25 | 17 | olivina, caulinita, opala, jarosita, halita, cromita, ilmenita, zircão |
| **Raro** (veios, enriquecimentos) | 16 | 16 | Ni-Cu até 8%, Mn até 25%, Zn/Ge, B, Li, F, Br, enxofre nativo, terras-raras, Th/U |
| **Meteorítico** | 8 | 7 | ferro-níquel (Phippsaksla em Jezero!), schreibersita, platinoides, palasito |
| **Atmosférico** | 13 | 7 | CO₂, N₂, Ar, Ne, Kr, Xe, NO, metano, deutério, gelo de CO₂ |
| **Espacial / fim de jogo** | 6 | 6 | regolito de Fobos/Deimos, asteroide metálico, gelo polar, cometa |
| **Importado da Terra** | 9 | — | H₂ inicial, chips, catalisadores, sementes, combustível nuclear |
| **Total de matérias-primas** | **86** | **58** | |
| Produtos refinados/intermediários (seção 8) | 62 | | aço inox, vidro borossilicato, baterias Na-íon, ímãs de ferrita, PFC… |

**Três descobertas que mudam a pesquisa anterior:**
1. **Flúor existe em Marte** (fluorita e fluorapatita, Curiosity 2015). A pesquisa anterior dizia "fluorita não confirmada" → a cadeia de **gases super-estufa (PFC)** pode ser local (com licença de escala).
2. **Meteorito ferro-níquel em Jezero** (Phippsaksla, 80 cm, borda da cratera, set/2025). O marco `meteoritos_ferrosos` (inventado) ganhou base real.
3. **Níquel e cobre em teor de minério em Jezero** (até ~8% Ni em rochas brancas ricas em Al, SuperCam 2024). Níquel/cobre deixam de ser "só da Terra".

---

## 1. Comuns (onipresentes — "o ferro do Satisfactory")

| # | Material (jogo / científico) | Evid. | Onde · Jezero? · marco | Vira → usos | Extr. | Gameplay |
|---|---|---|---|---|---|---|
| 1 | **Solo Marciano** / regolito basáltico | RM | Todo o planeta · ✔ · mapa inteiro | Marscrete, tijolo sinterizado, blindagem, água de fundo (3–5%), mistura para eletrólise de fundido (Fe, Si, Al, O₂) | B | Recurso "infinito" do começo; fonte de tudo em baixa pureza |
| 2 | ✱ **Poeira Fina** / poeira atmosférica (com magnetita/titanomagnetita) | RM | Global, homogênea (tempestades misturam) · ✔ · cai sobre tudo | Separação magnética → concentrado de Fe-Ti; pó para impressão 3D/sinterização | B | É ameaça (painéis, filtros) **e** recurso: "aspirador de poeira" que limpa painéis e gera pó de ferro. Ótimo loop |
| 3 | ✱ **Areia de Duna** / areia basáltica (olivina + piroxênio) | RM | Campos de dunas globais · ✔ · `dunas_seitah` (11,3; 4,0) | Peneiramento → olivina, piroxênio, minerais pesados; vidro escuro; fibra de basalto | B | Material fácil de pegar, mas atola rover (já é marco) |
| 4 | **Basalto** (rocha) | RM | Crosta inteira · ✔ Máaz · `campo_de_blocos` (14,8; 9,2), `mesa_terraco` | Fibra de basalto, brita, rocha fundida (lajes), lã de rocha (isolante) | B–M | Construção pesada; candidato a nome do "regolito" (D, notas) |
| 5 | ✱ **Piroxênio** (augita, pigeonita, ortopiroxênio) | RM | Máaz e borda · ✔ | Fe, Mg, Ca, Si; um dos insumos da eletrólise de fundido | M | Normalmente escondido dentro de "basalto"; útil só se o jogo quiser rochas separadas |
| 6 | ✱ **Feldspato** / plagioclásio (anortita-albita) e feldspato-K | RM | Máaz (fenocristais de plagioclásio em matriz rica em K) · ✔ | **Alumínio** (Al₂O₃ ~25–30%), Ca, Na, K; vidro, cerâmica | M–A | **Fonte realista de alumínio** em vez da "bauxita" inventada |
| 7 | **Óxido de Ferro** / hematita + goethita (pigmento vermelho) | RM | Global (15–20% do solo) · ✔ · `mesas_estratificadas` (camadas) | Ferro (redução H₂/carbotérmica), aço, pigmento, nanobastões de Fe (terraformação) | M | Espinha dorsal da siderurgia |
| 8 | ✱ **Magnetita** (Fe₃O₄) | RM | Poeira e basaltos · ✔ | Ferro de alta pureza via **separação magnética** (sem química) | B | Máquina simples "ímã" dá ferro barato → primeira siderurgia |
| 9 | **Perclorato** (sais de ClO₄⁻, Ca/Mg) | RM | Global (0,4–1%, Phoenix/Curiosity) · ✔ | O₂ (decomposição), Cl; precisa ser removido do solo agrícola | B–M | Poluente que vira recurso (já na pesquisa anterior) |

---

## 2. Regionais (cada zona de Jezero com seu perfil)

| # | Material (jogo / científico) | Evid. | Onde · Jezero? · marco | Vira → usos | Extr. | Gameplay |
|---|---|---|---|---|---|---|
| 10 | **Olivina** (forsterita-faialita) | RM | Séítah, Nili Fossae · ✔ · `dunas_seitah` | Mg, Fe, Si; captura de CO₂ (carbonatação); areia de fundição refratária; **gema "peridoto"** em cristal grande | M | Magnésio do fundo da cratera |
| 11 | **Argila** / esmectita Fe-Mg (saponita, nontronita) | RM | Delta ocidental · ✔ · `cratera_belva`, `mesa_kodiak`, `leito_neretva` | Água (~2–3%), cerâmica, tijolo cozido, solo agrícola (retém água), lítio adsorvido | M | Primeira fonte "fácil" de água |
| 12 | ✱ **Pedra Branca** / caulinita (argila de Al) | RM | Blocos soltos claros em Jezero (2025, "clima tropical chuvoso") · ✔ · espalhados no delta/margem | **Alumínio** (caulim ~39% Al₂O₃ → alumina), porcelana, cerâmica refratária, papel/filtro | M | Minério de alumínio **real** em Jezero; peças raras e visíveis ("pontos brancos" no chão) — ótimo para exploração |
| 13 | **Carbonato** Mg-Fe (magnesita, siderita) | RM | Margem do lago, Séítah · ✔ · `carbonatos` (19,5; 12,2) | CO₂ + MgO/FeO (calcinação), cal/cimento, carbono para aço | M | Carbono sólido estocável |
| 14 | **Serpentina** (lizardita/antigorita) | RM | Borda: amostra "Tablelands" (quase 100% serpentina) · ✔ · `mirante_sentinela`, `deslizamento` | Água (~12%), Mg, fibras; **gera H₂ natural** ao se formar | M | Magnésio + água na borda |
| 15 | ✱ **Opala** / sílica opalina (opala-A, hidratada) | RM | Unidade Margem (patch "Bills Bay", amostra "Lefroy Bay") · ✔ · `carbonatos` | **Sílica pura** → vidro óptico, silício, aerogel; água (3–10%) | B–M | Substitui a "areia de sílica pura" [JOGO] por algo real; também preserva fósseis (ciência) |
| 16 | ✱ **Quartzo** / calcedônia | RM | Seixos em Jezero (SuperCam) · ✔ raros | Silício grau solar, cristais osciladores, vidro de quartzo (UV/alta T) | M | Versão "premium" da sílica |
| 17 | **Gipsita** / selenita + anidrita/bassanita (CaSO₄) | RM | Veios no Gale; sulfatos em Jezero · ✔ · `dolina_cristais` (14,3; 17,0) | Gesso (reboco, placas), cimento, enxofre, água (~20% na gipsita), fertilizante Ca-S | B–M | "Minério de água" mais rico do solo |
| 18 | **Sulfato de Magnésio** (kieserita, epsomita, polihidratados) | RM | Fraturas de Séítah; delta ("Hogwallow Flats") · ✔ | Mg, S, água, sal de Epsom (agricultura) | B–M | Par barato de gipsita |
| 19 | ✱ **Jarosita** (KFe₃(SO₄)₂(OH)₆) | RM (Meridiani) | Meridiani, Mawrth · ≈ · `mesas_estratificadas` | Fe, **K** (potássio p/ fertilizante), S, ácido sulfúrico | M | Fonte de potássio → NPK completo |
| 20 | ✱ **Mirtilos** / concreções de hematita ("blueberries", ~4 mm, 24–100% hematita) | RM (Meridiani) | Meridiani · ≈ (licença) · `mesas_estratificadas` | Ferro já concentrado: peneira e pronto | B | Coleta manual divertida (bolinhas no chão) — "ferro de bolso" no início |
| 21 | ✱ **Sal-Gema** / halita e outros cloretos | RM | ~640 depósitos nas terras altas do sul; regolito do delta de Jezero com Cl até 2% · ✔ (disperso) · `dolina_cristais` | NaCl → **sódio** (baterias Na-íon), **cloro** (PVC, HCl, água sanitária), soda cáustica; salmoura para crioproteção | B–M | Fecha a química clássica "cloro-álcalis" |
| 22 | **Fosfato de Ferro** / vivianita e Fe³⁺-fosfatos (+ greigita) | RM | Cheyava Falls / Bright Angel · ✔ · `cheyava_falls` (4,0; 8,0) | Fósforo (fertilizante), Fe | M | Escolha moral preservar × minerar (já na pesquisa) |
| 23 | ✱ **Apatita** / fosfato de cálcio (fluorapatita, merrillita) | RM | Grãos em Jezero (PIXL, "Amalik"); fluorapatita no Gale · ✔ | **Fósforo sem mexer em Cheyava**, flúor, Ca | M | Rota alternativa de fósforo → a decisão moral não trava a agricultura |
| 24 | ✱ **Sulfetos de Ferro** / greigita, pirrotita, pirita | RM | Cheyava Falls; meteoritos marcianos · ✔ traço | Enxofre, Fe; ácido sulfúrico | M | Subproduto do fosfato |
| 25 | ✱ **Zeólita** / analcima | RM (Nili Fossae, vizinha de Jezero) | Picos centrais de crateras perto de Isidis · ≈ · `cratera_atol` | **Peneira molecular**: separar N₂/Ar do ar, capturar CO₂/água, filtrar amônia, solo agrícola | M | Material "técnico" natural para máquinas de ar |
| 26 | ✱ **Nitratos** (NO₃⁻ fixado, 70–1.100 ppm) | RM (Gale) | Sedimentos e areia · ≈ | **Nitrogênio para fertilizante sem Haber-Bosch**; ácido nítrico | M | Atalho de N no início da agricultura |
| 27 | **Gelo de Água** (cavernas) | J (não há gelo raso a 18°N) | Latitudes médias reais; no jogo em cavernas · `fossas_hefesto`, `pocos_colapso`, `tubo_lava_canyon`, `gruta_face_norte` | Água, H₂, O₂ | B | Já aprovado (notas de Recursos) |
| 28 | ✱ **Água Pesada** no gelo/salmoura (D/H ~6× a Terra) | RM (isótopo) | Toda água marciana · ✔ | Deutério: moderador de reator, traçador, fusão D-D (ficção de fim de jogo) | A (enriquecer) | ~1 em cada ~500 moléculas é HDO (Terra ~1 em 3.200): Marte é **"a melhor mina de deutério"** do sistema interno |
| 29 | ✱ **Cromita** / espinélio Cr-Ti | RM | Grãos no regolito e rochas de Jezero (PIXL) · ✔ | **Cromo** → aço inoxidável, refratário, cromagem | M–A | Faz o aço virar inox (resistente à poeira oxidante) |
| 30 | ✱ **Ilmenita** (FeTiO₃) | RM | Regolito de Jezero com TiO₂ alto (PIXL) · ✔ | **Titânio** (via Mg/Kroll), Fe, O₂; TiO₂ (tinta branca, fotocatalisador) | A | Titânio real no mapa (Caio já queria Mg → Ti) |
| 31 | ✱ **Areia Pesada** / placer de minerais pesados (cromita + ilmenita + zircão + magnetita) | RP | Jezero (depósitos de "heavy mineral sands" propostos, 2025) · ≈ · leito do `leito_neretva` | Concentrado multi-metal via peneira/gravidade | M | "Nó misto": uma mina, vários produtos → ótimo para separadores |
| 32 | ✱ **Zircão** / badeleíta (ZrSiO₄ / ZrO₂) | RM | Jezero "Amalik"; meteorito NWA 7034 · ✔ traço | **Zircônio** (revestimento de combustível nuclear!), cerâmica refratária, háfnio (barras de controle) | A | Liga a cadeia nuclear |
| 33 | ✱ **Vidro de Impacto** / rocha fundida por impacto | RM | Crateras (Hargraves, perto de Nili) e borda de Jezero · ✔/≈ · `cratera_atol`, `mirante_sentinela` | Vidro pronto, sílica; guarda bioassinaturas | B | Coleta rápida de vidro "natural" |
| 34 | ✱ **Megabrecha** / rocha profunda da borda (ortopiroxenito, "Silver Mountain" ~3,9 bi anos) | RM | Borda, Witch Hazel Hill · ✔ · `mirante_sentinela`, `deslizamento` | Mistura rica em Mg-Fe-Cr; amostras de ciência | M | "Nó de pesquisa" (amostras → tecnologia, D11) |

---

## 3. Raros (enriquecimentos, veios, "ouro" do jogo)

| # | Material (jogo / científico) | Evid. | Onde · Jezero? · marco | Vira → usos | Extr. | Gameplay |
|---|---|---|---|---|---|---|
| 35 | ✱ **Minério de Níquel** / rochas Al com Ni (até ~8% Ni, metade dos pontos >0,5%) | RM | Blocos claros ricos em Al e Ti em Jezero (alvo "Finch_Lake", sol 784) · ✔ · delta/`leito_neretva` | **Níquel** (aço inox, superligas, catalisador Sabatier, baterias NiFe/Ni-MH), + Cr, Ti, Al do mesmo bloco | M–A | "Veio" raro e rico — tesouro de meio de jogo. Assinatura de depósito Ni-Cu-PGE |
| 36 | ✱ **Minério de Cobre** (Cu 200–400 ppm no Gale; Cu correlacionado ao Ni em Jezero) | RM (traço) / J (minério) | Gale (Kimberley, Glen Torridon); Jezero junto ao Ni · ≈ | **Cobre**: fios, motores, trocadores de calor, eletrônica | A | Gargalo clássico: sem cobre local, cabos vêm da Terra. Teor real é baixo → minério concentrado é licença |
| 37 | ✱ **Óxido de Manganês** (>25% MnO em preenchimentos de fraturas) | RM (Gale) | Fraturas de arenitos (Kimberley) · ≈ · paredes das `fossas_hefesto` | **Mn** → aço-manganês, baterias (Li-Mn, alcalinas), catalisadores; adsorve Cu | M | Veio em fratura: bom para "mineração de parede" em canyon |
| 38 | ✱ **Zinco-Germânio** (Zn até ~8.000 ppm, Ge até ~650 ppm em veios) | RM (Gale) | Sedimentos/veios hidrotermais; Ge elevado em escala global (Spirit/Opportunity) · ≈ · `cratera_atol` (hidrotermal de impacto) | **Zn**: galvanização, baterias Zn-ar · **Ge**: semicondutores, **células solares multijunção**, óptica infravermelha | A | Cadeia de alta tecnologia: Ge é o elo para painéis solares melhores |
| 39 | ✱ **Gálio** (em teor crustal normal, acompanha Al) | RM | Global · ✔ traço | Subproduto do alumínio → GaAs/GaN (células solares, LEDs de estufa) | A | Subproduto "grátis" da refinaria de Al (ótimo design: premia quem faz Al) |
| 40 | ✱ **Boro** (<0,05% B em veios de sulfato de Ca) | RM (Gale) | Veios de gipsita · ≈ · `dolina_cristais` | **Vidro borossilicato** (estufas/labs), **blindagem de nêutrons e barras de controle**, fibra de boro, fertilizante micro | A | Pequeno volume, uso crítico → "tempero" de receitas |
| 41 | ✱ **Lítio** (elevado vs. meteoritos, segue as argilas) | RM (Gale) | Argilas e veios · ≈ · argilas do delta | **Baterias Li-íon**, graxas, ligas Al-Li, trítio (fusão, ficção) | A | Baterias locais = autonomia energética. Teor baixo → licença para "salmoura de lítio" em caverna |
| 42 | ✱ **Fluorita** / flúor (CaF₂; F até ~5% em alvos do Gale) | RM (Gale, 2015) | Conglomerados e arenitos · ≈ | **Gases super-estufa (C₃F₈, SF₆)**, PTFE/teflon (vedações), fluxo de fundição, HF | A | **Muda a terraformação**: fábrica de PFC com flúor local (a pesquisa anterior achava que não havia) |
| 43 | ✱ **Bromo** (brometos; até 0,45% Br no Gale) | RM | Sais de evaporitos · ≈ · `dolina_cristais` | Retardante de chama (habitat!), baterias de fluxo Zn-Br, remédios | M | Subproduto da mesma salmoura do sal-gema |
| 44 | ✱ **Enxofre Nativo** (cristais amarelos puros, Gediz Vallis 2024) | RM (Gale) | Campo de rochas claras no Gale · ≈ (licença) · `dolina_cristais` ou `mesas_estratificadas` | Enxofre direto → Marscrete sem refinar sulfato, ácido sulfúrico, borracha vulcanizada | B | "Achado de sorte" visual (cristal amarelo) que acelera o concreto |
| 45 | ✱ **Terras-Raras** (cério medido em Jezero; monazita/xenotima em NWA 7034) | RM (traço) / J (minério) | Rochas diferenciadas; meteorito "Black Beauty" com 5× mais ETR · ≈ | **Ímãs NdFeB** (motores, turbinas eólicas, drones), fósforos de LED, catalisadores | MA | Tesouro de fim de jogo; permite motores leves sem importar |
| 46 | ✱ **Potássio** (feldspato-K, matriz rica em K dos lavas de Máaz, jarosita; crosta ~0,33% K) | RM | Global (maior em Acidalia); ✔ Máaz | **Fertilizante K** (o "K" do NPK), vidro, sabão | M | Fecha a agricultura: N (nitrato/ar) + P (apatita) + K |
| 47 | ✱ **Tório** (crosta ~0,6 ppm; mapa Odyssey GRS) | RM | Global, maior em Acidalia Planitia · ✘ concentrado (✔ traço) | Combustível nuclear de ciclo tório (U-233) | MA | Reator local de **fim de jogo**; hoje só da Terra |
| 48 | ✱ **Urânio** (traço, ~¼ do Th) | RP | Global traço; depósitos só teóricos (hidrotermais) | Combustível nuclear (precisa enriquecer) | MA | Mantém "reator vem da Terra" por muito tempo |
| 49 | ✱ **Ouro / Prata / Platina marcianos** (depósitos Ni-Cu-PGE, pórfiro de Cu) | T | Tharsis, Syrtis Major; indícios em Gale/Jezero · ≈ (só teórico) | Contatos elétricos, catalisadores, espelhos | MA | Possível "lenda" (rumor de veio) — mas a fonte realista de platinoides é o meteorito (seção 4) |
| 50 | ✱ **Hidrogênio/Metano Geológico** (serpentinização; CH₄ de ppb sazonal no Gale) | T/RP | Borda com serpentina; subsolo · ≈ · `mirante_sentinela` | H₂ e CH₄ "de graça" (poço) | M | Poço de gás raro: alternativa ao H₂ importado da Terra |

---

## 4. Meteoríticos (caídos em Marte)

Já encontrados por rovers: **Heat Shield Rock/Meridiani Planum** (Opportunity 2005, 1º meteorito em outro planeta), **Block Island** (67 cm), **Shelter Island**, **Mackinac Island**, **Oileán Ruaidh** (Opportunity); **Lebanon** (~2 m, o maior, Curiosity 2014), **Egg Rock** (Fe-Ni-P, 2016), **Cacao** (2023) (Curiosity); **Phippsaksla** (~80 cm, Fe-Ni, **borda de Jezero**, set/2025 — 1º do Perseverance). Rochosos: **Barberton, Santa Catarina, Santorini, Kasos** (tipo mesossiderito, Opportunity). **Condritos: nenhum identificado** (frágeis, não sobrevivem ao impacto com a atmosfera fina).

| # | Material (jogo / científico) | Evid. | Onde · Jezero? · marco | Vira → usos | Extr. | Gameplay |
|---|---|---|---|---|---|---|
| 51 | **Ferro-Níquel Meteorítico** / kamacita + taenita (5–25% Ni) | RM | Gale, Meridiani, **borda de Jezero** · ✔ · `meteoritos_ferrosos` (16,5; 14,2) + borda (`mirante_sentinela`) | Aço-níquel **já ligado**, sem redução química (só fundir) | B | Atalho de metal perto da base (já é marco; agora com base real) |
| 52 | ✱ **Schreibersita** ((Fe,Ni)₃P) | RM (Egg Rock) | Dentro dos ferros · ✔ | Fósforo reativo (fertilizante, química), Fe-Ni | M | Bônus escondido do meteorito |
| 53 | ✱ **Troilita** (FeS) | RP | Nódulos em ferros · ✔ | Enxofre, Fe | B | Subproduto |
| 54 | ✱ **Cobalto Meteorítico** (~0,5% Co nos ferros) | RP | Nos ferros · ✔ | **Co**: superligas de motor/turbina, ímãs, baterias | M | Único Co realista no mapa |
| 55 | ✱ **Platinoides** / Pt, Ir, Os, Pd, Ru, Rh (Ir até ~50–60 ppm; PGM total até ~230 ppm nos ferros mais ricos) | RP (medido em ferros na Terra) | Nos ferros · ✔ traço | **Catalisadores** (Ru/Ni do Sabatier, Pt de células a combustível), contatos, eletrodos | A | **Tesouro raro**: cadeia longa (fundir → dissolver → refinar) que só compensa no meio/fim de jogo. Libera catalisador local |
| 56 | ✱ **Meteorito Rochoso** / mesossiderito (silicato + metal) | RM | Meridiani (campo de fragmentos) · ≈ | Mistura olivina + metal Fe-Ni | M | Variação visual/de receita |
| 57 | ✱ **Palasito** / olivina gema em ferro ("peridoto espacial") | J (nenhum achado em Marte) | — · licença · 1 único no mapa (cratera pequena) | Fe-Ni + gemas de olivina (ótica, decoração, conforto dos colonos) | M | **Tesouro raro único**, lindo visualmente; troféu/colecionável |
| 58 | ✱ **Condrito Carbonáceo** (água ~10%, orgânicos, aminoácidos) | T (não achado em Marte) | — · licença | Água, carbono, N orgânico | B | Evento "chuva de meteoros" rara que deixa condritos → sem combate, alinhado ao D10 (meteoritos como ameaça **e** recompensa) |

---

## 5. Atmosféricos (coletor de ar em qualquer lugar)

Composição (NSSDC/NASA): CO₂ 95,1% · N₂ 2,59% · Ar 1,94% · O₂ 0,16% · CO 0,06% · H₂O 210 ppm · NO 100 ppm · Ne 2,5 ppm · HDO 0,85 ppm · Kr 0,3 ppm · Xe 0,08 ppm. Pressão 6,36 mbar (4,0–8,7 conforme a estação).

| # | Material (jogo / científico) | Evid. | Onde | Vira → usos | Extr. | Gameplay |
|---|---|---|---|---|---|---|
| 59 | **CO₂** | RM | Global | O₂ (MOXIE), CO, CH₄ (Sabatier), carbono, plásticos, estufa (plantas) | B | Recurso infinito (já) |
| 60 | **Nitrogênio (N₂)** | RM | Global | Gás tampão do ar respirável, amônia/fertilizante | M | Já |
| 61 | **Argônio** | RM | Global | Gás tampão, **soldagem/fundição inerte**, propelente iônico barato | M | Subproduto do separador de ar |
| 62 | **Oxigênio (traço)** | RM | Global | O₂ | M | Já |
| 63 | **Monóxido de Carbono** | RM | Global + subproduto do MOXIE | Combustível CO/O₂, carbono (Bosch/Boudouard), redutor de Fe | B | Já |
| 64 | **Vapor de Água** | RM | Global (varia por estação) | Água (zeólita/adsorção) | A | Já |
| 65 | ✱ **Óxido Nítrico (NO, ~100 ppm)** | RM | Global | Ácido nítrico, fertilizante | A | Subproduto opcional do separador |
| 66 | ✱ **Neônio (2,5 ppm)** | RM | Global | Iluminação, criogenia | MA | Subproduto de colunas criogênicas |
| 67 | ✱ **Criptônio (0,3 ppm)** | RM | Global | **Propelente de propulsores Hall** (naves/satélites), lâmpadas, isolamento de janelas | MA | Cadeia de "espaço" (fim de jogo) |
| 68 | ✱ **Xenônio (0,08 ppm)** | RM | Global | **Propelente iônico premium**, **anestésico** (medicina), lâmpadas de arco | MA | Tesouro atmosférico; precisa processar oceanos de ar → ótimo gargalo tardio |
| 69 | ✱ **Metano atmosférico** (ppb sazonal) | RM | Gale (picos sazonais) | Irrelevante como fonte; pista científica | — | Só narrativa/ciência (não coletável em escala) |
| 70 | ✱ **Deutério** (HDO do ar e da água; D/H ~6×) | RM | Global | Ver #28 | A | — |
| 71 | ✱ **Gelo Seco** / gelo de CO₂ (calota sazonal + depósito enterrado no polo sul de 9.500–12.500 km³, +65–85% de pressão se sublimado) | RM | Polos · ✘ Jezero (geada de CO₂ só em inverno/latitudes altas) | CO₂ concentrado; **terraformação (pressão)** | A (logística) | Megaprojeto "derreter o polo" → medidor de pressão (fiel a Jakosky: não basta sozinho) |

---

## 6. Espaciais / fim de jogo (fora do mapa, por logística)

| # | Material (jogo / científico) | Evid. | Onde | Vira → usos | Extr. | Gameplay |
|---|---|---|---|---|---|---|
| 72 | ✱ **Regolito de Fobos** (escuro, densidade 1,9 g/cm³, espectro tipo condrito carbonáceo ou material de Marte ejetado; MMX/JAXA vai trazer amostra ~2031) | RP | Órbita (lua) | Carbono, água possível, blindagem, material de estação orbital | A | Tecnologia de "elevador"/estação; lança material de baixa gravidade |
| 73 | ✱ **Regolito de Deimos** | RP | Órbita (lua) | Idem, mais distante e mais fino | A | Complemento de Fobos |
| 74 | ✱ **Gelo Polar de Água** (calota norte, gelo de média latitude — Arcadia, Deuteronilus) | RM | Fora do mapa (35–90°N) | Água em escala, hidrosfera | M (+ logística) | "Rota do gelo" de trem/nave → encher o lago de Jezero |
| 75 | ✱ **Asteroide Metálico Capturado** (tipo M, Fe-Ni-Co-PGM) | T | Cinturão | Metais e platinoides em massa | MA | Projeto final lendário |
| 76 | ✱ **Gelo de Cometa** (H₂O, NH₃, CO₂, CH₄) | T | Sistema externo | Nitrogênio e água para a atmosfera; impacto dirigido | MA | Único jeito realista de subir pressão/N₂ planetário (ficção) |
| 77 | ✱ **Hélio-3** | ✘ não existe de forma útil | A atmosfera bloqueia o vento solar; o He-3 está na Lua | — | — | **Não usar** como recurso marciano (armadilha de ficção) |

---

## 7. Importados da Terra (no começo)

| # | Item | Por que não é local no início | Quando pode virar local | Fonte local futura |
|---|---|---|---|---|
| 78 | **Hidrogênio (semente do Sabatier)** | Sem água extraída ainda | Cedo (argila/gelo) | #11, #17, #27 |
| 79 | **Chips / eletrônica** | Litografia e Si grau eletrônico | Muito tarde | #15–16 + dopantes B (#40), P (#23), Ge/Ga (#38–39) |
| 80 | **Catalisadores (Ru, Ni, Pt)** | Metais raros | Meio (Ni #35) / tarde (PGM #55) | Minério Ni, meteoritos |
| 81 | **Sementes e microrganismos** | Biologia | Após a 1ª colheita | Estufas |
| 82 | **Combustível nuclear / reator** | Enriquecimento | Fim de jogo (tório) ou nunca | #47–48 |
| 83 | **Remédios** | Síntese | Tarde (bioreator de glicose, Xe anestésico) | #59, #68 |
| 84 | **Polímeros especiais / vedações / tecidos de traje** | Química orgânica industrial | Meio/tarde | CH₄/CO₂ + F (#42) + Cl (#21) |
| 85 | **Ímãs de terras-raras e motores** | ETR não mapeadas | Tarde | #45 (ou ímãs de ferrita locais antes) |
| 86 | **Fios de cobre** | Cu raro em Marte | Meio (licença) | #36; alternativa: **cabos de alumínio** (#6, #12) |
| — | **Painéis solares do pouso** | Silício + Ge/Ga | Meio/tarde | #15, #38, #39 |

---

## 8. Produtos refinados / intermediários → de onde vêm (mapeamento, não receita)

| Produto | Matérias-primas (nº do catálogo) | Observação |
|---|---|---|
| Ferro (lingote) | 7, 8, 20, 2, 51 | Magnetita e mirtilos = rota fácil; meteorito = já metálico |
| Aço carbono | Ferro + C (59, 63, 13) | Já na pesquisa |
| ✱ Aço inoxidável | Ferro + Cr (29) + Ni (35, 51) | Resiste à poeira oxidante (perclorato) |
| ✱ Aço-manganês / ferro-ligas | Ferro + Mn (37) | Peças de desgaste (escavadeiras) |
| ✱ Aço-níquel meteorítico | 51 | Sem refino químico |
| Alumínio | 6, 12, (1) | Caulinita é o minério mais limpo |
| ✱ Alumina / cerâmica técnica | 12, 6 | Isolantes, refratários |
| Magnésio | 10, 14, 18, 13 | Já |
| ✱ Titânio | 30 (+ Mg como redutor) | Mg → Ti (Kroll) casa com D-notas |
| ✱ Cromo | 29 | — |
| ✱ Níquel | 35, 51 | Catalisador Sabatier, baterias, superligas |
| ✱ Cobalto | 54 | Superligas, baterias |
| ✱ Cobre (fio, bobina) | 36 | Gargalo |
| ✱ Zinco | 38 | Galvanização (proteção de aço), baterias Zn-ar |
| ✱ Manganês | 37 | — |
| ✱ Zircônio | 32 | Tubos de combustível nuclear |
| ✱ Platinoides | 55 | Catalisadores, células a combustível |
| Vidro comum | 15, 16, 33, 1 | Já |
| ✱ Vidro borossilicato | Sílica + B (40) | Estufas e laboratórios (choque térmico) |
| ✱ Vidro de quartzo | 16 | Janela anti-UV/alta temperatura |
| Fibra de basalto / lã de rocha | 4, 3 | Já / isolante |
| ✱ Fibra de vidro | Vidro | — |
| Silício metalúrgico | Sílica + C ou Mg | Já |
| ✱ Silício grau solar/eletrônico | 15, 16 + refino por zona | Muito tarde |
| ✱ Germânio refinado | 38 | Células multijunção, óptica IR |
| ✱ Célula solar de alta eficiência (GaAs/Ge) | 38, 39 | Upgrade de energia |
| Marscrete (concreto de enxofre) | 1 + S (17, 18, 24, 44, 53) | Enxofre nativo pula o refino |
| ✱ Cimento / cal | 13, 17 | — |
| ✱ Gesso (placas, reboco) | 17 | Interior dos domos |
| Tijolo / cerâmica cozida | 11, 12 | — |
| ✱ Refratários (revestimento de fornos) | 10 (forsterita), 29, 32, 12 | Fornos melhores = tier de fundição |
| Aerogel de sílica | 15 | Já |
| ✱ Ácido sulfúrico | 17, 18, 24, 44 | Base de lixiviação de metais |
| ✱ Cloro / HCl / soda cáustica | 21 | Cloro-álcalis |
| ✱ Sódio metálico | 21 | Baterias Na-íon, trocador de calor de reator |
| Oxigênio | 59, 9, água | Já |
| Hidrogênio | Água (11, 14, 17, 27) ou 50 ou importado (78) | — |
| Metano / LOX (combustível) | 59 + H₂ | Já |
| ✱ Amônia | N₂ (60) + H₂; ou 26 | — |
| ✱ Ácido nítrico | 65, 26, amônia | Fertilizante, explosivo de mineração |
| Fertilizante NPK | N (26, 60) + P (22, 23, 52) + K (19, 46) | Agora fecha 100% local |
| Plásticos (polietileno) | 59, CH₄ | Já |
| ✱ PVC | Cl (21) + eteno | Tubos |
| ✱ PTFE / fluoropolímeros | F (42) + C | Vedações, trajes |
| ✱ Gases super-estufa (PFC, SF₆) | F (42) + C / S | **Terraformação: temperatura** |
| Nanobastões Fe/Al | Ferro, Alumínio | Já (terraformação) |
| ✱ Bateria Li-íon | 41 + Ni/Co/Mn (35, 54, 37) + Al/Cu | Tarde |
| ✱ Bateria Na-íon | 21 + Fe/Mn | **Mais "marciana"** que Li: sódio abundante |
| ✱ Bateria de ferro-ar / Ni-Fe | 7, 35 | Estacionária, robusta |
| ✱ Bateria de fluxo Zn-Br | 38, 43 | Armazenamento grande |
| ✱ Ímã de ferrita | Fe + Ba/Sr (traços em Jezero) | Ímã barato local para motores simples |
| ✱ Ímã NdFeB | 45 + Fe + B (40) | Motores leves (drones) |
| ✱ Motor elétrico | Fio Cu/Al + ímã + aço | — |
| ✱ Cabo de energia | Cu (36) ou **Al** (6, 12) | Alumínio contorna o gargalo do cobre |
| Célula a combustível | Pt (55)/Ni + CH₄/O₂ | — |
| ✱ Peneira molecular | 25 (natural) ou sintética (Al+Si+Na) | Separadores de ar |
| ✱ Blindagem de nêutrons / barras de controle | B (40), Hf de 32 | Reator |
| ✱ Água pesada | 28, 70 | Moderador; ficção de fusão |
| ✱ Propelente iônico | 61, 67, 68 | Naves / satélites (fim de jogo) |
| ✱ Anestésico (xenônio) | 68 | Hospital |
| ✱ Retardante de chama | 43 | Segurança dos habitats |
| ✱ Pigmentos/tintas | 7 (vermelho/ocre), 30 (TiO₂ branco) | Visual das bases (D12: base branca) |
| ✱ Gemas / decoração (peridoto, opala, selenita) | 10, 15, 17, 57 | Conforto dos colonos (D10) |

---

## 9. Terra × Marte: o que não dá cedo e o que vira local depois

**Não dá para fazer em Marte no começo (tem que vir da Terra):**
- Eletrônica (chips, sensores), motores de precisão e rolamentos.
- Catalisadores de metal nobre (Pt, Ru, Pd) — até achar platinoides em meteoritos.
- Combustível nuclear e o reator (tório/urânio são só traço).
- Ímãs de terras-raras; fios de cobre em quantidade.
- Remédios, sementes, microrganismos.
- Polímeros técnicos (vedações, tecidos de traje, lubrificantes).
- O hidrogênio inicial (até a primeira água ser extraída).

**Vira local cedo:** O₂, CO, água (argila/gipsita/gelo), Marscrete, vidro, ferro (magnetita/mirtilos/meteorito), basalto, gesso, cal.

**Vira local no meio:** aço/inox (Cr + Ni de Jezero), alumínio (caulinita/feldspato), magnésio, titânio, fertilizante NPK completo (nitrato + apatita + K), sódio/cloro, PVC, baterias Na-íon/ferro-ar, cabos de alumínio, zeólita para separar ar, catalisador de Ni.

**Vira local no fim:** cobre em escala, germânio/gálio (solar de alta eficiência), silício eletrônico → chips simples, platinoides, terras-raras (ímãs), gases PFC (flúor), combustível de tório, xenônio/criptônio (propelente), água pesada, Fobos/Deimos, gelo polar e cometas.

**Não existe em Marte (evitar ou marcar como ficção):** hélio-3 útil; carvão/petróleo; bauxita real confirmada (usar caulinita); minério de ouro/prata (só teórico); gelo raso em Jezero (licença já aprovada).

---

## 10. Achados novos com maior potencial de jogo (resumo)

1. **Flúor local (fluorita)** → fábrica de gases super-estufa sem importar: conecta a indústria química à temperatura global.
2. **Meteorito Fe-Ni real na borda de Jezero (Phippsaksla)** → justifica o marco `meteoritos_ferrosos` e dá "atalho de aço" + cobalto + platinoides.
3. **Níquel até 8% + cobre + cromo + titânio** nas rochas claras de Jezero → veio raro multi-metal, tesouro de meio de jogo.
4. **Caulinita ("Pedra Branca")** → minério de alumínio real e visível no mapa, substitui a bauxita [JOGO].
5. **Opala / sílica opalina** na Unidade Margem → "sílica pura" real para vidro, silício e aerogel.
6. **Deutério 6×** → Marte como mina de água pesada (reator, e fim de jogo de fusão).
7. **Xenônio e criptônio no ar** → cadeia de propelente iônico / medicina, gargalo lindo de fim de jogo.
8. **Cromita + ilmenita + zircão em areia pesada** → um nó que alimenta separadores (inox, titânio, zircônio nuclear).
9. **Enxofre nativo em cristais** e **manganês >25% em fraturas** → achados visuais de exploração em canyon/dolina.
10. **Sal-gema + nitratos + apatita + jarosita** → sódio (baterias Na-íon), cloro (PVC), e NPK 100% local sem mexer em Cheyava Falls.

---

## Fontes

**Metais e elementos traço**
- Lanza et al. 2016, óxidos de Mn no Gale (GRL): https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016gl069109 · JPL: https://www.jpl.nasa.gov/news/nasa-rover-findings-point-to-a-more-earth-like-martian-past/
- Berger et al. 2022, mobilidade de Mn no Gale: https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2021JE007171
- Gasda et al. 2017, boro (GRL): https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2017GL074480 · Das et al. 2020, B e Li em veios: https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019JE006301
- Berger et al. 2017, Zn e Ge (JGR): https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017JE005290
- Knight et al. 2025, Ga e Ge nos MER (JGR): https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2024JE008569
- Goetz et al. 2023, cobre no Gale: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021JE007101 · Payré et al. 2019, Cu em Kimberley: https://www.sciencedirect.com/science/article/abs/pii/S0019103518304779
- Forni et al. 2024, Ni-Cu em Jezero (LPSC 1236): https://www.hou.usra.edu/meetings/lpsc2024/pdf/1236.pdf
- Payré et al. 2017, alcalinos traço (Li, Rb, Sr, Ba): https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016je005201 · Nikolajsen et al. 2026, lítio no Gale: https://doi.org/10.1029/2025JE009281
- Forni et al. 2015, primeira detecção de flúor: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014GL062742
- Stern et al. 2015, nitratos (PNAS): https://www.pnas.org/doi/10.1073/pnas.1420932112
- Bromo/cloro no Gale (APXS): https://ui.adsabs.harvard.edu/abs/2020AGUFMP069.0009M/abstract · Marker Band: https://www.hou.usra.edu/meetings/tenthmars2024/pdf/3310.pdf
- Enxofre nativo, Gediz Vallis (2024): https://www.nasaspaceflight.com/2024/07/curiosity-gediz-vallis/
- Odyssey GRS, mapa de tório: https://science.nasa.gov/photojournal/map-of-martian-thorium-at-mid-latitudes/ · Taylor et al. 2006, K e Th da crosta: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2005JE002645
- Minérios potenciais em Marte (Earth-Science Reviews, 2025): https://www.sciencedirect.com/science/article/pii/S001282522500251X · Recursos minerais por amostras (2025): https://link.springer.com/article/10.1007/s44461-025-00001-8
- NWA 7034 "Black Beauty", terras-raras: https://www.sciencedirect.com/science/article/abs/pii/S0012821X16303284
- Terras-raras (cério) em Jezero com PIXL: https://www.sciencedirect.com/science/article/pii/S0019103524004159

**Minerais de Jezero e de Marte**
- Shumway et al. 2025, regolito de Jezero rico em sais (Cr-Ti-espinélio, Cl até 2%): https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JE008912
- Fe-fosfatos em Jezero (Nature Comm. 2025): https://www.nature.com/articles/s41467-025-60026-7 · Associações redox (Nature 2025): https://www.nature.com/articles/s41586-025-09413-0
- Lavas de Máaz, matriz rica em K (Science Advances): https://www.science.org/doi/10.1126/sciadv.adr2613
- Ultramáficas carbonatadas em Jezero (Science): https://www.science.org/doi/10.1126/science.adu8264
- Caulinita em Jezero (Purdue, 2025): https://www.purdue.edu/newsroom/2025/Q4/findings-suggest-red-planet-was-warmer-wetter-millions-of-years-ago · https://phys.org/news/2025-12-evidence-driven-climate-mars-jezero.html
- Opala-A em Jezero (Bykov 2026): https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025JE009375 · Sílica hidratada → quartzo (EPSL 2025): https://www.sciencedirect.com/science/article/pii/S0012821X2500055X · Lefroy Bay: https://science.nasa.gov/resource/meet-the-mars-samples-lefroy-bay-sample-23/
- Borda de Jezero (Silver Mountain, Tablelands, Main River): https://www.jpl.nasa.gov/news/nasas-perseverance-mars-rover-studies-trove-of-rocks-on-crater-rim/
- Jarosita e hematita em Meridiani (Science 2004): https://science.sciencemag.org/content/306/5702/1740 · Concreções de hematita: https://www.science.org/doi/10.1126/sciadv.aau0872
- Cloretos nas terras altas (Osterloo et al. 2008): https://www.science.org/doi/10.1126/science.1150690 · THEMIS: https://themis.asu.edu/news/salt-deposits-found-martian-highlands
- Ehlmann et al. 2009, zeólita (analcima), serpentina, caulinita em Nili Fossae: https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2009JE003339
- Vidro de impacto (CRISM, Cannon & Mustard 2015): https://www.jpl.nasa.gov/news/nasa-spacecraft-detects-impact-glass-on-surface-of-mars/
- Poeira magnética (Goetz et al. 2005, Nature): https://www.nature.com/articles/nature03807
- Perclorato no Phoenix (Hecht et al. 2009): https://www.science.org/doi/10.1126/science.1172466

**Meteoritos**
- Phippsaksla (Perseverance, 2025): https://science.nasa.gov/blog/a-stranger-in-our-midst/
- Lebanon e Egg Rock (Curiosity): https://science.nasa.gov/photojournal/curiosity-rover-finds-and-examines-a-meteorite-on-mars/ · https://www.jpl.nasa.gov/news/curiosity-mars-rover-checks-odd-looking-iron-meteorite/ · Cacao: https://astrobites.org/2023/04/29/cacao-meteorite-and-other-fe-ni-meteorites-on-mars/
- Opportunity: Heat Shield Rock https://en.wikipedia.org/wiki/Heat_Shield_Rock · Oileán Ruaidh https://science.nasa.gov/photojournal/opportunitys-close-up-of-a-meteorite-oilean-ruaidh-false-color/ · Ashley et al. 2011: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2010JE003672
- Schröder et al. 2008, meteoritos rochosos (mesossideritos): https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2007JE002990
- Platinoides em ferros e asteroides (PSS 2022): https://www.sciencedirect.com/science/article/pii/S0032063322001945

**Atmosfera, voláteis e espaço**
- NASA Mars Fact Sheet (composição): https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html
- Conrad et al. 2016, Kr e Xe (EPSL): https://www.sciencedirect.com/science/article/abs/pii/S0012821X16304514
- Webster et al. 2013, D/H ~6× (Science): https://www.science.org/doi/10.1126/science.1237961
- Webster et al. 2018, metano sazonal (Science): https://www.science.org/doi/10.1126/science.aaq0131
- Phillips et al. 2011, CO₂ enterrado no polo sul (Science): https://www.science.org/doi/10.1126/science.1203091
- Fobos / MMX / MEGANE: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019EA000811 · Britannica: https://www.britannica.com/place/Phobos-moon-of-Mars
