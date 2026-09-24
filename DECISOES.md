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
