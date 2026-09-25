# Referência: Satisfactory — inventário completo e alternativas de logística

> Feito em 25/09/2026. Cobre o Satisfactory **1.0** (10/09/2024), **1.1** (10/06/2025) e **1.2** (estável em 02/06/2026). Depois do 1.2 a Coffee Stain não anunciou novo tier de conteúdo: o foco de 2026 é estabilidade de rede e console.
> Lado "Satisfactory" do pedido da [lista de desejos, seção 0](lista-desejos.md). O lado "Surviving Mars" fica para um documento próprio.
> **Nada aqui é decisão.** As recomendações são sugestões do Claude para o Caio aceitar, mudar ou apagar. Decisões ficam em [DECISOES.md](../DECISOES.md).

## Legenda

| Recomendação | Significado |
|---|---|
| **Trazer parecido** | Funciona quase igual no nosso jogo |
| **Adaptar** | A ideia serve, mas muda de forma ou de tema (o "como" está na linha) |
| **Criar novo** | O Satisfactory resolve algo que precisamos, mas a resposta tem que ser nossa |
| **Não trazer** | Bate com um "não é" (D9) ou pesa mais do que o jogo precisa |

**Fase:** **MVP** = entra na fatia vertical (D13) · **Pós** = depois do MVP · **Talvez** = só se sobrar fôlego.

---

## Resumo

| Grupo | Itens | Trazer parecido | Adaptar | Criar novo | Não trazer |
|---|---|---|---|---|---|
| A1 Progressão | 14 | 0 | 9 | 1 | 4 |
| A2 Recursos e nós | 13 | 3 | 7 | 0 | 3 |
| A3a Extração | 5 | 1 | 3 | 0 | 1 |
| A3b Produção | 11 | 2 | 4 | 1 | 4 |
| A3c Energia | 11 | 3 | 4 | 1 | 3 |
| A3d Logística | 25 | 10 | 6 | 2 | 7 |
| A3e Ferramentas de construção | 13 | 9 | 4 | 0 | 0 |
| A3f Organização | 6 | 3 | 2 | 0 | 1 |
| A4 Jogador e veículos | 26 | 5 | 10 | 1 | 10 |
| A5 QoL e interface | 16 | 10 | 4 | 2 | 0 |
| **Total** | **140** | **46** | **53** | **8** | **33** |

**Top para trazer/adaptar (o que dá "cara de Satisfactory" do jeito bom):**
1. **Taxa de cada máquina visível no mundo + aviso de gargalo** (D4 já pede) e um **painel de produção global**, que o Satisfactory **não tem** e é uma das críticas mais comuns.
2. **Pureza de nó** (impuro/normal/puro) e **nós infinitos**: dá motivo pra explorar (D8, D15) sem virar microgerenciamento.
3. **Holograma de construção, encaixe automático, zoop, nudge, pipeta, desmontagem em massa, blueprints**: o "simples por fora" da D4 vem daqui.
4. **Fundações e rampas** (D14, já decidido) + parede com furo para a logística passar.
5. **Overclock/underclock** simples (slider de 50–150% no MVP da fábrica, sem "fragmentos" coletáveis no começo).
6. **Receitas alternativas** encontradas em **exploração** (pouso da missão anterior, D16) em vez de discos rígidos em naves caídas.
7. **AWESOME Sink → "Exportar para a Terra"**: excedente vira **Financiamento**, que compra foguetes de suprimento (liga a fábrica ao modelo Surviving Mars das notas de recursos).
8. **Elevador Espacial → medidores de terraformação** (D3 já diz: "a fábrica existe pra transformar Marte").
9. **Divisor, mescla, divisor inteligente, monitor de fluxo e merge com prioridade**, mas na nossa forma de logística (Parte B).
10. **Veículos com rota gravada** (caminhão/rover de carga) e **drones de carga** para longa distância (D4).

**Não trazer:** combate e armas (D9: xeno-zapper, rifle, nobelisk, criaturas), comida do personagem e inalador (D10), gás tóxico e máscara como sobrevivência do jogador (vira ameaça ambiental da colônia), matéria alienígena (Somersloop, esfera de Mercer, S.A.M., Conversor, Codificador Quântico, Ficsônio, portais, depósito dimensional), Mk1–Mk6 de tudo (no máximo 3 níveis), Acelerador de Partículas com energia variável, Blender/Packager como máquinas separadas no começo, hipertubos com "hypertube cannon".

**Logística (Parte B) — três conceitos-assinatura:**
1. ⭐ **Recomendado: Trilho de Caçambas** — trilho baixo (altura da cintura) onde correm **caçambinhas** com um punhado de itens visível dentro. Substitui a esteira em toda a fábrica. Mesmo modelo de dados da esteira atual (fila de slots), só que cada slot é uma caçamba com pilha pequena.
2. **Tubo Selado de Cápsulas** — upgrade de meio de jogo: tubo translúcido, pressurizado, imune à poeira, mais rápido; cápsulas com "whoosh" e janelas de inspeção.
3. **Teleférico de Carga** — cabo aéreo com torres para ligar complexos distantes por cima do relevo real (canyon, mesas, borda da cratera). Ponte entre o trilho e os drones/trens da D4.

---

# Parte A — Inventário do Satisfactory

## A1. Progressão

| # | Item | O que é no Satisfactory | Rec. | Como / por quê | Fase |
|---|---|---|---|---|---|
| 1 | **HUB** | Base inicial, terminal de marcos, bancada, coletor de biomassa; sobe de nível | **Adaptar** | Vira o **Módulo de Pouso** da base (D16): terminal de objetivos + bancada + armário. Sem upgrade de "HUB", o que cresce é a colônia | MVP |
| 2 | **Tiers 0–9 e marcos (milestones)** | Pacotes de desbloqueio pagos com peças entregues no HUB | **Adaptar** | Vira **objetivos de missão** (D11): "construa o domo", "entregue X vidro". Entregar peças no terminal é um bom loop — manter, mas amarrado a metas da colônia, não a listas genéricas | MVP |
| 3 | **Elevador Espacial e fases 1–5** | Entregas enormes de peças de projeto que liberam tiers; é o "fim" do jogo | **Adaptar** | O papel dele é da **terraformação** (D3): projetos grandes (aquecedores, fábrica de gás estufa) consomem peças e empurram medidores. Visual de "entregar e ver algo gigante mudar" = céu/lago mudando | Pós (MVP tem 1 medidor, D13) |
| 4 | **Peças de projeto** (Smart Plating, Versatile Framework, Modular Engine, Adaptive Control Unit…) | Itens específicos só para o elevador | **Adaptar** | Peças de **domo e terraformação** (painel de domo, vidro reforçado, módulo de habitat). Tudo é fabricado (D4) | MVP (peças do 1º domo) |
| 5 | **M.A.M.** (pesquisa) | Máquina de pesquisa com árvores por material (Caterium, Quartzo, Enxofre, Alien…); consome itens e tempo | **Adaptar** | **Laboratório** que pesquisa com **amostras da exploração** (D11). Árvores por tema de Marte (Geologia, Atmosfera, Biologia, Engenharia). Sessão de design "Pesquisa" pendente | Pós |
| 6 | **AWESOME Sink** | Destrói qualquer item e dá pontos/cupons | **Adaptar** | **"Exportar para a Terra"**: foguete/lançador que envia excedente e dá **Financiamento**. Resolve o lixo da fábrica e alimenta o suprimento da Terra estilo Surviving Mars | Pós |
| 7 | **AWESOME Shop** | Cupons compram cosméticos, peças de arquitetura, alguns itens | **Adaptar** | Financiamento compra **carga de foguete** (suprimentos, colonos, peças da Terra) + cosméticos de base. Sem loja separada: é o menu de pedido à Terra | Pós |
| 8 | **Discos rígidos + receitas alternativas** | Naves caídas dão disco; pesquisa oferece 1 de 3 receitas alternativas (1.0 permite rerrolar) | **Adaptar** | **Registros de dados** achados no pouso da missão anterior (D16), cavernas e marcos (D15). Cada um libera uma receita alternativa escolhida entre 2–3. Recompensa perfeita para exploração (pilar 4) | Pós |
| 9 | **Naves caídas (crash sites)** | Pontos no mapa com disco, às vezes exigem energia/itens para abrir, protegidos por gás/inimigos | **Adaptar** | **Destroços e sondas antigas** (missão anterior D16, sondas reais em Jezero). Barreira = O₂ do traje, terreno, tempestade — nunca inimigos | Pós |
| 10 | **Power Slugs e Fragmentos de Energia** | Lesmas coletáveis → fragmentos para overclock | **Criar novo** (opcional) | Se quisermos overclock com item raro: **fragmentos de meteorito** (marco `meteoritos_ferrosos`, Phippsaksla real) viram "núcleos de sobrecarga". No MVP, overclock sem item ou sem overclock | Talvez |
| 11 | **Somersloop + Amplificador de Produção** | Artefato alienígena dobra a saída de uma máquina (1.0) | **Não trazer** | Alien/mágico; foge de "inspirado no real" (D9). Bônus equivalente pode vir de pesquisa | — |
| 12 | **Esfera de Mercer + Portal/Depósito Dimensional** | Artefatos para portais e depósito "na nuvem" (1.0) | **Não trazer** | Idem. Teletransporte mata a logística, que é nosso diferencial (D4) | — |
| 13 | **Final e história (1.0)** | ADA, Project Assembly, lore; o jogo "termina" no tier 9 | **Não trazer** (forma) | Nossa história é sessão própria (D11). Satisfactory é criticado por final fraco; nosso fim natural é Marte terraformado | — |
| 14 | **Modos de jogo (1.2)** | Multiplicadores de custo, energia, randomização de nós e pureza | **Não trazer** (agora) | Guardar como ideia para depois do lançamento; dificuldade de colônia já está prevista (D10). Randomizar nós contradiz mapa feito à mão (D8) | — |

## A2. Recursos e nós

| # | Item | O que é | Rec. | Como / por quê | Fase |
|---|---|---|---|---|---|
| 1 | **Minérios sólidos**: ferro, cobre, calcário, carvão, catério, quartzo bruto, enxofre, bauxita, urânio, S.A.M. | 10 recursos em nós fixos | **Adaptar** | Nossa lista vem do [catálogo](catalogo-materiais.md): óxido de ferro/magnetita, sílica/opala, olivina (Mg), caulinita/feldspato (Al), carbonato (C), gelo… Nada de "catério" inventado | MVP (3–4, D13) |
| 2 | **Nós infinitos** | Nó nunca acaba | **Trazer parecido** | Evita logística de "mina esgotada"; bate com fábrica mais leve | MVP |
| 3 | **Pureza** (impuro/normal/puro = 0,5×/1×/2×) | Multiplica a taxa do minerador | **Trazer parecido** | Nós puros longe da base = motivo para ir longe (D8 "alguns recursos bem longe"). Valores em `Data/` | MVP |
| 4 | **Fluidos**: água, petróleo, nitrogênio, combustíveis, ácidos | Pipes, bombas, tanques | **Adaptar** | Fluidos de Marte: água, CO₂/N₂/Ar do ar, H₂, O₂, metano (Sabatier). Poucos e com propósito (colônia) | Pós (canos fora do MVP, D13) |
| 5 | **Poços de recurso** (pressurizador + extratores satélite) | Campo de fissuras; água/óleo/nitrogênio | **Adaptar** | **Poços de colapso com gelo** (D15) ou fontes de gás: 1 pressurizador + satélites. Encaixa em marco existente | Pós |
| 6 | **Extrator de água "de qualquer lugar"** | Coloca na água superficial | **Não trazer** | Não há água líquida no começo; depois da terraformação o lago (D8) pode aceitar bomba → vira **recompensa da terraformação** | Pós (pós-lago) |
| 7 | **Gêiseres + gerador geotérmico** | Nó especial de energia variável | **Adaptar** | **Fumarola/respiro de calor** raro (licença de jogo) ou nada. Ver A3c | Talvez |
| 8 | **Cadeia nuclear** (urânio → barras → usina → lixo → plutônio → ficsônio) | Energia alta com resíduo | **Adaptar** (curto) | **Kilopower** (reator pequeno real) com combustível **vindo da Terra** e sem cadeia de lixo. Ficsônio: não trazer | Pós |
| 9 | **Scanner de recursos** | Pulso que mostra nós próximos | **Trazer parecido** | Já está na lista de desejos (seção 9). Pulso barato, ícones no HUD | MVP |
| 10 | **Scanner de objetos** | Aponta para coletáveis (lesmas, esferas, discos) | **Adaptar** | Vira modo do mesmo scanner para **amostras científicas e destroços** | Pós |
| 11 | **Recursos coletáveis soltos** (pedras, folhas, flores, cogumelos) | Biomassa manual | **Adaptar** | **Coleta manual de amostras e "mirtilos" de hematita** (catálogo #20). Sem biomassa: não há plantas em Marte até a terraformação | MVP (coleta manual inicial) |
| 12 | **Gás tóxico / radiação por nó** | Áreas perigosas ao redor de alguns nós | **Não trazer** (como está) | Perigo contínuo por área cansa. Radiação vem por **evento** (tempestade solar, D10) | — |
| 13 | **Biomassa (queimador de biomassa)** | Primeira energia com folhas | **Não trazer** | Não existe em Marte; energia inicial é solar vinda da Terra (lista de desejos, seção 5) | — |

## A3a. Extração

| # | Item | O que é | Rec. | Como / por quê | Fase |
|---|---|---|---|---|---|
| 1 | **Minerador Mk1–Mk3** | 60/120/240 por min em nó normal | **Trazer parecido** (menos níveis) | Já existe na simulação (`Miner`). Máx. 2–3 níveis | MVP (Mk1) |
| 2 | **Minerador portátil** | Miniminerador colocado à mão, baixa taxa | **Adaptar** | **Robô minerador inicial** ("robôs que ajudam no começo", seção 0): anda até o nó e enche a própria caçamba. Ponte para o minerador fixo | MVP |
| 3 | **Extrator de água** | Bombeia de superfície | **Adaptar** | Ver A2 #6: só no lago terraformado; antes, água vem de gelo/argila/Sabatier | Pós |
| 4 | **Extrator de petróleo** | Em nó de petróleo | **Não trazer** | Sem petróleo em Marte. "Combustível" = metano do Sabatier | — |
| 5 | **Pressurizador + extrator de poço** | Ver A2 #5 | **Adaptar** | Poço de gelo/gás | Pós |

## A3b. Produção

| # | Item | O que é | Rec. | Como / por quê | Fase |
|---|---|---|---|---|---|
| 1 | **Smelter** | 1 entrada → lingote | **Trazer parecido** | Já existe (`Smelter`). "Fundição" da D4 | MVP |
| 2 | **Foundry** | 2 entradas → liga (aço) | **Trazer parecido** | **Forno de aço** (ferro + carbono), lista de desejos seção 3 | MVP ou logo após |
| 3 | **Constructor** | 1 entrada → peça | **Adaptar** | **Prensa/Impressora 3D** de peças simples (placas, vigas). Nome e visual nossos | MVP |
| 4 | **Assembler** | 2 entradas → peça | **Adaptar** | **Montadora** (lista de desejos) | MVP (1 receita do domo) |
| 5 | **Manufacturer** | 3–4 entradas → peça complexa | **Adaptar** | Montadora avançada no pós-MVP; talvez fundir com a Montadora em "níveis" | Pós |
| 6 | **Refinery** | Fluido + sólido; plástico, borracha, combustível | **Adaptar** | **Reator químico** genérico: Sabatier, eletrolisador, MOXIE, cloro-álcalis — cada um com visual próprio mas mesma lógica | Pós |
| 7 | **Blender** | 4 entradas fluido/sólido | **Não trazer** | Fundir no reator químico. Menos máquinas = mais leve | — |
| 8 | **Packager** | Embala fluidos em latas | **Não trazer** | Transporte de fluido por cano/tanque/veículo basta | — |
| 9 | **Particle Accelerator** | Energia variável, receitas de fim de jogo | **Não trazer** | Fim de jogo alienígena; nosso fim de jogo é terraformação | — |
| 10 | **Converter / Quantum Encoder** (1.0) | Transmutação de minérios com S.A.M.; itens quânticos | **Não trazer** | Alienígena; o Conversor ainda apaga a exploração (troca minério por minério) | — |
| 11 | **Bancada de fabricação manual** | Clicar e segurar para fabricar | **Criar novo** | **Impressora de bordo** no módulo de pouso: fila de itens simples, sem "segurar botão". Só para o começo | MVP |

## A3c. Energia

| # | Item | O que é | Rec. | Como / por quê | Fase |
|---|---|---|---|---|---|
| 1 | **Queimador de biomassa** | Primeira energia | **Não trazer** | Ver A2 #13 | — |
| 2 | **Gerador a carvão** | Carvão + água | **Não trazer** | Sem combustão (não há O₂ livre) | — |
| 3 | **Gerador a combustível** | Queima combustível líquido | **Adaptar** | **Gerador metano/O₂** (ambos do Sabatier/MOXIE): energia de reserva para tempestade | Pós |
| 4 | **Geotérmico** | Em gêiser, saída oscilante | **Adaptar** (talvez) | Ver A2 #7 | Talvez |
| 5 | **Usina nuclear** | Alta energia, resíduo | **Adaptar** | Kilopower (A2 #8) | Pós |
| 6 | **Energia solar** | Não existe no Satisfactory | **Criar novo** | Nossa energia base (D13); cai com poeira e tempestade (D10). Painel sujo → limpeza manual/drone | MVP |
| 7 | **Bateria (Power Storage)** | Armazena energia, 100 MWh | **Trazer parecido** | Essencial para noite e tempestade | MVP ou logo após |
| 8 | **Postes e cabos Mk1–3, tomada de parede, torre de energia** | Rede por conexões | **Trazer parecido** (simplificado) | 1 poste + 1 torre longa. **Daisy-chain entre prédios (1.2)** e **pernas de fundação levando energia** reduzem cabo | MVP |
| 9 | **Interruptor e interruptor de prioridade** (1.0) | Liga/desliga ramos; corta por prioridade quando falta energia | **Trazer parecido** (prioridade) | Com tempestade (D10) o jogador precisa escolher o que fica ligado: **prioridade por prédio** (suporte à vida primeiro). Automático, sem fiação extra | MVP (versão simples) |
| 10 | **Fusível que desarma** | Rede cai toda quando consumo > geração | **Adaptar** | Queda total é punitiva. Preferir **cortes por prioridade** automáticos e aviso claro | MVP |
| 11 | **Alien Power Augmenter** (1.0) | Somersloop aumenta energia da rede | **Não trazer** | Alienígena | — |

## A3d. Logística

> As esteiras são o ponto mais sensível (lista de desejos, seção 0). A recomendação aqui é sobre **a função**; a **forma** está na Parte B.

| # | Item | O que é | Rec. | Como / por quê | Fase |
|---|---|---|---|---|---|
| 1 | **Esteira Mk1–Mk6** (60/120/270/480/780/1200 por min) | Transporte principal | **Criar novo** | **Trilho de Caçambas** (Parte B). Máx. **3 níveis** (ex.: 60/120/240 por min, valores em `Data/`) | MVP |
| 2 | **Esteira reta/curva, modos de construção** | Arrastar do ponto A ao B com curva automática | **Trazer parecido** | Arrastar célula a célula na grade; curva automática | MVP |
| 3 | **Elevador de esteira (lift)** | Vertical | **Adaptar** | **Elevador de caçambas** (nória, como moinho/mineração real): cadeia vertical de canecas. Muito legível | Pós |
| 4 | **Splitter** | 1 → 3 alternando | **Trazer parecido** | **Desvio/agulha** do trilho: alterna caçambas | MVP ou logo após |
| 5 | **Merger** | 3 → 1 | **Trazer parecido** | **Junção** do trilho | MVP ou logo após |
| 6 | **Priority Merger** (1.1) | Mescla com prioridade | **Trazer parecido** | Junção com prioridade: útil para "abastecer o domo primeiro" | Pós |
| 7 | **Smart / Programmable Splitter** | Filtra por item / sobra | **Trazer parecido** (um só) | **Agulha com filtro**: item escolhido + "sobra". Um prédio em vez de dois | Pós |
| 8 | **Monitor de throughput** (1.1) | Mede itens/min num ponto | **Trazer parecido** | Melhor ainda: **toda caçamba/trilho mostra taxa ao olhar** (D4). O monitor fica como placa física | MVP (leitura ao olhar) |
| 9 | **Furo de parede para esteira** (1.1) | Passar esteira por parede | **Trazer parecido** | Barato e evita frustração | Pós |
| 10 | **Baús Mk1/Mk2, armazém industrial** | Estoque | **Trazer parecido** | Já existe (`Storage`). 2 tamanhos | MVP |
| 11 | **Pipes Mk1/Mk2, bombas, válvulas, T (1.2), buffer** | Fluidos com física de cabeça de pressão | **Adaptar** | Canos **sem física de altura/pressão** (só vazão), é a parte mais odiada do Satisfactory por novatos. Bomba só se precisar | Pós |
| 12 | **Tanques de fluido** | Buffer | **Trazer parecido** | Tanques de gás/líquido (lista de desejos) | Pós |
| 13 | **Trens** (estação, plataformas de carga/fluido, sinais de bloco e de caminho) | Longa distância, alta vazão, sinais complexos | **Adaptar** | Trem **sem sinalização manual**: 1 linha = 1 trem ou colisão impossível. Chega depois do teleférico | Pós |
| 14 | **Caminhões e tratores com rota gravada** | Grava o trajeto dirigindo; estação de carga; 1.2 refez rotas com build gun | **Adaptar** | **Rover de carga autônomo**: rota desenhada no mapa/com a ferramenta (modelo 1.2), não gravada dirigindo. Casa com "carro de transporte" do Surviving Mars | Pós |
| 15 | **Caminhão de fluido** (1.2) | Tanque 3200 m³ com estação | **Adaptar** | Mesmo rover com módulo de tanque | Pós |
| 16 | **Drones + porto de drones** | Ponto a ponto, gasta bateria como combustível | **Adaptar** | **Drones de transporte** (D4, Surviving Mars): porto com raio de atuação, magnésio na fabricação (notas). Combustível = energia da rede, sem item de bateria | Pós |
| 17 | **Hipertubos** (entradas, junções e ramos 1.1, "canhão") | Transporte do jogador em tubo | **Não trazer** (forma) | Nosso jogador anda de rover (D7) e em **corredores pressurizados** (lista de desejos) | — |
| 18 | **Jump pad / U-Jelly** | Pula longe | **Não trazer** | Com 0,38 g o pulo do jogador já é maior; não precisa | — |
| 19 | **Elevador de pessoas** (1.1) | Elevador com andares | **Trazer parecido** | Útil em domos e prédios altos | Pós |
| 20 | **Portal** (1.0) | Teletransporte entre bases | **Não trazer** | Anula exploração e logística | — |
| 21 | **Depósito Dimensional** (1.0) | Estoque global acessível na bancada | **Não trazer** (forma) | Alternativa leve: **o módulo de pouso puxa de baús conectados à rede da base** para construir (QoL sem magia) | Pós |
| 22 | **Transporte de pacote pequeno por esteira** | Cada item é um objeto na esteira | **Não trazer** (forma) | Simulação já usa arrays (regra 8); a caçamba reforça isso | — |
| 23 | **Esteira de fluido/empacotado em esteira** | Latas na esteira | **Não trazer** | Ver A3b #8 | — |
| 24 | **Bombas de altura (head lift)** | Física de fluido vertical | **Não trazer** | Ver #11 | — |
| 25 | **Cabo/tirolesa de carga** | Não existe no Satisfactory | **Criar novo** | **Teleférico de Carga** (Parte B) | Pós |

## A3e. Ferramentas de construção

| # | Item | O que é | Rec. | Como / por quê | Fase |
|---|---|---|---|---|---|
| 1 | **Build gun** | Ferramenta única para construir/desmontar | **Adaptar** | **Ferramenta de construção do traje** (D10): mesmo papel, visual nosso (projetor holográfico no pulso) | MVP |
| 2 | **Fundações, rampas, pilares** | Chão plano sobre terreno | **Trazer parecido** | D14: fundações auto-niveladoras com pernas | MVP |
| 3 | **Paredes, janelas, portas, telhados, vigas, escadas** | Arquitetura | **Trazer parecido** (poucas) | Poucas peças no MVP; mais peças são cosmético pós | Pós |
| 4 | **Holograma de pré-visualização** | Mostra antes de construir, verde/vermelho | **Trazer parecido** | + overlay de inclinação (D14) e aviso de alagamento (D8) | MVP |
| 5 | **Encaixe (snap) em grade e em portas de entrada/saída** | Alinha prédios e logística | **Trazer parecido** | Nossa simulação já é grade: encaixe é natural | MVP |
| 6 | **Zooping** | Arrastar para construir várias fundações/paredes de uma vez | **Trazer parecido** | Barato e muito elogiado | MVP |
| 7 | **Nudge (empurrão)** incl. vertical ilimitado (1.1) | Ajuste fino | **Trazer parecido** | Na grade é 1 célula por vez | Pós |
| 8 | **Pipeta (copiar prédio e receita)** | Clique do meio | **Trazer parecido** | Atalho de altíssimo valor | MVP |
| 9 | **Desmontagem em massa** | Seleciona vários e desmonta | **Trazer parecido** | Itens da máquina vão para o inventário ou caem no chão (notas: "caem no chão e ficam lá") | MVP |
| 10 | **Blueprints** (Mk1–Mk3, auto-connect 1.1) | Salvar/colar layouts | **Adaptar** | **Copiar/colar direto** (sem prédio "Designer"), resposta à crítica de "construir de novo e de novo". Estado de simulação ajuda (é só lista de comandos) | Pós |
| 11 | **Customizer** (cores, materiais, padrões) | Pintura | **Adaptar** | Poucas cores da paleta D12; pintar linhas de logística por produto ajuda a ler a fábrica | Pós |
| 12 | **Sinais de trem livres, esteira reta (1.0)** | Precisão | **Trazer parecido** | Esteira reta é o padrão na grade | MVP |
| 13 | **Terraplanagem** | Não existe | **Adaptar** (é nosso) | D14 (manual + drone) | Pós |

## A3f. Organização

| # | Item | O que é | Rec. | Como / por quê | Fase |
|---|---|---|---|---|---|
| 1 | **Placas (signs)** com ícone/texto, zoop (1.2) | Etiquetar | **Trazer parecido** | Ícone automático do item no baú/máquina reduz a necessidade | Pós |
| 2 | **Luzes e painel de controle de luz** | Iluminação | **Trazer parecido** | Noite marciana + luz fria (D12) | Pós |
| 3 | **Marcadores no mapa (stamps)** | Pinos | **Trazer parecido** | | MVP |
| 4 | **Depósito Dimensional** | Ver A3d #21 | **Não trazer** | | — |
| 5 | **Rótulos de baú / filtro de slot** | Trava slot para item | **Adaptar** | Baú com "item fixo" simples | Pós |
| 6 | **Lista de tarefas / To-Do e Codex** | Lembretes de receitas | **Adaptar** | **Painel de objetivo** mostra o que falta e onde fabricar cada peça | MVP |

## A4. Jogador, equipamento e veículos

| # | Item | O que é | Rec. | Como / por quê | Fase |
|---|---|---|---|---|---|
| 1 | **Inventário com slots** (aumenta via pesquisa) | Mochila | **Trazer parecido** | Mochila cresce com o traje (D10). Perde itens ao morrer (D10) | MVP |
| 2 | **Slots de equipamento** (corpo, mãos, cabeça) | Equipar itens | **Adaptar** | **Módulos do traje**: tanque maior, bateria, propulsor | Pós |
| 3 | **Oficina de equipamento** | Fabrica equipamento | **Adaptar** | Mesma impressora de bordo | Pós |
| 4 | **Jetpack** | Voo curto com combustível | **Adaptar** | **Propulsor de O₂/CO₂** que gasta energia do traje; em 0,38 g rende muito | Pós |
| 5 | **Hoverpack** | Flutua perto de energia | **Não trazer** | Redundante com o propulsor | — |
| 6 | **Blade Runners** | Corre e pula mais | **Não trazer** | Com 0,38 g o pulo já é alto; velocidade vem do rover | — |
| 7 | **Zipline** | Desliza em cabos de energia | **Adaptar** | Se tivermos **teleférico**, o jogador pode "pegar carona" num gancho dele (Parte B) | Talvez |
| 8 | **Paraquedas** | Queda | **Não trazer** | Atmosfera fina: paraquedas não funciona bem (real). Queda amortecida pelo propulsor | — |
| 9 | **Máscara de gás / traje hazmat / filtros / iodo** | Proteção de área | **Não trazer** (forma) | O traje já é o equipamento; radiação = abrigo (D10) | — |
| 10 | **Inalador medicinal, comida (frutas, nozes, cogumelos)** | Cura | **Não trazer** | Sem fome/vida microgerenciada (D10). Recarga de O₂/energia em postos | — |
| 11 | **Xeno-Zapper, Xeno-Basher, Rebar Gun, Rifle, Nobelisk** | Combate | **Não trazer** | D9: sem combate | — |
| 12 | **Motosserra** | Limpa vegetação | **Não trazer** | Não há vegetação; limpeza de pedras vem da terraplanagem (D14) | — |
| 13 | **Criaturas (hog, spitter, stinger) e fauna passiva (Lizard Doggo)** | Inimigos e pet | **Não trazer** | D9. Companheiro possível: **robô ajudante** (seção 0) | — |
| 14 | **Pioneer customizável** (1.0) | Aparência do personagem | **Adaptar** | Cores/decalques do traje; foto em 3ª pessoa (D7) | Talvez |
| 15 | **Selfie/modo foto** (1.1, 1.2) | Fotos | **Adaptar** | Modo foto simples (D7 já citou) | Talvez |
| 16 | **Beacon** | Marcador físico | **Trazer parecido** | Barato; útil com tempestade (visibilidade baixa) | Pós |
| 17 | **Explorer** | Buggy rápido | **Trazer parecido** | **Rover simples** (D13) | MVP |
| 18 | **Tractor / Truck** | Carga + rota automática | **Adaptar** | Rover de carga (A3d #14) | Pós |
| 19 | **Cyber Wagon** | Veículo piada | **Não trazer** | | — |
| 20 | **Factory Cart** | Carrinho rápido dentro da fábrica | **Adaptar** | Se as fábricas forem grandes: um **carrinho que anda sobre o próprio trilho de caçambas** (reuso do sistema) | Talvez |
| 21 | **Trem de passageiro** | Viagem | **Trazer parecido** (junto com trem) | | Pós |
| 22 | **Veículo autônomo de terraplanagem** | Não existe | **Criar novo** | D14 + Surviving Mars | Pós |
| 23 | **Coleta de itens à mão / bancada no início** | Loop inicial de "bater em pedra" | **Adaptar** | Coleta rápida de amostra/nó, mas o robô minerador inicial tira o jogador disso cedo | MVP |
| 24 | **Morte e mochila no chão** | Deixa caixa com itens | **Adaptar** | D10: perde os itens (pode deixar uma cápsula recuperável, a decidir) | MVP |
| 25 | **Hub terminal "Ship upgrades" (upgrade de inventário)** | Mais slots por marco | **Trazer parecido** | Via objetivos/pesquisa | Pós |
| 26 | **Voar de hipertubo / jetpack como transporte** | Mobilidade vertical | **Não trazer** | Ver #4 e A3d #17 | — |

## A5. Qualidade de vida e interface

| # | Item | O que é | Rec. | Como / por quê | Fase |
|---|---|---|---|---|---|
| 1 | **Menu de construção por categorias + busca** | Grade de prédios, busca por texto | **Trazer parecido** | | MVP |
| 2 | **Atalhos (hotbar) de construção** | 1–0 | **Trazer parecido** | | MVP |
| 3 | **Tela da máquina com taxa por minuto** | Mostra entrada/saída/min e eficiência | **Trazer parecido** | | MVP |
| 4 | **Taxa visível no mundo (sem abrir a tela)** | Satisfactory **não** tem | **Criar novo** | D4: número flutuante/luz de status ao olhar (verde = ok, âmbar = falta entrada, vermelho reservado a alerta, D12) | MVP |
| 5 | **Estatísticas de produção globais** | Satisfactory **não** tem (só mods) | **Criar novo** | **Painel de produção**: produzido/consumido por item, por minuto, na colônia inteira. Resposta direta a uma crítica comum | Pós (logo após MVP) |
| 6 | **Overclock/underclock** (1–250%, fragmentos acima de 100%) | Ajusta velocidade e energia (energia cresce ~exponencialmente) | **Adaptar** | Slider simples 50–150% (energia linear ou pouco acima). Acima de 100% com "núcleo de sobrecarga" é opcional (A1 #10) | Pós |
| 7 | **Pausa de máquina / standby** | Liga/desliga | **Trazer parecido** | Casado com prioridade de energia | MVP |
| 8 | **Mapa com camadas, ícones e nós descobertos** | Mapa geral | **Trazer parecido** | Nosso terreno real é o próprio mapa (D8) | MVP (simples) |
| 9 | **Bússola com marcadores** | HUD | **Trazer parecido** | Importante no mapa grande (D8) | MVP |
| 10 | **Salvamento automático e múltiplos slots** | | **Trazer parecido** | D13 (save/load) | MVP |
| 11 | **Mensagens/rádio da ADA** | Voz guia | **Adaptar** | Voz do **controle da missão na Terra** com atraso de comunicação (tema) | Pós |
| 12 | **Pausa de verdade em single-player** (1.2) | | **Trazer parecido** | Tick fixo facilita (D5) | MVP |
| 13 | **Suporte a controle** (1.1) | | **Trazer parecido** (tarde) | Planejar input com rebind desde o começo | Pós |
| 14 | **Clima dinâmico (chuva, 1.2)** | Só visual | **Adaptar** | Nossa tempestade de poeira tem **efeito de jogo** (D10), previsão com dias | MVP |
| 15 | **Codex / receitas / wiki no jogo** | Consulta de receitas | **Trazer parecido** | "Onde uso isto / como faço isto" num clique | Pós |
| 16 | **Otimização como diversão** (proporções, "números redondos") | Comunidade faz planilhas | **Adaptar** | Receitas com **proporções redondas** (1:2, 2:3) para caber de cabeça. Sem obrigar calculadora externa | MVP (dados) |

## A6. O que os jogadores elogiam e criticam

### Elogios (o que torna a fábrica "divertida")
- **Escala vista em primeira pessoa**: andar embaixo da própria fábrica e ver tudo funcionando. É o pilar 2 (D9).
- **Esteiras cheias de itens visíveis**: o jogador "vê" a produção e o gargalo (espaço vazio na esteira).
- **Otimização**: proporções, receitas alternativas, overclock — profundidade opcional.
- **Construção livre e bonita**: fundações, zoop, blueprints, cores → fábricas "de mostrar".
- **Exploração recompensada**: nós puros longe, discos rígidos, lesmas.
- **Sem pressão**: poucas ameaças; o jogador define o ritmo (bate com D9 "não é sobrevivência hardcore").

### Críticas (o que evitar)
- **Fim de jogo tedioso e repetitivo**: construir a mesma linha várias vezes; "só construir mais máquinas e esperar". → blueprints/copiar-colar cedo, metas de colônia variadas.
- **Espaguete de esteiras** e dificuldade de coordenar fábricas espalhadas. → trilho legível, cores por produto, teleférico/drones para ligar complexos.
- **Sem visão global de produção** (depende de mods e calculadoras externas). → painel de produção (A5 #5).
- **Fluidos confusos** (altura, pressão, buffers). → canos sem física de altura (A3d #11).
- **Movimentação lenta no fim**. → rover e rotas; mapa maior exige atalhos de viagem, mas **sem portal**.
- **Criaturas incomodando** e sem valor de jogo para quem quer construir (muitos jogam no modo "sem inimigos"). → D9 já resolve.

### Leve vs pesado — onde cortar
| Satisfactory (pesado) | Nosso jogo (mais leve) |
|---|---|
| 6 níveis de esteira, 3 de minerador, 3 de cano | 3 / 2 / 1 |
| ~11 máquinas de produção | ~5–6 no MVP (D13), ~8 no total |
| Cadeias de 10+ etapas (ex.: Ballistic Warp Drive) | Cadeias de 3–5 etapas; profundidade vem da colônia e da terraformação |
| Física de fluido e sinais de trem | Vazão simples; trem sem sinais |
| Energia com desarme total | Cortes automáticos por prioridade |
| A fábrica é o objetivo | A fábrica **serve** a colônia e a terraformação (D3) |

---

# Parte B — Logística que não parece Satisfactory

## B1. Por que a esteira do Satisfactory é tão reconhecível
Faixa plana larga, cinza/amarela, apoiada em postes, com itens individuais soltos em fila contínua, elevadores de esteira em espiral e splitters/mergers cúbicos. Qualquer esteira plana com itens soltos vai lembrar Satisfactory (ou Factorio). Para ser diferente, precisa mudar **pelo menos duas** destas coisas: forma do suporte, forma do "contêiner" do item, ritmo do movimento (contínuo × em pacotes) e som.

## B2. O que existe (real, ficção e outros jogos)

### Outros jogos
| Jogo | Logística | O que aproveitar |
|---|---|---|
| **Factorio** | Esteira de 2 faixas + braços (inserters), trens com sinais, robôs logísticos | Robôs de construção/entrega como fim de jogo; braço dá "vida" ao movimento |
| **Dyson Sphere Program** | Esteiras + "sorters" + torres logísticas com drones e naves interplanetárias | Torre logística = oferta/demanda automática entre estações (modelo para drones) |
| **Captain of Industry** | Esteiras, canos, **caminhões** que entregam por demanda, **canal de metal fundido** | Canal fundido: logística específica por tipo de material; caminhões para cargas pequenas |
| **Mindustry** | Esteiras, pontes, **mass driver** (canhão de itens), **plastanium conveyor** (anda em **lotes**) | Transporte em **lote** em vez de item a item — base do Trilho de Caçambas |
| **Shapez 2** | Esteiras, **space belts** de várias faixas, **trens em pacotes** | Carregador que enche um pacote e só despacha cheio |
| **Techtonica** | Esteiras + **monotrilho** com depósitos e "haulers"; o jogador pode andar no trilho (railrunner) | Monotrilho com estações; jogador usar a infraestrutura como transporte |
| **Foundry** | Esteiras em voxel, trens | — |
| **Astroneer** | Sem esteira: **trilhos com vagonetes**, sondas de carga automáticas, cabos de energia | Vagonete em trilho simples com caixotes visíveis |
| **Oxygen Not Included** | **Trilho de transporte** com "caixinhas" que correm; tubos de gás/líquido | Item em caixinha num trilho estreito: legível e barato |
| **Planet Crafter** | Sem esteira: extratores enchem baús; drones levam entre baús (fim de jogo) | Prova de que Marte "sem esteira" funciona, mas perde o espetáculo |
| **Surviving Mars** | Sem esteira: **drones** (raio do hub), **RC Transport**, **shuttles** entre cúpulas | Drones com raio de atuação e hub; rover de transporte automático |
| **Timberborn / Frostpunk** | Carregadores (castores/pessoas) e armazéns | Logística como consequência da mão de obra (colonos, D2) |

### Tecnologias reais
| Tecnologia | Como é na vida real | Relação com Marte |
|---|---|---|
| **Vagonetes de mina em trilho** | Carrinhos pequenos em trilho estreito, puxados por cabo ou locomotiva | Robusto, funciona com poeira, baixo atrito |
| **Teleférico de material / RopeCon (Doppelmayr)** | Cabo sobre torres carrega caçambas ou uma correia suspensa; ex.: 4,8 km, ~20 mil t/dia de minério de platina em Booysendal (África do Sul) | Passa por cima de relevo difícil sem mexer no chão; em 0,38 g as torres podem ficar mais longe |
| **Tubo pneumático de cápsulas (Sumitomo, Japão)** | Cápsulas com rodas (~1,8 t) empurradas por ar em tubo de ~1 m; 3,2 km para calcário desde 1980 | Tubo **fechado**: protege da poeira; ar fino marciano exige pressurizar o tubo (bom motivo para ser "tecnologia de meio de jogo") |
| **Transporte pneumático de regolito (NASA)** | Regolito levado por gás em tubo fechado, testado em gravidade reduzida | Estudo real para Lua/Marte: sistema fechado quase sem poeira |
| **Mineroduto (slurry)** | Minério moído + água bombeado por cano | Exige muita água → ruim no começo de Marte; bom tema pós-terraformação |
| **Nória / elevador de canecas** | Correia vertical com canecas | Vertical muito legível; clássico em silos e minas |
| **Maglev / trilho magnético** | Levitação e propulsão magnética | Sem atrito nem desgaste com poeira; ficção plausível de fim de jogo |

### Problemas de Marte que justificam o visual
- **Poeira fina e abrasiva** (e eletrostática): gasta rolamentos e correias expostas; cobre painéis. → sistemas fechados ou com poucas peças em contato.
- **Ar fino (~0,6% da Terra)**: não há resfriamento por ar; pneumático só funciona **dentro de tubo pressurizado**.
- **Frio extremo (até −80 °C à noite)**: borracha de correia endurece → justifica **trilho metálico** em vez de correia de borracha.
- **Gravidade 0,38 g**: estruturas mais leves e mais altas, vãos maiores entre torres; carga pesa menos.

## B3. Avaliação das alternativas

Critérios: **Visual** (quão diferente do Satisfactory) · **Sensação** (ver itens andando, vazão) · **Marte** (se encaixa com poeira/frio/0,38 g) · **Complexidade** na nossa simulação (grade + arrays, D5) · **Desempenho** · **Leitura em 1ª pessoa**. Nota de 1 (ruim) a 5 (ótimo); em complexidade, 5 = mais simples.

| Conceito | Como se vê | Visual | Sensação | Marte | Complex. | Desemp. | 1ª pessoa | Observação |
|---|---|---|---|---|---|---|---|---|
| **Trilho de Caçambas** (vagonetes pequenas em trilho baixo) | Trilho metálico único na altura da cintura; caçambinhas abertas com monte de minério/peças | 5 | 5 | 5 | 5 | 5 | 5 | Mesmo modelo da esteira atual (slot = caçamba com pilha pequena) |
| **Tubo Selado de Cápsulas** | Tubo translúcido/branco com anéis ciano; cápsula passa com "whoosh"; janelas | 5 | 3 | 5 | 4 | 5 | 3 | Itens escondidos → precisa de janelas e trechos transparentes |
| **Teleférico de Carga** | Torres altas, cabo, caçambas penduradas atravessando o relevo | 5 | 4 | 5 | 3 | 5 | 5 | Longa distância; contorna o problema do terreno irregular (D14) |
| **Monotrilho suspenso** (itens pendurados por baixo) | Viga no alto, ganchos com carga | 4 | 4 | 4 | 4 | 5 | 4 | Libera o chão; lembra linha de montagem de carro |
| **Transporte pneumático de granel** (pó dentro de cano) | Cano comum | 2 | 1 | 5 | 5 | 5 | 1 | Não se vê nada: vira "cano", perde o pilar 2 |
| **Mineroduto (slurry)** | Cano | 2 | 1 | 2 | 5 | 5 | 1 | Precisa de água; bom só tardio |
| **Maglev de fim de jogo** | Trilho liso com pods flutuando e luz ciano | 5 | 5 | 4 | 5 | 5 | 5 | Ótimo como **nível 3** do próprio Trilho de Caçambas |
| **Enxame de drones** | Drones voando entre portos | 4 | 3 | 3 | 3 | 3 | 3 | Ar fino dificulta hélice (Ingenuity voou, mas com pás enormes); ótimo para média distância, não para dentro da fábrica |
| **Robôs rastejantes / crawlers** | Robozinhos com carga andando no chão | 4 | 3 | 4 | 2 | 2 | 4 | Precisa de pathfinding por robô; caro com milhares de itens |
| **Braços robóticos em cadeia** | Braços passando item de um para outro | 3 | 4 | 3 | 4 | 4 | 5 | Lembra Factorio; bom como **peça de carga/descarga** das máquinas |
| **Contêineres modulares (pods)** | Contêiner padrão movido por guindaste/rover | 4 | 2 | 4 | 3 | 5 | 4 | Bom para trens/rovers (unidade de carga), não para fábrica |
| **Mass driver (canhão de itens)** | Lançador disparando cápsulas | 5 | 4 | 5 | 4 | 5 | 4 | 0,38 g e ar fino ajudam (real para lançar da Lua). Divertido, mas arriscado de parecer Mindustry; fim de jogo |

## B4. Três conceitos-assinatura

### 1. ⭐ Trilho de Caçambas (recomendado como logística principal)

**Visual.** Um **trilho metálico único** (perfil em "I" ou tubo) sustentado por **pés finos** na altura da cintura ou do joelho. Em cima correm **caçambinhas** abertas (≈ 40–60 cm) presas por um carrinho de rodas. Cada caçamba leva um **montinho visível** do material (minério ocre, lingotes empilhados, placas) — o jogador vê *o que* e *quanto* passa. Pintura branco/cinza com **luz ciano** em cada caçamba (D12). Caçamba vazia volta? **Não**: a caçamba descarrega na máquina e é "reciclada" visualmente (vira para baixo e some por baixo do trilho, como correia de retorno) — resolve o problema de caçambas vazias sem simular retorno.

**Sensação.** Movimento em **pacotes ritmados** ("tac-tac-tac" de rodas nas juntas) em vez de fluxo contínuo. Gargalo aparece como **caçambas paradas encostadas uma na outra**; falta de insumo como **trilho vazio**. Estações de carga/descarga com pequeno **braço basculante** que vira a caçamba na tremonha da máquina — o momento "satisfatório".

**Marte.** Trilho de aço não endurece no frio como correia de borracha; poucas peças em contato com poeira; em 0,38 g carrinhos leves e pés finos. **Mecânica opcional** (D10): tempestade de poeira reduz a velocidade de trilhos **descobertos** (ex.: −25%) até um drone/o jogador limpar, ou até cobrir o trecho com uma **capa** (upgrade barato). Dá um motivo para o Tubo Selado existir.

**Simulação.** Praticamente o que já existe: `Belt` é uma fila de ints por célula. Muda só que cada slot guarda `(itemId, count)` com `count ≤ capacidade da caçamba` (valor em `Data/`). Vazão = caçambas/s × itens por caçamba. Continua array de inteiros, determinístico, 1 célula por segmento (regra 8, D5). A caçamba **não é entidade** (sem ID): é dado dentro do trilho; a apresentação desenha uma malha por slot (GPU instancing).

**Níveis (máx. 3):** Trilho Mk1 (caçamba pequena, lenta) → Mk2 (caçamba maior) → **Maglev** (pods fechados flutuando, luz ciano, silencioso). A progressão muda o **visual** e o **som**, não só um número.

**Peças auxiliares no mesmo idioma:** agulha (divisor), junção (mescla), agulha com filtro, **nória** (elevador de caçambas vertical), estação de carga/descarga, placa de contagem.

**Por que mantém a satisfação do Satisfactory:** o jogador continua vendo cada lote de material andar, contando vazão pelo olho, caçando gargalo pela fila parada. **Por que não parece cópia:** trilho estreito em vez de faixa larga; caçamba com carga em vez de itens soltos; movimento em pulsos; basculamento na descarga; som de trilho; nória em vez de espiral.

### 2. Tubo Selado de Cápsulas (meio de jogo)

**Visual.** Tubo branco de ~50 cm com **anéis de luz ciano** que acendem quando uma cápsula passa; trechos de **vidro** (que a fábrica produz — liga com sílica/vidro) onde dá para ver a cápsula. Estações com escotilha que abre com sopro de ar.

**Sensação.** Mais rápido que o trilho e "fechado": som de **whoosh**, luz correndo pelo tubo. Menos espetáculo de itens, mais espetáculo de **luz e som**.

**Marte.** Pressurizado por dentro com CO₂ comprimido do ar (liga com o coletor atmosférico). **Imune à poeira e à tempestade**, que é o motivo de existir. Transporte pneumático fechado é linha real de pesquisa da NASA para regolito.

**Simulação.** Mesmo modelo do trilho (fila de slots) com velocidade maior e custo de energia por segmento. Nenhuma lógica nova.

**Papel.** Upgrade/alternativa **situacional**: ligações longas dentro da base e trechos críticos (suporte à vida) que não podem parar na tempestade. Não substitui o trilho: é caro (vidro + energia).

### 3. Teleférico de Carga (média/longa distância)

**Visual.** **Torres altas e finas** a cada 100–300 m (vão maior graças a 0,38 g), cabo duplo, **caçambas penduradas** cruzando por cima de mesas, do canyon (D15) e da borda da cratera. Visível de longe, cria silhuetas no horizonte (ajuda a ler a base no mapa grande, D8). Estação terminal com roda gigante de retorno do cabo.

**Sensação.** Ver a produção de uma mina distante chegar em fila pelo céu. Grande momento de "minha colônia cresce". Opcional: o jogador pode **se pendurar** numa caçamba para viajar (substitui zipline/hipertubo sem ser teletransporte).

**Marte.** Resolve o problema do **terreno real irregular** (D14): não precisa fundação nem terraplanagem entre torres. RopeCon/teleféricos de minério existem de verdade (km de extensão).

**Simulação.** Ligação **ponto a ponto** entre duas estações: fila de slots de comprimento = distância / espaçamento. Sem células intermediárias na grade (as torres só validam colisão com o terreno no posicionamento). Barato de simular e de desenhar.

**Papel.** Liga complexos (mina distante → base) **antes** dos drones e do trem da D4. Ordem sugerida: trilho (MVP) → teleférico → drones/rover de carga → trem.

## B5. Recomendação

- **Logística principal: Trilho de Caçambas** (MVP), com o Maglev como nível 3. É o de menor custo técnico (reaproveita `Belt`), o mais legível em 1ª pessoa e o mais distante visualmente da esteira do Satisfactory.
- **Tubo Selado** entra quando a tempestade de poeira (D10) passar a afetar a logística — cria escolha real ("barato e exposto" × "caro e protegido").
- **Teleférico** é a assinatura de paisagem: nenhum jogo do gênero usa, casa com o relevo real de Jezero e com a D8 (mapa grande, recursos longe).
- Para decidir: um teste visual rápido no Unity (cubo/caçamba simples em trilho) antes de mudar nomes na simulação. A mudança de dados (`count` por slot) é pequena e pode esperar essa validação.

**Perguntas para o Caio:**
1. Caçamba **aberta** (vê o minério) ou **pod fechado** com janela? A aberta mostra mais, o pod é mais "sci-fi".
2. Tempestade desacelerar trilhos descobertos: entra ou fica de fora (pode pesar)?
3. Teleférico com carona do jogador: sim ou não?

---

## Fontes

**Satisfactory — oficial e wiki**
- [Patch 1.0 — Official Satisfactory Wiki](https://satisfactory.wiki.gg/wiki/Patch_1.0)
- [Patch 1.1.0.0 — Official Satisfactory Wiki](https://satisfactory.wiki.gg/wiki/Patch_1.1.0.0)
- [Patch 1.2.0.0 — Official Satisfactory Wiki](https://satisfactory.wiki.gg/wiki/Patch_1.2.0.0)
- [Future content — Official Satisfactory Wiki](https://satisfactory.wiki.gg/wiki/Future_content)
- [Quantum Encoder — Official Satisfactory Wiki](https://satisfactory.wiki.gg/wiki/Quantum_Encoder)
- [Satisfactory 1.2 Update Out Now — Coffee Stain Group](https://coffeestain.com/news/satisfactory-1-2-update-out-now/)
- [Patch Notes 1.0 — Satisfactory Q&A](https://questions.satisfactorygame.com/post/66e0629a772a987f4a8a9842)
- [Satisfactory — Wikipedia](https://en.wikipedia.org/wiki/Satisfactory)
- [Satisfactory Roadmap 2026 — Supercraft](https://supercraft.host/article/satisfactory-roadmap-2026/)
- [Satisfactory 1.0 Review — Zap-Hosting](https://zap-hosting.com/en/blog/2024/11/satisfactory-1-0-review-everything-new/)

**Satisfactory — opinião dos jogadores**
- [End game is still so way too TEDIOUS — Steam](https://steamcommunity.com/app/526870/discussions/0/4849905062599261701/)
- [Late game and other thoughts — Steam](https://steamcommunity.com/app/526870/discussions/0/3820780544817559996/)
- [Satisfactory — Metacritic](https://www.metacritic.com/game/satisfactory/)

**Outros jogos**
- [Monorails? Yes! — Techtonica](https://techtonicagame.com/monorails-yes-introducing-techtonicas-monorail-system/)
- [Trains — Shapez 2 Wiki](https://shapez2.wiki.gg/wiki/Trains) · [Space Transport — Shapez 2 Wiki](https://shapez2.wiki.gg/wiki/Space_Belt)
- [Molten Channel — Captain of Industry Wiki](https://wiki.coigame.com/Molten_Channel)
- Factorio, Dyson Sphere Program, Mindustry, Astroneer, Oxygen Not Included, Planet Crafter, Surviving Mars, Timberborn, Frostpunk: conhecimento geral de jogo (sem página específica consultada).

**Tecnologia real**
- [RopeCon — Doppelmayr](https://www.doppelmayr.com/en/systems/ropecon/)
- [RopeCon em Booysendal South — International Mining](https://im-mining.com/2019/02/25/doppelmayr-ropecon-suspended-conveyor-running-booysendal-south-platinum/)
- [Pneumatic capsule pipeline — Britannica](https://www.britannica.com/technology/pipeline-technology/Pneumatic-pipelines)
- [Capsule Pipelines for Aggregate Transport — Agg-Net](https://www.agg-net.com/resources/articles/transport-distribution/capsule-pipelines-for-aggregate-transport)
- [Pneumatic Capsule Pipeline Developments — Tim Howgego](https://timhowgego.wordpress.com/capsule/history/pcp_developments/)
- [Pneumatic Regolith Transfer Systems for ISRU — NASA NTRS](https://ntrs.nasa.gov/api/citations/20110008766/downloads/20110008766.pdf)
- [Experimental Testing of a Pneumatic Regolith Delivery System — NASA NTRS](https://ntrs.nasa.gov/citations/20110014001)
- [Dust mitigation and regolith conveyance review — Acta Astronautica](https://www.sciencedirect.com/science/article/pii/S0094576522001965)
