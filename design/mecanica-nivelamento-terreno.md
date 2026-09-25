# Mecânica de nivelamento de terreno

> Registrada em 24/09/2026 a partir da ideia do Caio (texto original: "MECÂNICA DE NIVELAMENTO DE TERRENO").
> Resumo da decisão: [DECISOES.md](../DECISOES.md) D14. Status: **implementação futura**, camada 1 entra no MVP.

## Contexto

Ao testar o mapa na prática, o relevo real de Marte ficou bem ondulado. Mesmo com as áreas suavizadas no
pipeline (`ferramentas/terreno/edicoes.json`: platôs e suavizações), **sempre vai sobrar irregularidade**,
porque a base é dado real. O jogador precisa de uma forma de construir em chão irregular sem que isso vire um
obstáculo chato.

Pilares envolvidos (D9): **fábricas que você vê e entende** (automação é o coração; informação sempre clara na
tela) e **uma colônia pra cuidar** (tudo é construído pra gente viver).

## Ideia central

Terraplanagem não é só um pré-requisito: **o material escavado vira recurso** (regolito, que entra na cadeia de
produção). "Preciso nivelar" vira "vou nivelar **e** ganho material".

> Nome do recurso em aberto: "Regolito" vai ser renomeado (finalistas **Basalto** e **Solo Marciano**, ver
> notas de recursos no DECISOES.md). Aqui fica "regolito" até a decisão.

## Camada 1 — Fundações auto-niveladoras (MVP)

- Cada fundação tem "pernas" que descem até o terreno; a peça fica sempre nivelada, na altura escolhida.
- Resolve o problema imediato: sem isso o jogador trava na primeira construção.
- Já previsto no D8 ("fundações/plataformas que nivelam o chão") e na ordem do MVP (D13, passo 3).
- **Técnico:** a fundação guarda na simulação só a posição, a rotação e a **altura** (inteiro, D5); as pernas
  são apresentação (o Unity mede o terreno embaixo e estica a malha). Não altera o terreno.

## Camada 2 — Ferramenta de terraplanagem manual (meio de jogo)

Ferramenta ou veículo para achatar uma área de verdade antes de algo grande (ex: o domo):

- **Prévia** da área final (grade verde/vermelha: onde corta, onde aterra).
- Mostra o **volume** de terra a mover antes de confirmar.
- Custa **energia proporcional ao volume**: é uma escolha real (nivelar aqui ou procurar um platô natural?).
- **Cortar** gera regolito coletável; **aterrar** consome regolito do estoque.

## Camada 3 — Automação da terraplanagem (fase tardia)

- **Drone de terraplanagem** (não "terraformador", para não confundir com a terraformação do planeta, D3):
  o jogador marca uma área e o drone nivela sozinho com o tempo, gastando energia armazenada.
- Coerente com o pilar de automação e com o D10 (drones automatizam manutenção mais tarde).
- Recompensa de progresso: no começo nivela na mão, depois automatiza.

## Posicionar construções conforme a elevação

O posicionamento mostra antes de confirmar o que é possível:

- **Overlay de inclinação:** verde = encaixa sem terraplanagem; amarelo = precisa nivelar um pouco; vermelho =
  inclinação grande demais mesmo com fundação auto-niveladora.
- Encaixa direto no pilar "informação sempre clara na tela".
- **Faixas (a definir e ajustar em teste):** proposta inicial verde ≤ 5°, amarelo 5–15°, vermelho > 15°,
  medidas **no jogo** (o terreno usa exagero vertical 2×, D8, então as inclinações no jogo são maiores que as
  reais). Os valores ficam em `Data/`, não no código.

## Ordem de implementação

1. Fundações auto-niveladoras (resolve o problema visto no teste).
2. Overlay de inclinação (barato e ajuda muito a ler o terreno).
3. Ferramenta manual de terraplanagem com custo de energia + regolito.
4. Drone de terraplanagem (depois do MVP).

## Restrições técnicas (D5 — base pronta pra co-op)

Valem a partir da camada 2 (a camada 1 não mexe no terreno):

- **Toda alteração de terreno é um comando** (`TerraformAreaCommand` ou similar: área, altura alvo) validado pela
  simulação; nada altera o heightmap direto.
- **O estado guarda as alterações**, não o Unity: uma camada de ajustes de altura por cima do terreno base,
  em inteiros (ex: centímetros) numa grade fixa (ex: 1 m), só onde houve edição. Mesmo formato no save e no
  sync de rede futuro. O terreno base continua vindo dos tiles gerados pelo pipeline.
- **Determinismo:** volume, custo de energia e regolito gerado calculados em inteiros/ponto fixo.
- **Streaming:** quando um tile volta a carregar, o Unity reaplica os ajustes daquela área antes de mostrar;
  o colisor precisa ser atualizado junto. O horizonte/fundo de baixa resolução pode ignorar ajustes pequenos.
- **Balanceamento em `Data/`:** faixas de inclinação, energia por m³, regolito por m³, velocidade do drone.

## Em aberto

- Nome do recurso escavado (regolito → Basalto ou Solo Marciano).
- Nome do jogo: o texto original cita "Solum Mars / New Mars / Terra Mars" — ainda não decidido em nenhum documento.
- Limite de área por operação e se aterrar exige material específico (ex: regolito compactado).
- Se a ferramenta manual é item de mão, veículo, ou os dois em fases diferentes.
