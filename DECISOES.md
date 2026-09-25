# Jogo de Marte — Decisões

> Registro das decisões tomadas, uma por vez. Base de conhecimento em [CONHECIMENTO.md](CONHECIMENTO.md).

## D1 — O jogador administra a colônia estando no chão (24/09/2026)

- Não existe visão de cima / modo estratégico estilo Surviving Mars.
- **Surviving Mars é referência de funcionalidades**, não de câmera nem de forma de jogar: terraformação e outras mecânicas interessantes de Marte.
- A forma de jogar vem de Subnautica/Satisfactory: o jogador está no mundo, anda, constrói e opera tudo pessoalmente.

## D2 — Colônia com população abstrata (24/09/2026)

- **Jogo final: opção B.** Colonos chegam, moram em habitats e aparecem como números, necessidades (comida, O₂, conforto) e vagas de trabalho nos prédios. Poucos visíveis andando, só como ambientação.
- **Protótipo: opção A.** Só o jogador + robôs/drones.
- **Futuro, se der: opção C** (colonos NPC completos). Não é compromisso.
- Os colonos existem principalmente para sustentar uma **terraformação simples** (ver D3, a decidir).
- Nota técnica: modelar colonos como dados (contagem, necessidades, vagas), não como personagens. Assim dá pra evoluir pra C depois sem jogar fora o sistema.

## D3 — Terraformação híbrida e simples (24/09/2026)

- **Local:** cúpulas/estufas criam bolhas habitáveis desde cedo. É onde os colonos moram. Objetivo de curto prazo ("construir a cúpula e trazer os primeiros colonos").
- **Global:** 3–4 medidores do planeta (ex: pressão, temperatura, oxigênio, água). Sobem devagar. Em marcos, o mundo muda visualmente (céu, água líquida, plantas). Objetivo de longo prazo.
- **Ligação com a automação:** os medidores globais só sobem com produção em escala. A fábrica existe pra transformar Marte (o "elevador espacial" do nosso jogo).
- **Ligação com os colonos:** mais colonos → mais mão de obra → mais produção → terraformação mais rápida → colonos podem viver fora das cúpulas.
- **Loop resultante (rascunho):** explorar → coletar → automatizar → sustentar colonos → terraformar → mundo muda → novas áreas/recursos → explorar mais.

## D4 — Automação híbrida, esteiras como protagonistas (24/09/2026)

- **Esteiras e canos** dentro de cada complexo industrial (estilo Satisfactory). É o diferencial frente aos concorrentes de Marte.
- **Drones/veículos/trens** para longas distâncias entre bases, liberados com o progresso.
- **"Simples por fora"** via QoL: encaixe automático, taxa de cada máquina visível no mundo, aviso claro de gargalo.
- **Tudo é fabricado:** domos, cúpulas e o que vai dentro deles são construídos a partir de peças produzidas nas fábricas.
- **Terra x Marte:** algumas peças vêm ou podem vir da Terra, mas também podem ser fabricadas em Marte. (Ideia a explorar: importar da Terra como atalho caro/lento no início, e produção local como objetivo.)
- **Protótipo:** minerador → esteira → fundição → esteira → baú.
- ⚠️ **Precisa ser detalhado depois**: cadeias de produção, lista de peças, como funciona o suprimento da Terra.

## D5 — Single-player no lançamento, co-op como atualização futura (24/09/2026)

- Lançar single-player. Co-op entra numa atualização futura se houver demanda (é um diferencial grande).
- **A base precisa nascer pronta pra co-op.** Regras de arquitetura desde o primeiro código:
  1. **Simulação separada da apresentação**: a lógica (fábrica, colonos, terraformação) não depende de visual, câmera ou input.
  2. **Toda mudança de estado passa por comandos** ("construir X em Y", "girar esteira"). O jogador nunca altera o estado direto. No co-op, esses comandos passam a ir pela rede.
  3. **Simulação em tick fixo** (ex: 20x/segundo), não por frame.
  4. **Estado 100% serializável**: o mesmo formato serve pro save e, no futuro, pra sincronizar jogadores.
  5. **Toda entidade tem ID único**; nada de "o jogador" como singleton global.
  6. **Pensar como servidor**: single-player = um host com um único jogador.
- Isso não torna o co-op grátis, mas reduz muito o retrabalho. Pesa na escolha da engine (D6).

## D6 — Engine: Unity 6 (24/09/2026)

- **Unity 6 com URP**, versão LTS (hoje 6.3), plano Personal (grátis até US$200k/ano).
- **Por quê:** roda bem no PC de desenvolvimento (Xeon + GTX 1660), C# é texto puro (a IA lê e edita tudo), MCP maduro, maioria dos jogos do gênero feitos em Unity, alcança jogadores com PC fraco.
- **Troca aceita:** gráfico mediano em vez do máximo do Unreal. O "gráfico legal" vem da direção de arte (estilo visual, a decidir), não da força bruta da engine.
- **Stack de IA (ponto de partida):** plugin oficial `Unity-Technologies/unity-agent-plugin` + `unity` CLI; MCP `CoplayDev/unity-mcp` (telemetria desligada). **Evitar** AnkleBreaker (licença exige logo no jogo) e o Unity AI Assistant pago.
- **Regras pro agente:** nunca editar `.unity`/`.prefab`/`.meta` à mão; criar conteúdo via editor scripts; rodar testes antes de concluir tarefa.
- **Co-op futuro:** NGO ou Mirror (decidir quando chegar a hora).
- Pesquisa completa: [CONHECIMENTO.md](CONHECIMENTO.md) seção 9.
- **Pendente:** rodar CPU-Z no PC Xeon (modelo do CPU, AVX2, placa-mãe, slots, canais de RAM) → decidir upgrade de RAM.

## D7 — Câmera: 1ª pessoa a pé, 3ª pessoa nos veículos (24/09/2026)

- **A pé: 1ª pessoa** (padrão Subnautica/Satisfactory). Só braços + ferramenta na tela → evita animação de corpo inteiro.
- **Veículos: 3ª pessoa** (rover, caminhões etc.).
- Possível extra futuro e barato: câmera de foto em 3ª pessoa (pose parada), pra mostrar o personagem.

## D8 — Mundo: contínuo, real + feito à mão, 5 km → 8×8 km (24/09/2026)

- **Mapa contínuo** (desvantagens e mitigação em [CONHECIMENTO.md](CONHECIMENTO.md) 10.10).
- **Real + feito à mão:** relevo real da NASA/USGS como base + formações de outras regiões coladas como stamps + detalhes à mão.
- **Tamanho:** **8×8 km desde o início**, em tiles de 1 km, origem no centro. Se ficar ruim, diminui. 10×10 fica como possibilidade, mas passa do limite recomendado sem floating origin (canto a ~7 km do centro).
- **Atualização 2 (24/09/2026, Caio): mapa de 25×25 km**, crescendo para **nordeste** a partir do 16×16 (canto sudoeste fixo, mesmas coordenadas de mapa para o que já existia). O dado de 1 m (HiRISE) só cobre ~55% do 25×25; o resto usa **CTX 20 m real** (mosaico Mars 2020 + DTMs CTX do catálogo USGS, CC0), que é mais liso — o Caio quer justamente espaço mais reto/liso nessa parte. Norte: sobe para a borda da cratera; leste: fundo plano da cratera.
- **Nível da água: −2560 m** (antes −2530) → lago ~15% do 25×25 (em −2530 seria 24%). Libera fundo de cratera plano entre a base e o lago.
- **Direção do Caio para o mapa (24/09/2026):** o mapa grande existe para dar **espaço de construção** (a base cresce aos poucos, é o foco do jogo, já que há poucas ameaças), não precisa ter "algo interessante" em cada km². **Alguns recursos ficam bem longe da base**, para o jogador ter que explorar e buscar. O carregamento tem que manter o **horizonte visível** sem parecer bugado (sem terreno surgindo do nada nem borda cortada).
- **Mundo sem fim visível (Caio, 24/09/2026):** em volta do mapa jogável há um **terreno de fundo só visual** (sem colisão), com relevo real: CTX 20 m até 8 km da borda e **MOLA 463 m (USGS, CC0)** até 50 km do centro — dá pra ver a cratera de Jezero inteira. Névoa de poeira + céu caramelo (D12) escondem o fim. **Limite:** aviso no traje "SINAL DA BASE FRACO — fora da área de operação" a partir de 1,2 km da borda e barreira invisível a 300 m da borda. Curvatura do planeta (horizonte real ~3,5 km) fica como ideia para testar depois.
- **Streaming de tiles** (carregar só os tiles perto do jogador) entra como próximo passo técnico por causa dos 625 tiles. Mapa maior que 25×25 fica possível depois (dado CTX 20 m cobre dezenas de km em volta), mas não é compromisso.
- **Atualização (24/09/2026, pedido do Caio): mapa de 16×16 km** (256 tiles de 1 km), substitui o 8×8. Motivo: com rovers, 8 km se atravessa em poucos minutos. O mosaico HiRISE de 1 m cobre ~21×21 km em volta de Jezero, então o 16×16 cabe inteiro em dado real de 1 m (mesmo centro do recorte B). Exige **floating origin** (bordas a 8 km do centro) e resolução menor nos tiles distantes.
- **Formas de relevo a incluir (Caio):** paredões verticais retos, falésias longas e vale estreito, espalhados pelo mapa, **sempre com dado real** (CC0). Falésia longa e vale: candidatos naturais na área (borda da cratera, Neretva Vallis). Paredão vertical e vale estreito: stamp **Hephaestus Fossae** (HiRISE `DTEEC_069071_2020_063847_2020_A01`, 1 m, CC0), escolhido pelo Caio entre 4 candidatos renderizados no Unity. **Altura: meio-termo, ~300 m no jogo** (paredes ~75°), em vez dos 150 m iniciais (achatariam demais com o exagero 2×) ou dos ~660 m reais×2. Obs.: as paredes do DTM têm trechos interpolados (triângulos lisos) → disfarçar com textura/ruído.
- **Mapa jogável 28×25 km (Caio, 24/09/2026):** 3 km a menos a oeste, 6 km a mais a leste (planície seca ao norte do lago). **A borda da cratera a oeste é só parcialmente jogável:** o limite passa no **meio da subida** (dá pra subir um pedaço, não chegar ao topo nem atravessar); no norte abre pouco para leste. Coordenadas de edições/limite presas a uma referência fixa (`mapa.json → referencia`).
- **Canyon (Caio, 24/09/2026):** o vale das Hephaestus Fossae foi para a **borda norte** (x 13–23 km, z ≈ 23,6 km nas coordenadas de referência), **só visual**: 10 km de leste a oeste (5,9 km reais esticados no comprimento), profundidade ~300 m no jogo, pontas afinando. O limite jogável contorna a **beirada sul** — dá pra chegar na borda e olhar, não descer. Fora do meio do mapa para não tirar espaço de construção. Mesas isoladas (Gale) ficam como ideia para depois.
- **Área da base inicial (Caio, 24/09/2026):** platô nivelado a mão em x 9,1 km / z 12,05 km do mapa 16×16 (fundo de uma bacia com dunas antigas, ~73 m acima da água futura). Raio 300 m plano + 150 m de transição, altura real −2456,5 m. Configurado em `ferramentas/terreno/edicoes.json` (reaplicado a cada geração).
- **Região:** base em **Jezero** (lago, delta, rio seco → água volta com a terraformação), recorte posicionado pra incluir a borda da cratera (serra, com exagero vertical 1,5–2,5×); **Gale** entra como stamps (morros estratificados) e o **Aeolis Mons** como montanha no horizonte (só visual). Resultado: "inspirado em Jezero e Gale", não geograficamente fiel.
- **Custo:** caminho **gratuito** — dados USGS (CC0), GDAL/QGIS, Unity Terrain Tools, MicroSplat core, Poly Haven/ambientCG, espalhamento de pedras por script do Claude. Reserva de **~US$20, uma vez**, pro módulo URP do MicroSplat se o terreno precisar de mais de 8 texturas.
- **Licenças:** só dados CC0 na área jogável; nunca o mosaico CTX da Murray Lab (NC-ND).
- **Recorte candidato B** (renders em `referencias/mapa/`, scripts no scratchpad da sessão de 24/09): centro 18,4975°N 77,3761°E; 77,305–77,447°E × 18,430–18,565°N. Relevo real ~771 m (−2586 a −1815 m). Contém borda (oeste), Neretva Vallis (entra pelo oeste), delta com escarpa, fundo do lago (leste/sudeste, ~12% do mapa).
- Nível do lago terraformado sugerido: −2530 m (jogabilidade; o lago histórico era mais alto e cobria o delta). Início do jogador sugerido: tile H2, −2521 m (vira margem do lago).
- Fonte: DTM HiRISE 1 m (USGS S3, lido só o recorte a 4 m/px) + DTM CTX 20 m no entorno.
- **Recorte B confirmado** pelo Caio (manter como está). Lago deve ser **pequeno**.
- **Áreas planas (análise do relevo real, com exagero 2×):** só ~6,5% do mapa tem trechos de 100 m com inclinação < 5°. As maiores planícies ficam no fundo do lago (203 ha a −2546 m → alagam com a água em −2530) e perto do início do jogador (89 ha a −2526 m → secas em −2530, alagam se subir 5 m). Poucas planícies no topo do delta (~4–5 ha).
- ⇒ **Nível da água fica em −2530 m** (12% do mapa); subir engole a principal área plana de construção.
- ⇒ **Solução para construir:** (1) fundações/plataformas estilo Satisfactory que nivelam o chão; (2) aplainar à mão alguns platôs médios em pontos estratégicos (topo do delta, pé da serra), já que o mapa é "real + feito à mão".
- **Construção (confirmado):** fundações/plataformas + platôs aplainados à mão. O fundo do lago pode ser usado, mas não é a área principal: tem que haver outras áreas boas de construção.
- **Aviso de alagamento (obrigatório):** o jogador precisa saber que o fundo do lago vai alagar. Formato definido: (1) **aviso ao posicionar** uma construção abaixo do nível futuro da água; (2) **alerta antes do marco** de terraformação que enche o lago, com prazo pra realocar. **Sem** linha d'água no modo construção (decisão do Caio).
- **Versão do Unity: 6.3 LTS** (ver também D6) (suporte até dez/2027). Fixar durante o desenvolvimento.
- **MicroSplat:** Core (grátis) + **"MicroSplat - URP for Unity 6.3"** (US$20, em promoção por US$10 em 24/09/2026). Compra única, licença padrão da Asset Store (1 assento por instalação). Pacote é por versão do Unity → trocar de versão pode exigir comprar outro módulo.

## D9 — Pilares do jogo (24/09/2026)

**O jogo É:**
1. **Transforme Marte com as próprias mãos.** A terraformação é o propósito de tudo; o mundo muda visivelmente (lago de Jezero volta, rio corre, céu muda).
2. **Fábricas que você vê e entende.** Automação é o coração: esteiras, máquinas, cadeias. Simples de usar, profundo de dominar, informação sempre clara na tela.
3. **Uma colônia pra cuidar.** Tudo é construído pra gente viver. A sobrevivência pressiona a colônia, não o jogador com fome a cada 5 minutos.
4. **Um Marte real pra explorar.** Terreno real (Jezero), descobertas que valem a caminhada, progressão que abre novas áreas e recursos.

**O jogo NÃO É:**
- Sobrevivência hardcore (sem microgerenciar fome/sede do personagem).
- City builder visto de cima (D1).
- Procedural ou roguelike (D8).
- Simulação científica rigorosa (inspirado no real; jogabilidade primeiro).
- **Jogo de combate.** Sem armas nem inimigos. As ameaças são o ambiente: tempestades de poeira, radiação/tempestades solares, falhas de equipamento, meteoritos.

**Regra de uso:** toda feature nova precisa servir a pelo menos um pilar e não bater com nenhum "não é".

## D10 — Papel da sobrevivência (24/09/2026)

**Jogador (traje leve):**
- Só gerencia **oxigênio e energia do traje**, que gastam fora de ambientes pressurizados e recarregam na base, nos veículos e em postos construídos.
- **Sem fome nem sede** do personagem.
- Traje evolui com a progressão (tanques maiores → expedições mais longas). A sobrevivência limita a exploração, como no Subnautica.
- **Se o O₂ acabar:** desmaia/morre e reaparece na base, **perdendo os itens do inventário** (estilo Subnautica). Sem morte permanente.

**Colonos (estilo Surviving Mars):**
- Depende da causa: algumas falhas **matam** colonos (ex: falta de O₂, água, comida), outras fazem colonos **quererem voltar pra Terra** (ex: conforto baixo, insatisfação).
- O rigor **depende da dificuldade** escolhida (quais causas matam, quão rápido, tolerâncias).

**Ameaças (ambiente, sem combate):**
- **Tempestade de poeira:** reduz energia solar e visibilidade, pode danificar o que está exposto. Previsão com alguns dias de antecedência.
- **Tempestade solar / radiação:** colonos e jogador precisam se abrigar por um tempo.
- **Falhas de equipamento:** poeira nos painéis, manutenção das máquinas; automatizável com drones mais tarde.
- **Meteoritos:** raros, danificam estruturas; tecnologia de defesa (escudos, reforço).

## D11 — Core loop (24/09/2026)

- **Minuto a minuto:** coletar → construir → conectar → ver funcionando.
- **Sessão (1–2h):** objetivo → planejar a cadeia → explorar pra achar o recurso que falta → automatizar → cumprir → liberar tecnologia nova. Ex: primeiro domo → vidro reforçado → sílica no delta → rover + mineração + esteira → painéis → domo → chegam os primeiros colonos. Tempestade prevista como pressão extra.
- **Campanha (dezenas de horas):** base pequena → colônia sustentável → fábrica em escala → terraformação → Marte muda (céu, lago de Jezero volta, plantas, colonos saem dos domos) → novas áreas/recursos → colônia maior.
- **O que puxa pra frente:** objetivos de missão (direção sem linearidade), árvore de tecnologia (pesquisa com amostras da exploração), necessidade dos colonos, curiosidade.

**Sessões de design futuras (com ideias do Claude):**
- [ ] **História** — o Caio já tem uma ideia; desenvolver juntos. Importante: falta de história é crítica ao 687 Days on Mars.
- [ ] **Pesquisa / árvore de tecnologia** — como funciona; Caio quer ideias.
- [ ] **Suprimentos da Terra** — ritmo, custo, o que vem de lá; Caio quer ideias.
- [ ] Cadeias de produção e lista de peças (pendente da D4).

## D12 — Estilo visual: semi-realista estilizado (24/09/2026)

- Caminho de **Subnautica / Planet Crafter**: formas reais, cores controladas, leitura clara.
- **Paleta em contraste:** Marte em caramelo/ocre/ferrugem; tecnologia humana em branco/cinza claro com luzes frias (ciano/azul) → bases e máquinas se destacam da paisagem (ajuda o pilar 2).
- **Iluminação faz o trabalho pesado:** névoa de poeira, pôr do sol azul (real em Marte), sombra de tempestades.
- **Terraformação como virada de cor:** céu caramelo → azul, água, verde.
- Vermelho liberado neste jogo (a regra "sem vermelho" é da Embrepoli); pode ser reservado pra alertas.
- Próximo: documento de direção de arte (art bible) com paleta e referências.
- **Referências visuais geradas:** `referencias/estilo/` (01 dia, 02 pôr do sol azul, 03 tempestade, 04 terraformação média, 05 terraformado, 06 paleta, 07 base humana). Paleta inicial:
  - Marte: #4A2A1A #653A22 #7A492D #8F5B39 #B98657 #C9A67D · céu #B4885B · horizonte #E3C49A · pôr do sol #A9C6E6 · tempestade #BF8A5C
  - Tecnologia: #F2F3F5 #D9DDE2 #A3AAB2 #5E6670 · luz ciano #8CF2FF #40D9FF · UI #2F8FD8
  - Alertas: âmbar #FFC247 #F5A000 #C77700 · vermelho #E5484D #A8262B
  - Terraformação: céu #9FB0B8 → #4F86C4 · água #3FA6A0 / #1D6A86 · musgo #465F38 #587644 #728A52

## D13 — MVP: "Do pouso ao primeiro domo com colonos" (24/09/2026)

Fatia vertical de **1–2 h de jogo**, base da futura demo do Steam.

| Entra | Fica pra depois |
|---|---|
| Região inicial (~2×2 km dos 8×8), terreno real | Resto do mapa |
| Traje O₂/energia, morte e reaparecimento | Evoluções do traje |
| 3–4 recursos (proposta: gelo, regolito, ferro, sílica — **a definir**) | Recursos raros |
| 5–6 máquinas + esteiras + fundações | Canos, **drones, trens** |
| 1 cadeia completa até o domo | Árvore de tecnologia completa |
| Energia solar + 1 tempestade de poeira | Radiação, meteoritos, estações |
| 1 domo + 5 primeiros colonos (como números) | Colonos avançados |
| 1 medidor de terraformação (sem mudança visual) | Visuais da terraformação |
| Rover simples | Outros veículos |
| Save/load | — |
| Arte provisória (cubos → básica) | Arte final, áudio completo, história |

**Ordem de construção:** (1) andar em 1ª pessoa no terreno real → (2) coletar/máquina/esteira/baú com cubos → (3) fundações → (4) traje, energia, tempestade → (5) cadeia até o domo + colonos → (6) save/load → (7) arte básica.

**Sessão de design futura adicionada:**
- [ ] **Recursos de Marte** — como funcionam na realidade (gelo, regolito, minerais, atmosfera de CO₂, percloratos etc.) e como traduzir pro jogo. Define a lista final de recursos do MVP.

## D14 — Nivelamento de terreno (24/09/2026)

Detalhes: [design/mecanica-nivelamento-terreno.md](design/mecanica-nivelamento-terreno.md).

- O relevo real sempre terá irregularidade; construir nele é resolvido em **três camadas**:
  1. **Fundações auto-niveladoras** (pernas até o chão) — **MVP**.
  2. **Terraplanagem manual** com prévia, volume visível e custo de energia; **cortar gera regolito**, aterrar consome.
  3. **Drone de terraplanagem** automatiza (pós-MVP, coerente com D10).
- **Overlay de inclinação** verde/amarelo/vermelho no posicionamento (faixas em `Data/`, proposta 5°/15° medidos no jogo).
- **Ordem:** fundações → overlay → ferramenta manual → drone.
- **Técnico (D5):** alterar terreno é comando; ajustes de altura ficam no estado da simulação (inteiros, só onde houve edição) e são reaplicados quando um tile carrega no streaming.

## Notas de design — Recursos (em aberto, 24/09/2026)

> Base: [referencias/recursos-marte-pesquisa.md](referencias/recursos-marte-pesquisa.md). Sessão de recursos ainda vai fechar a lista.

- **Gelo pode existir no jogo** mesmo não havendo gelo raso real em Jezero (licença de jogo, marcar como [JOGO]). Água também de argilas/sulfatos aquecidos e, estilo Perdido em Marte / Mars Direct, de hidrogênio trazido da Terra.
- **Recursos onipresentes:** alguns recursos aparecem no mapa todo (como o ferro no Satisfactory). Na vida real o regolito tem 15–20% de óxidos de ferro em todo lugar.
- **Nomes:** "Regolito" vai ser renomeado (a definir). "Areia de sílica" → **"Sílica"**.
- **Metais:** Caio quer entender como funcionam pra definir a parte de metais (ferro, magnésio, alumínio, níquel, cobre…).
- **Cheyava Falls** (possível sinal de vida antiga no Neretva Vallis, real): registrar como ideia de **missão futura** (ex: preservar ou minerar).
- **Terraformação:** Caio quer entender a ciência a fundo e como reproduzir no jogo da melhor forma → sessão dedicada.
- **Suprimentos da Terra:** usar o **Surviving Mars como referência** (fazer algo parecido).
- **Itens de máquina removida caem no chão e ficam lá** (estilo Minecraft/Satisfactory), não somem.
- **Água em duas frentes (aprovado como direção):** (1) **hidrogênio da Terra + CO₂ do ar** (Sabatier) → água + metano/combustível; (2) **gelo escondido em cavernas** (e locais especiais) como alternativa [JOGO].
- **Alumínio:** meio-termo de energia (não tão caro quanto na vida real).
- **Nome do regolito:** finalistas **Basalto** e **Solo Marciano** — decidir depois.
- **Terraformação: parecida com o Surviving Mars** (parâmetros globais alimentados por construções e projetos especiais). Detalhar na sessão de terraformação.
- **Usos dos metais (direção):** magnésio → drones e algumas peças de veículos, redutor pra fazer **silício** (com sílica) e **titânio**, e fertilizante (agricultura). Estrutura do domo: **aço** e/ou **alumínio** (definir).
- **Aço = ferro + carbono**; carbono vem do CO₂ do ar ou dos carbonatos do delta (ambos reais em Jezero).
- **Magnésio em mais de um lugar:** olivina no fundo da cratera **e** serpentina na borda (ambos reais). Nós submersos após a terraformação podem ser minerados com tecnologia de extração subaquática (a definir).

## D15 — Marcos, área jogável e canyon (25/09/2026)

Base: [design/proposta-marcos-e-cavernas.md](design/proposta-marcos-e-cavernas.md) e `referencias/terreno/12_proposta_marcos.png`.

- Problema: o mapa parecia vazio por **falta de marcos**, não por tamanho.
- **Área jogável: Variante A "Delta + Leste"** (~337 km², ~7× Satisfactory; lago ~15%; inclui Cheyava Falls e a cratera-atol).
- **Canyon** sai da borda norte e passa a **cruzar a planície leste na diagonal**, de (19,0; 19,6) a (23,4; 15,0) km, seguido de uma **cadeia de poços de colapso** até (24,9; 13,2) com cavernas de gelo.
- **26 marcos** da proposta aceitos como base, e o Caio quer **mais**: mais cavernas e mais mesas.
- **Subir a montanha:** um trecho da borda da cratera (a parte menos íngreme) passa a ser jogável, com um **mirante** no alto pra ver o mapa (a definir: rota e extensão).
- Pendente de implementação: `mapa.json` (novo polígono), `edicoes.json` (canyon novo; tipos novos `pocos` e `mesas`), cavernas como malhas + Terrain Holes (ver proposta).

## D16 — Base no centro: B2 "Terraço do Lago" (25/09/2026)

Detalhes: seção 8 de [design/proposta-marcos-e-cavernas.md](design/proposta-marcos-e-cavernas.md); imagens `referencias/terreno/17–19`.

- **Base** em (14,40; 13,55) km, a 1,3 km do centro da Variante A, sempre seca (chão final ≥ 64 m reais acima da água).
- **Zona aplainada de ~4,1 km²** (+400 m de transição), inclinação ~0,9° no jogo, 12% da ondulação original → depois **campo de rochas**: pad de pouso (raio 250 m, só cascalho), pedras normais na zona, pedras densas na transição e no pé da mesa.
- **Mesa do Terraço** (real, 13,05; 13,17) **reforçada em +45 m** (forma da Kodiak) → ~+160 m sobre a base no jogo.
- **Início do jogador** no pad da base (14,25; 13,50). **Caverna-tutorial nova:** Abrigo do Terraço, face sul da mesa (12,90; 12,80). Grupo do sul (Kodiak, Perseverance, Séítah) vira a primeira expedição de rover.
- **Novo tipo de edição `nivelamentos`** no pipeline do terreno (plano inclinado ajustado à área + ondulação residual + transição suave).
- **Base antiga (9,1; 12,05)** vira **local de pouso de uma missão anterior**: algo pra encontrar no futuro (foguete, peças, destroços). Diferente do pouso do Perseverance (sítio real, ao sul).

## D17 — Escopo de funcionalidades validado (25/09/2026)

Detalhes item a item: [design/validacao-funcionalidades.md](design/validacao-funcionalidades.md) (base viva, pode ser atualizada).
Critérios usados: Surviving Mars (espinha da colônia) × Satisfactory (fábrica leve) × **vida real** (NASA/ciência) × pilares.

**Principais escolhas:**
- **Exportação realista:** amostras científicas, dados, deutério, combustível em órbita + metais raros (grupo da platina de meteoritos) e/ou um mineral exclusivo de Marte [JOGO]. Metas da missão: em aberto (fora do MVP). Dificuldade: pós-MVP.
- **Terra:** janelas de lançamento (ondas); foguete precisa de metano local pra voltar; dependência da Terra diminui com tecnologias de produção local.
- **Colônia LEVE, sem microgestão:** saúde/bem-estar e especialidades existem mas pesam pouco; traços bem simples; nascimentos no meio do jogo. **Morte/volta pra Terra: mais sutil ou nem ter → revisar D10.**
- **Domos:** módulos cobertos de regolito → domos de gelo translúcidos (Mars Ice Home) → domos de vidro.
- **Robôs** que pousaram antes ajudam a construir: **sistema de planta no chão** (holograma completado pelo jogador ou pelos robôs). Ajudantes iniciais com rodas; drones voadores avançados; rover aberto → pressurizado; caminhão com rota; terraplanagem autônoma; trem no futuro.
- **Fábrica leve** com poucas máquinas de processos reais (forno de redução, MOXIE, Sabatier, sinterizadora, montadora); teor de minério; sala de controle física; receitas alternativas = processos reais.
- **Transporte = tubo selado de cápsulas** (3 níveis, cápsula com janela) da mina até a fábrica. Sem trilho de caçambas. Teleféricos (carga e pessoas) em aberto.
- **Ciclo do hidrogênio** (H₂ + CO₂ → água + metano → eletrólise), gelo depois; metano pra foguetes e geradores de reserva; **rovers elétricos**; reciclagem de água; vento/redemoinhos limpam painéis.
- **Pesquisa:** local (amostras no laboratório) + da Terra (pacotes de tecnologia nos foguetes); descobertas escondidas nos marcos.
- **Desastres:** tempestade = crise de energia/visibilidade (global rara); **estações do ano**; meteoritos ocasionais quebram coisas e trazem itens valiosos; tempestade solar → abrigo; sem terremotos.
- **Terraformação** com 4 medidores ligados e marcos reais (lago, **Limite de Armstrong** = traje leve + máscara, céu azul, ar respirável); prédios de aerogel → gases de flúor/carbonatos → nanopartículas, escudo magnético, espelhos orbitais, cometas.
- **Cavernas só para explorar e coletar** (sem construir dentro). Scanner = radar de subsolo + espectrômetro; sem jetpack. História: decidir depois.

**Sessões de design novas:** sistema de construção por planta; colônia leve (indicador por domo); revisão da D10.
