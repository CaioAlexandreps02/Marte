# Roadmap

> Ordem de trabalho até o MVP ("do pouso ao primeiro domo com colonos", D13) e o que precisa de design antes.
> Atualizar ao fim de cada sessão. Status: ✅ feito · 🔶 em andamento · ⬜ não começado · 📝 precisa de sessão de design.

## Fase 0 — Base técnica
| Item | Status | Onde |
|---|---|---|
| Decisões D1–D16, pilares, core loop, MVP | ✅ | DECISOES.md |
| Simulação C# (grade, tick 20/s, comandos, minerador/esteira/fundição/baú, save) + 7 testes | ✅ | Simulation/ |
| Projeto Unity 6.3 URP + MCP | ✅ | Unity/, .mcp.json |

## Fase 1 — Andar no terreno real (D13 passo 1) 🔶
| Item | Status |
|---|---|
| Pipeline do terreno real (HiRISE/CTX/MOLA), 28×25 km | ✅ |
| Streaming, horizonte, fundo, floating origin, limite do mapa, céu e névoa | ✅ |
| Jogador 1ª pessoa (andar, correr, voo de teste) | ✅ |
| Ajustes finos de relevo (mais suavizações/platôs, mesas de Gale, emendas CTX) | 🔶 contínuo |
| **Edições D15/D16 no pipeline** (Variante A + corredor, canyon diagonal, poços, mesas, base nivelada, trilha do Mirante, início no pad) | 🔶 feito no pipeline, falta regenerar tiles + reimportar no Unity (PC Xeon) |
| Marcadores de marcos no Unity a partir de `ferramentas/terreno/marcos.json` (editor script `Marte/...`) | ⬜ |
| **Cavernas** como malhas (entrada + interior modular/cena aditiva) + **Terrain Holes** por editor script, reaplicados a cada import; 1º protótipo: Abrigo do Terraço (#37, tutorial) | ⬜ |
| Campos de pedras da base (pad só cascalho, normal na zona, denso na transição e no pé da Mesa do Terraço) | ⬜ |
| Aviso "sinal da base fraco" no corredor da trilha (medir até a antena do Mirante ou desligar no corredor) | ⬜ |
| **Texturas do terreno** (MicroSplat Core + módulo URP 6.3, paleta D12, pintura por inclinação/altura) | ⬜ |
| Pedras e detalhes espalhados (Poly Haven CC0, espalhamento por script) | ⬜ |
| Água de verdade (shader, reflexo do céu certo) | ⬜ |
| Teste de desempenho do streaming em movimento (rover-speed) | ⬜ |

## Fase 2 — Fábrica com cubos (D13 passo 2)
Já existe a lógica em `Simulation/`; falta a ponte com o Unity.
| Item | Status |
|---|---|
| Ponte Simulation ↔ Unity (host local, tick 20/s, Unity só lê estado e envia comandos) | ⬜ |
| Coletar à mão (minério → inventário) | ⬜ |
| Colocar/girar/remover minerador, esteira, fundição, baú (cubos) | ⬜ |
| Itens visíveis nas esteiras (arrays, sem objeto por item) | ⬜ |
| Grade de construção sobre o terreno real (célula da simulação ↔ posição no mundo) | ⬜ |
| 📝 **Recursos de Marte** (lista final do MVP: gelo/regolito/ferro/sílica "a definir") | 📝 D13 |

## Fase 3 — Fundações (D13 passo 3, D14 camada 1)
| Item | Status |
|---|---|
| Fundações auto-niveladoras (pernas até o chão) | ⬜ |
| Overlay de inclinação verde/amarelo/vermelho (faixas em `Data/`) | ⬜ |

## Fase 4 — Sobrevivência e ambiente (D13 passo 4, D10)
| Item | Status |
|---|---|
| Traje: O₂ e energia, recarga na base/veículo/posto | ⬜ |
| Morte → reaparece na base perdendo o inventário | ⬜ |
| Energia solar | ⬜ |
| 1 tempestade de poeira (menos sol, visibilidade, previsão) | ⬜ |
| HUD do traje (inclui o aviso de "sinal da base" do limite do mapa) | ⬜ |

## Fase 5 — Cadeia até o domo e colonos (D13 passo 5)
| Item | Status |
|---|---|
| 5–6 máquinas + 1 cadeia completa até o domo | ⬜ |
| 1 domo + 5 colonos como números (necessidades, vagas) | ⬜ |
| 1 medidor de terraformação (sem visual) | ⬜ |
| Rover simples (3ª pessoa) | ⬜ |
| 📝 **Cadeias de produção e lista de peças** | 📝 D4/D11 |
| 📝 **Suprimentos da Terra** (referência Surviving Mars) | 📝 D11 |

## Fase 6 — Save/load (D13 passo 6)
| Item | Status |
|---|---|
| Save/load do estado da simulação (já existe em `Simulation/`) + posição do jogador + edições de terreno | ⬜ |

## Fase 7 — Arte básica (D13 passo 7)
| Item | Status |
|---|---|
| 📝 **Art bible** (paleta D12, referências `referencias/estilo/`) | 📝 D12 |
| Modelos básicos de máquinas, domo, traje (braços + ferramenta) | ⬜ |

## Sessões de design pendentes
Ordem sugerida pelo que bloqueia a implementação primeiro:
1. **Recursos de Marte** — bloqueia a fase 2 (dá pra começar com os placeholders de `Data/`). Base: `referencias/recursos-marte-pesquisa.md`.
2. **Cadeias de produção e lista de peças** — bloqueia a fase 5.
3. **Suprimentos da Terra** — fase 5.
4. **Pesquisa / árvore de tecnologia** — pós-MVP (no MVP basta a cadeia até o domo).
5. **Terraformação (ciência e medidores)** — MVP só precisa de 1 medidor.
6. **História** — importante para a demo (crítica ao 687 Days on Mars), não bloqueia código.
7. **Art bible** — antes da fase 7.
8. **Nome do jogo** — candidatos citados: Solum Mars / New Mars / Terra Mars.

## Pendências técnicas soltas
- CPU-Z no PC Xeon (D6) → decidir upgrade de RAM.
- Emendas dos DTMs CTX do catálogo (linhas retas fracas no norte/nordeste).
- Plugin oficial `unity-agent-plugin` (opcional).
- Git: configurar autor e acesso da conta CaioAlexandreps02 nesta máquina.
