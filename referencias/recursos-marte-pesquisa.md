# Recursos em Marte — pesquisa para o design do jogo

> Pesquisa feita em 24/09/2026. Objetivo: basear a economia do jogo (automação estilo Satisfactory + colônia estilo Surviving Mars + terraformação) no que existe e no que se faz de verdade em Marte.
> Mapa: área de 8×8 km na cratera Jezero (delta ocidental, entrada do Neretva Vallis, borda da cratera, fundo do antigo lago), ~18,4°N 77,5°E.
>
> Legenda usada no documento:
> - **[REAL]** = dado medido ou processo demonstrado (fonte citada)
> - **[TEÓRICO]** = proposto em artigo/estudo, ainda não demonstrado em Marte
> - **[JOGO]** = simplificação ou invenção nossa para gameplay

---

## 1. O que existe de fato

### 1.1 Atmosfera [REAL]
| Gás | % volume (média anual, Gale/Curiosity SAM) |
|---|---|
| CO₂ | ~95,1% |
| N₂ | ~2,6% |
| Ar (argônio) | ~1,9% |
| O₂ | ~0,16% |
| CO | ~0,06% |
| H₂O (vapor) | traço, varia com a estação |

- Pressão na superfície: ~6–7 mbar (≈0,6% da Terra); varia ~25–30% ao longo do ano porque CO₂ congela nos polos no inverno.
- **Para o jogo:** a atmosfera é o recurso "infinito e onipresente" — CO₂ em qualquer lugar do mapa, N₂ e Ar em pequena proporção (precisa processar muito ar para pouco N₂).

### 1.2 Regolito (solo) [REAL]
Composição média do solo (APXS, rovers Spirit/Opportunity/Curiosity), em % de massa de óxidos:

| Óxido | % aprox. | Vira o quê |
|---|---|---|
| SiO₂ (sílica) | 45–50% | vidro, silício, aerogel |
| FeO/Fe₂O₃ (óxidos de ferro — a cor vermelha) | 15–20% | ferro, aço |
| Al₂O₃ | 5–10% | alumínio |
| MgO | 5–8% | magnésio |
| CaO | 5–7% | cimento/cal |
| SO₃ (sulfatos) | até ~7% na poeira | enxofre → concreto de enxofre |
| Cl (cloretos/percloratos) | ~0,6–0,8% | problema tóxico / fonte de O₂ |
| Percloratos (ClO₄⁻) | ~0,4–1% | tóxico para humanos e plantas |

- A poeira fina é praticamente homogênea no planeta inteiro (tempestades globais misturam tudo).
- Água "ligada" em minerais: em latitudes baixas (<30°) o solo tem ~3–5% em massa de água hidratada de fundo, chegando a ~15% em pontos com sulfatos hidratados.

### 1.3 Gelo de água — tem perto de Jezero? [REAL]
- **Não há gelo raso conhecido em Jezero (18°N).** O mapeamento SWIM (NASA/PSI, equador até 60°N, profundidades 0–1 m, 1–5 m, >5 m) aponta gelo consistente principalmente nas médias latitudes mais ao norte — os locais de pouso "com gelo" mais citados são Arcadia Planitia e Deuteronilus Mensae (~35–45°N+). Perto do equador o gelo superficial é instável e sublima.
- **Fontes de água realistas em Jezero:**
  1. **Minerais hidratados** — argilas (esmectitas Fe/Mg no delta), sulfatos hidratados (gipsita, kieserita, polihidratados), serpentina na borda. Aquecer libera a água. Referência NASA: regolito com 40% de gipsita ≈ 8,6% de H₂O; com 40% de esmectita ≈ 2,7% de H₂O.
  2. **Água "de fundo" do regolito** (3–5%) — aquecimento a 150–400 °C.
  3. **Vapor atmosférico** — existe, mas em quantidade minúscula; adsorção (zeólitas) é possível e muito pouco eficiente. [TEÓRICO]
  4. **Importar gelo** de latitudes altas (logística) ou da Terra no começo. [JOGO: bom gancho de "Suprimentos"]
- Estudo de extração da NASA (M-WIP): planta centralizada com esteira-secadora, produção nominal ~1,35 kg/h, 16 t de água em 480 dias. Ou seja: é **lento e caro em energia** — ótimo gargalo de jogo.

### 1.4 O que o Perseverance encontrou em Jezero (sabor do mapa) [REAL]
| Zona do nosso mapa | Achado real | Recurso no jogo |
|---|---|---|
| **Fundo da cratera — Séítah** | Rocha ígnea rica em **olivina** (cumulato de magma), com carbonatos Mg-Fe nos contornos dos grãos; **sulfatos e percloratos** preenchendo fraturas | Olivina (Mg, Fe, Si); carbonatos (CO₂ + Mg); sais |
| **Fundo da cratera — Máaz** | Basalto/andesito alterado por água | Basalto (construção, fibra de basalto) |
| **Delta ocidental** | Camadas sedimentares com **argilas esmectitas Fe/Mg** e **carbonatos** (confirma orbitais) | Argila (água + cerâmica), carbonato |
| **Margem do antigo lago** | Carbonatos "de margem" vistos de órbita | Carbonato de alta pureza |
| **Neretva Vallis (entrada do rio)** | Rocha **"Cheyava Falls"** (formação Bright Angel), lamito avermelhado com "leopard spots": **vivianita** (fosfato de ferro hidratado) e **greigita** (sulfeto de ferro) + carbono orgânico. Amostra "Sapphire Canyon". Publicado na *Nature* em 10/09/2025 como **potencial bioassinatura** (não confirmada) | Fosfato (fertilizante!), sítio científico/evento narrativo |
| **Borda da cratera (Witch Hazel Hill)** | Pilha de ~75 m de rochas fragmentadas por impactos (megabreccia), rocha fundida por impacto; **serpentina** (amostra "Tablelands") — evidência de água prolongada; amostra bandada "Main River" | Serpentina (água + Mg + possível H₂ natural), rochas raras/profundas |

- **Ideia de design:** cada zona do mapa tem um "perfil mineral" diferente — delta = argilas/água; fundo = olivina/ferro/magnésio; borda = minerais profundos e raros; Neretva = fosfatos/orgânicos + sítio arqueológico-científico. Isso dá razão real para o jogador expandir. [JOGO baseado em REAL]
- Evento narrativo possível: proteger o sítio de Cheyava Falls (não minerar) dá bônus de "Ciência"/reputação — sem combate, alinhado aos pilares.

---

## 2. Processos ISRU (como cada recurso vira algo útil)

| Processo | Entrada → Saída | Status | Números / observações |
|---|---|---|---|
| **MOXIE (eletrólise de óxido sólido)** | CO₂ → O₂ + CO | **[REAL] demonstrado em Marte** | 16 rodadas (2021–2023), **122 g de O₂** no total; pico **12 g/h com ≥98% de pureza** (2× a meta). Escala humana precisaria de ~centenas de vezes maior |
| **Sabatier** | CO₂ + 4H₂ → CH₄ + 2H₂O | [REAL na Terra/ISS] | Base do combustível de retorno (metano + O₂). Precisa de H₂ → precisa de água |
| **Eletrólise da água** | 2H₂O → 2H₂ + O₂ | [REAL] | Maior consumidor de energia da cadeia; fonte do H₂ |
| **Extração de água do regolito** | regolito hidratado + calor → H₂O | [REAL em lab/protótipo NASA] | ~150–400 °C; rendimento de poucos % em massa |
| **Redução de ferro por hidrogênio** | FeO + H₂ → Fe + H₂O (>800 °C) | [REAL em lab] | Bônus: devolve água! |
| **Redução carbotérmica** | óxidos + C (do CO/CH₄) → Fe + CO₂ | [REAL em lab; estudo 2025 com simulante marciano] | Carbono vem da atmosfera (Bosch/CO) |
| **Eletrólise de regolito fundido (MRE)** | regolito fundido → Fe, Si, Al + O₂ | [TEÓRICO/lab] | Muito quente (>1600 °C), muita energia, extrai vários metais de uma vez |
| **Aço** | Fe + C (Bosch) | [TEÓRICO/lab — estudo 2025 com carbono de Bosch e impressão a laser] | Carbono e ferro locais |
| **Silício/vidro** | SiO₂ (+ fundentes) → vidro; SiO₂ + C → Si | [REAL na Terra] | Vidro é fácil; silício grau eletrônico é muito difícil |
| **Alumínio / magnésio** | Al₂O₃ / MgO → Al / Mg | [TEÓRICO] | Exige eletrólise de sais fundidos, muita energia. Olivina de Séítah = fonte de Mg |
| **Concreto de enxofre ("Marscrete")** | regolito + enxofre fundido (~50/50) | [REAL em lab] | ~50 MPa de compressão, sem água, cura rápida, reciclável (re-derreter). Enxofre vem dos sulfatos |
| **Sinterização / impressão 3D de regolito** | regolito + calor/laser/micro-ondas | [REAL em lab] | Tijolos e blindagem contra radiação |
| **Fibra de basalto** | basalto fundido → fibra | [REAL na Terra] | Reforço estrutural leve |
| **Remoção de percloratos** | lavagem com água / bactérias redutoras de perclorato | [REAL na Terra] | >40 espécies de bactérias reduzem ClO₄⁻ → Cl⁻ + O₂ (biorremediação; ESA estuda) |
| **Perclorato como fonte de O₂** | ClO₄⁻ → Cl⁻ + 2O₂ | [TEÓRICO para Marte; é o princípio das "velas de oxigênio" usadas na ISS] | Transforma o problema em recurso |
| **Nitrogênio / fertilizante** | N₂ atmosférico (2,6%) → NH₃ (Haber-Bosch) | [REAL na Terra] | Precisa de H₂; N₂ também é gás tampão do ar respirável |
| **Plásticos** | CO₂/CH₄ → etileno → polietileno; ou CO₂ → glicose → bioreator | [REAL na Terra; NASA CO₂ Conversion Challenge] | NASA premiou sistemas CO₂ → açúcar para alimentar bioreatores que fazem plásticos, remédios, adesivos |
| **Comida** | regolito tratado + água + luz ou hidroponia | [REAL em lab — Wamelink/Wageningen] | 9 de 10 culturas cresceram em simulante marciano (tomate, rabanete, centeio, ervilha, quinoa…; espinafre falhou). **Simulante não tinha perclorato** — solo real precisa ser lavado |
| **Fertilizante de fósforo** | fosfatos (vivianita, apatita) | [REAL — minerais existem] | Gancho perfeito para Neretva Vallis |

---

## 3. Energia

| Fonte | Dados | Status |
|---|---|---|
| **Solar** | Irradiância no topo da atmosfera ~590 W/m² (≈43% da Terra, ~1361 W/m²). Na superfície, NASA usa ~450 W/m² nominal no equador e **~100 W/m² em tempestade de poeira** (opacidade τ 1 → 5). Luz difusa em tempestade ≈30–40% da direta em dia limpo. Poeira acumula nos painéis (Opportunity/InSight morreram assim) | [REAL] |
| **Nuclear de fissão (Fission Surface Power / Kilopower-KRUSTY)** | Referência NASA: **40 kWe** para 6 tripulantes por ~500 dias. Funciona em qualquer latitude, dia/noite, atravessa tempestade global. KRUSTY (2018) validou o conceito em teste de solo | [REAL em teste terrestre; baseline NASA] |
| **Eólica** | Atmosfera ~1% da densidade da Terra → potência do vento ~100× menor na mesma velocidade. Complemento marginal, útil só em tempestades | [REAL — fraco] |
| **Baterias / células de combustível CH₄-O₂** | Armazenamento para a noite (~12 h) | [REAL] |

- **Posição NASA (estudos 2016 e workshop de arquitetura 2025):** fissão é a opção preferida para missões humanas; solar é viável perto do equador, mas precisa de área enorme e sofre em tempestades globais, que são um risco de segurança.
- **Para o jogo:** solar barato no início + evento "tempestade de poeira" que derruba a geração → motiva limpeza de painéis, baterias e, depois, o reator nuclear como upgrade de meio de jogo. [JOGO baseado em REAL]

---

## 4. Ciência da terraformação (para os medidores)

| Método | O que diz a ciência | Status |
|---|---|---|
| **Liberar CO₂ dos polos e do regolito** | Jakosky & Edwards (Nature Astronomy, 2018): todo CO₂ acessível apenas **triplicaria** a pressão atual (~20 mbar), **1/50 do necessário** para aquecimento significativo. Mobilizar carbonatos exigiria "mineração em escala planetária" | [REAL — análise; conclusão: insuficiente sozinho] |
| **Gases super-estufa (PFCs, SF₆)** | Marinova, McKay et al. (JGR 2005): C₃F₈ é o melhor; 1 Pa de C₃F₈ → +33,5 K. Flúor-based preferido (Cl/Br destroem ozônio). Flúor viria de minerais tipo fluorita — **fluorita não foi confirmada em abundância em Marte** | [TEÓRICO; flúor local é suposição] |
| **Nanopartículas engenheiradas** | Ansari, Kite et al. (Science Advances, 2024): nanobastões condutores de **ferro ou alumínio** (~9 µm) aqueceriam **>5.000× mais eficientemente** que gases estufa; liberação contínua de ~30 L/s → +30 °C (>50 °F) em escala de anos, efeitos em meses. Ainda milhões de toneladas | [TEÓRICO — modelo] |
| **Aerogel de sílica (efeito estufa sólido)** | Wordsworth, Kerber & Cockell (Nature Astronomy, 2019): camada de **2–3 cm** deixa passar luz visível, bloqueia UV e aquece o solo abaixo em **até +50 °C**; aquece metros de profundidade em ~1 década. É **regional**, não global | [REAL em lab; TEÓRICO em Marte] |
| **Roadmaps recentes** | Workshop de terraformação 2025 e roadmap de pesquisa 2026 (arXiv) — área voltou a ser levada a sério, com pré-requisito ético (verificar vida nativa antes) | [REAL — literatura] |

**Tradução para medidores do jogo [JOGO]:**
- **Temperatura** ← PFCs (fábrica de gases), nanopartículas (Fe/Al → "Dispersor de Aerossol"), aerogel (local, aquece área).
- **Pressão** ← sublimação de CO₂ (polos/regolito), limite máximo baixo (fiel a Jakosky) → precisa de outras fontes tardias (importação de voláteis de cometas = late game / ficção).
- **Oxigênio** ← MOXIE em escala, perclorato, fotossíntese (fazendas/algas).
- **Água/hidrosfera** ← derreter gelo (só possível após temperatura subir).
- **Biomassa** ← líquens, algas, plantas (só depois de temperatura + pressão).
- Gancho ético: Cheyava Falls → decisão "preservar possível vida nativa vs. acelerar terraformação" (sem combate, escolha moral).

---

## 5. O que precisa vir da Terra (mecânica de "Suprimentos")

| Categoria | No início | Quando pode ser local | Por quê |
|---|---|---|---|
| **Eletrônicos / chips** | Terra | Muito tarde (ou nunca no escopo) | Silício grau eletrônico e litografia exigem cadeia industrial gigantesca |
| **Maquinário de precisão, motores, rolamentos** | Terra | Meio de jogo (peças simples de aço) | Tolerâncias finas |
| **Polímeros complexos, vedações, tecidos técnicos (trajes)** | Terra | Meio/tarde (a partir de CH₄/CO₂) | Química orgânica industrial |
| **Remédios** | Terra | Tarde (bioreatores de glicose) | Síntese farmacêutica |
| **Sementes, microrganismos** | Terra | Depois da 1ª colheita, sementes próprias (Wamelink mostrou sementes viáveis) | Biologia |
| **Reator nuclear / combustível** | Terra | Nunca (urânio local não mapeado) | Enriquecimento |
| **Catalisadores (Ni, Ru, Pt)** | Terra | Tarde/nunca | Metais raros |
| **Hidrogênio (para Sabatier inicial)** | Terra (estratégia clássica de Zubrin: levar H₂ e usar CO₂ local) | Assim que houver extração de água | Leve, rende muito |
| **Estrutura, vidro, O₂, água, concreto, ferro** | — | **Local, desde cedo** | ISRU simples |

**Mecânica sugerida [JOGO]:** janela de lançamento a cada ~26 meses (real: sincronia Terra-Marte) → em escala de jogo, "Nave de suprimento" a cada X sóis com espaço de carga limitado. O jogador escolhe o que pedir (chips vs. sementes vs. remédios). Com o tempo, cada item "desbloqueado localmente" libera espaço de carga → progressão de autonomia clara.

---

## 6. Proposta de tradução para o jogo

### 6.1 Tiers
```
T0 Bruto       → extraído (drill, escavadeira, coletor de ar)
T1 Refinado    → forno, eletrolisador, separador, prensa
T2 Componente  → montadora
T3 Estrutura   → construído no mundo (domo, fábrica, veículo)
T4 Terraform.  → megaprojetos que movem medidores globais
```
"Acessível na superfície, profundo por baixo": T0→T1→T3 com 2–3 máquinas no começo; profundidade vem de subprodutos (ex.: redução de ferro devolve água; MOXIE gera CO utilizável; perclorato vira O₂).

### 6.2 Recursos brutos (T0) — 13 candidatos
| # | Recurso | Onde no mapa | Realidade |
|---|---|---|---|
| 1 | **Regolito** (solo genérico) | Todo lugar | [REAL] |
| 2 | **Ar marciano (CO₂)** | Todo lugar (coletor) | [REAL] |
| 3 | **Óxido de ferro** (hematita/magnetita — depósito) | Fundo da cratera, Máaz | [REAL — composição; "depósito concentrado" é JOGO] |
| 4 | **Areia de sílica** | Dunas/delta | [REAL SiO₂; "areia pura" é JOGO — em Marte a sílica está misturada nos silicatos, embora existam depósitos de sílica opalina em Jezero/Gusev] |
| 5 | **Argila hidratada** (esmectita) | Delta ocidental | [REAL] |
| 6 | **Sulfatos** (gipsita/kieserita) | Fundo/margem do lago | [REAL] |
| 7 | **Olivina** | Séítah | [REAL] |
| 8 | **Carbonato** | Margem do lago/delta | [REAL] |
| 9 | **Basalto** | Fundo da cratera | [REAL] |
| 10 | **Serpentina** | Borda | [REAL] |
| 11 | **Fosfato** (vivianita/apatita) | Neretva Vallis | [REAL a ocorrência; depósito minerável é JOGO] |
| 12 | **Gelo de água** | Não existe no mapa → só por importação/rota | [REAL: ausência em 18°N] |
| 13 | **Bauxita/anortosita (alumínio)** | Borda (megabreccia) | [JOGO — Al existe no regolito, mas não achamos minério concentrado confirmado em Jezero] |

### 6.3 Intermediários (T1–T2) — 22 candidatos
**T1 refinados**
1. Oxigênio (O₂) — MOXIE/eletrólise/perclorato
2. Monóxido de carbono (CO) — subproduto do MOXIE
3. Água (H₂O) — de argila/sulfato/serpentina
4. Hidrogênio (H₂) — eletrólise
5. Metano (CH₄) — Sabatier
6. Nitrogênio (N₂) + Argônio (Ar) — separador de ar (gás tampão do ar respirável)
7. Ferro (lingote) — redução por H₂
8. Vidro — sílica fundida
9. Enxofre — dos sulfatos
10. Magnésio — da olivina
11. Alumínio — eletrólise (tarde)
12. Silício — sílica + carbono
13. Cal/cimento — dos carbonatos/CaO
14. Regolito limpo (sem perclorato) — lavagem/bioreator
15. Fertilizante (NH₃ + fosfato)

**T2 componentes**
16. Placa de concreto de enxofre (Marscrete)
17. Painel de vidro laminado (transparente, com filtro UV)
18. Viga de aço / estrutura metálica
19. Fibra de basalto
20. Tubulação / vedação (polímero do CH₄ — tarde)
21. Célula solar (Si — tarde; no início vem da Terra)
22. Aerogel de sílica (isolamento + terraformação regional)

(Chips, circuitos, remédios e reatores = só "Suprimentos da Terra" no começo.)

### 6.4 MVP — cadeia "pouso → primeiro domo com colonos"

**Conjunto recomendado: 3 recursos brutos + energia**

| Recurso bruto | Máquina | Produto | Usado em |
|---|---|---|---|
| **Regolito** | Escavadeira → **Forno de sinterização/concreto** (com enxofre dos sulfatos simplificado dentro do regolito) | **Placa de Marscrete** | Base e estrutura do domo |
| **Areia de sílica** | Escavadeira → **Forno de vidro** | **Painel de vidro** | Cúpula transparente |
| **Ar marciano (CO₂)** | **Coletor/MOXIE** | **Oxigênio** (+ CO descartado) | Encher o domo (ar respirável) |
| **Energia** (não é recurso de inventário) | Painéis solares (trazidos da Terra no pouso) | kW | Tudo acima |

- Domo = N placas de Marscrete + M painéis de vidro + X unidades de O₂ + ligação elétrica → colonos chegam.
- **4º recurso opcional (se o MVP aguentar):** **Argila hidratada → Água**, que já introduz o "gargalo de água" e prepara a próxima fase (comida, H₂, Sabatier). Se cortar, a água vem como "Suprimento da Terra" inicial.
- **Simplificações do MVP [JOGO], marcadas:**
  - Marscrete real precisa de enxofre refinado separado; no MVP o forno aceita regolito direto.
  - Ar respirável real precisa de N₂/Ar como gás tampão (O₂ puro a pressão alta é risco de incêndio); no MVP "Ar" = só O₂. Upgrade futuro: separador de N₂/Ar.
  - Painel de vidro real precisa de camada anti-UV e laminação contra radiação; no MVP é um item só.
  - MOXIE real produz ~12 g/h — em escala de jogo, a máquina é centenas de vezes mais rápida.
  - Painéis solares do pouso vêm da Terra (fiel à realidade — primeiro produto da mecânica de Suprimentos).

### 6.5 Loops profundos pós-MVP (ideias fiéis à ciência)
- **Ciclo da água fechado:** redução de ferro por H₂ devolve H₂O → incentivo a integrar siderurgia com eletrólise.
- **CO do MOXIE** → carbono para aço (Bosch/carbotérmica) → subproduto vira recurso.
- **Perclorato:** poluente do solo que bloqueia fazendas → bioreator de bactérias limpa o solo **e** gera O₂.
- **Tempestade de poeira:** evento que derruba solar → desbloqueia pesquisa nuclear.
- **Fosfato de Neretva + N₂ do ar** → fertilizante → fazendas em regolito limpo.
- **Ferro/alumínio → nanopartículas** → medidor global de temperatura (conecta indústria ao terraforming).
- **Sílica → aerogel** → aquecimento regional (bolsões verdes antes do planeta todo).

---

## Fontes

**Jezero / Perseverance**
- Liu et al., *Aqueously altered igneous rocks sampled on the floor of Jezero crater* (Science, 2022): https://www.science.org/doi/10.1126/science.abo2196 · https://pubmed.ncbi.nlm.nih.gov/36007009/
- *Sampling Mars: Geologic context and preliminary characterization of samples* (PNAS, 2024): https://www.pnas.org/doi/10.1073/pnas.2404255121
- *Distinct Carbonate Lithologies in Jezero Crater*: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8243932/
- *Olivine-Carbonate Mineralogy of Jezero Crater*: https://arxiv.org/pdf/1801.09841
- JPL — potencial bioassinatura Cheyava Falls / Sapphire Canyon (2025): https://www.jpl.nasa.gov/news/nasa-says-mars-rover-discovered-potential-biosignature-last-year/
- Planetary Society — análise de Cheyava Falls: https://www.planetary.org/articles/a-biosignature-on-mars-unpacking-perseverances-cheyava-falls-find
- JPL — rochas da borda da cratera (Witch Hazel Hill, serpentina): https://www.jpl.nasa.gov/news/nasas-perseverance-mars-rover-studies-trove-of-rocks-on-crater-rim/
- JPL — registro de impactos na borda: https://www.jpl.nasa.gov/news/nasas-perseverance-rover-reads-record-of-ancient-mars-impacts/

**Atmosfera, regolito, água**
- Mahaffy et al., *Abundance and Isotopic Composition of Gases in the Martian Atmosphere from Curiosity* (Science, 2013): https://www.science.org/doi/10.1126/science.1237966
- Trainer et al., *Seasonal Variations in Atmospheric Composition, Gale Crater* (JGR, 2019): https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019JE006175
- NASA — *Chemical, mineralogical, and physical properties of Martian dust and soil*: https://ntrs.nasa.gov/api/citations/20170005414/downloads/20170005414.pdf
- SWIM — Subsurface Water Ice Mapping: https://swim.psi.edu/ · https://science.nasa.gov/resource/swim-map-shows-subsurface-water-ice-on-mars/
- Morgan et al., *Availability of subsurface water-ice resources in the northern mid-latitudes* (Nature Astronomy, 2021): https://www.nature.com/articles/s41550-020-01290-z
- NASA — *Extraction and Capture of Water from Martian Regolith*: https://ntrs.nasa.gov/api/citations/20160010258/downloads/20160010258.pdf
- Sanders — *Mars Water Mining for Future Human Exploration* (KISS/Caltech): https://www.kiss.caltech.edu/workshops/isru/presentations/Sanders_2.pdf
- *Water in the Martian regolith from OMEGA/Mars Express*: https://arxiv.org/pdf/1407.2550
- *Equatorial locations of water on Mars* (Odyssey Neutron Spectrometer): https://arxiv.org/pdf/1708.00518

**ISRU**
- JPL — MOXIE conclui missão: https://www.jpl.nasa.gov/news/nasas-oxygen-generating-experiment-moxie-completes-mars-mission/
- NASA ISRU — Hydrogen Reduction of Regolith: https://isru.nasa.gov/Hydrogen-Reduction-of-Regolith.html · Metals from Regolith: https://isru.nasa.gov/MetalsfromRegolith.html
- Carbothermic reduction of Martian regolith (Acta Astronautica, 2025): https://www.sciencedirect.com/science/article/abs/pii/S0094576525002814
- Aço com carbono de Bosch e LPBF (2025): https://www.sciencedirect.com/science/article/pii/S2772422025000436
- Wan et al., *A Novel Material for In Situ Construction on Mars* (concreto de enxofre): https://arxiv.org/pdf/1512.05461
- Concreto de enxofre sob CO₂ (Icarus, 2024): https://www.sciencedirect.com/science/article/pii/S0019103524001945
- *Perchlorates on Mars: Occurrence and implications* (Icarus, 2024): https://www.sciencedirect.com/science/article/pii/S0019103524003063
- Bactéria redutora de perclorato resistente à radiação: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11546323/
- ESA — Marscrop (biorremediação de perclorato): https://activities.esa.int/4000141974
- NASA CO₂ Conversion Challenge: https://www.nasa.gov/prizes-challenges-and-crowdsourcing/centennial-challenges/co%e2%82%82-conversion-challenge/
- Wamelink et al., *Can Plants Grow on Mars and the Moon* (PLOS One, 2014): https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0103138
- *The Potential for Lunar and Martian Regolith Simulants to Sustain Plant Growth* (Frontiers, 2021): https://www.frontiersin.org/journals/astronomy-and-space-sciences/articles/10.3389/fspas.2021.747821/full

**Energia**
- Rucker et al., *Solar Versus Fission Surface Power for Mars* (NASA, 2016): https://ntrs.nasa.gov/api/citations/20160010550/downloads/20160010550.pdf
- NASA — *Mars Surface Power* (workshop de arquitetura 2025): https://www.nasa.gov/wp-content/uploads/2025/02/2025-ia-workshop-wp-mars-surface-power.pdf
- NASA — *Mars Surface Power Generation* (2023): https://ntrs.nasa.gov/api/citations/20230015763/downloads/Mars%20Surface%20Power%20Generation.pdf

**Terraformação**
- Jakosky & Edwards, *Inventory of CO₂ available for terraforming Mars* (Nature Astronomy, 2018): https://www.nature.com/articles/s41550-018-0529-6
- Marinova, McKay & Hashimoto, *Radiative-convective model of warming Mars with artificial greenhouse gases* (JGR, 2005): https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2004JE002306
- Gerstell et al., *Keeping Mars warm with new super greenhouse gases* (PNAS, 2001): https://www.pnas.org/doi/10.1073/pnas.051511598
- Ansari, Kite et al., *Feasibility of keeping Mars warm with nanoparticles* (Science Advances, 2024): https://www.science.org/doi/10.1126/sciadv.adn4650
- Wordsworth, Kerber & Cockell, *Enabling Martian habitability with silica aerogel* (Nature Astronomy, 2019): https://arxiv.org/pdf/1907.09089 · JPL: https://www.jpl.nasa.gov/news/want-to-colonize-mars-aerogel-could-help/
- *An Introduction to Mars Terraforming, 2025 Workshop Summary*: https://arxiv.org/pdf/2510.07344
- *A research roadmap for assessing the feasibility of warming Mars* (2026): https://arxiv.org/pdf/2604.02242
