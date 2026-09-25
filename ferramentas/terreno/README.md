# Terreno — mapa real de Jezero para o Unity

Dois scripts geram o terreno a partir do relevo **real** de Marte:

| Script | Saída |
|---|---|
| `exportar_heightmap.py` | Mapa jogável em tiles RAW 16-bit de 1 km (1025×1025), hoje **28×25 km** |
| `exportar_fundo.py` | Terreno de **fundo só visual** de 100×100 km em volta (roda depois do anterior) |

## Configuração

- **`mapa.json`** — tamanho (`tiles_x`, `tiles_z`), canto sudoeste, nível da água (−2560 m), exagero vertical (2×),
  **ponto de início exato** (`inicio_km`, pad de pouso da base, D16), **área jogável** (polígono: Variante A + corredor
  da Trilha do Mirante, D15) e parâmetros do fundo.
- **`edicoes.json`** — edições feitas à mão, reaplicadas a cada geração **nesta ordem** (`aplicar_edicoes`):

  | # | Tipo | O que faz | Parâmetros |
  |---|---|---|---|
  | 1 | `suavizacoes` | reduz a ondulação dentro de um polígono | `poligono_km`, `escala_m`, `manter`, `transicao_m` |
  | 2 | `nivelamentos` | **(novo, D16)** ajusta um plano ao polígono, guarda parte da inclinação e da ondulação; transição para **fora** | `poligono_km`, `inclinacao` (fração da inclinação do plano), `manter` (fração da ondulação), `transicao_m` |
  | 3 | `mesas` | **(novo)** soma relevo com a forma de um morro real (stamp do mosaico CTX 20 m, hoje a Kodiak) | `x_km`, `z_km`, `somar_m`, `base_raio_m`, `rotacao_graus`, `fonte_km`, `fonte_raio_m`, `topo_plano` (corta o pico → topo plano) |
  | 4 | `pocos` | **(novo, D15)** poço de colapso: fundo plano + paredes íngremes, borda irregular | `x_km`, `z_km`, `raio_m`, `profundidade_m`, `fundo` (fração do raio), `irregularidade`, `semente` |
  | 5 | `canyons` | escava um vale real (stamp de DTM HiRISE), girado, esticado e com as pontas afinando | `fonte_url`, `de_km`, `ate_km`, `largura_km`, `profundidade_m`, `afinar_pontas_km` |
  | 6 | `trilhas` | **(novo, D15)** leito plano ao longo de uma polilinha; perfil suavizado e **cortado** (rampa escavada) onde passa do limite | `polilinha_km`, `largura_m`, `transicao_m`, `suavizar_m`, `max_inclinacao_jogo_graus` |
  | 7 | `platos` | nivela uma área circular com borda irregular; `altura_m: null` = mediana do terreno já editado | `x_m`, `z_m`, `raio_m`, `transicao_m`, `altura_m`, `detalhe`, `irregularidade`, `semente` |

  Por que essa ordem: forma grande primeiro; mesas depois do nivelamento (a transição não achata a mesa); o que cava soma
  diferença ao terreno já moldado; a trilha segue o terreno final; platôs por último (pad da base e cume com altura exata).
- **`marcos.json`** — lista dos marcos (D15/D16: 37 numerados + base, início, início da trilha, pouso da missão anterior)
  com tipo, origem (real/jogo), caverna/gelo e coordenadas de referência, para o Unity pôr marcadores. Manter em sincronia
  com `design/proposta-marcos-e-cavernas.md`.
- **Coordenadas de referência:** edições, início, área jogável e marcos usam metros/km a partir do canto sudoeste do mapa
  25×25 original (`mapa.json → referencia`). Assim, crescer ou deslocar o mapa não tira nada do lugar.
- **Tamanho continua 28×25** (a proposta sugeria 28×22 para a Variante A): com 22 o norte do limite (z = 21) teria só
  1 km de tiles e o streaming (raio 2,5 km) mostraria o fundo de 100 m logo ali; e mudar `tiles_z` mexe no cos(lat) do
  centro (desloca o leste do mapa ~4 m). Os tiles a mais só custam disco/geração.
- **Autoverificação das edições** (`verificar_edicoes`, vai para `metadata.json → verificacao_edicoes`, só avisa):
  nivelamento com inclinação mediana ≤ 1,5° no jogo e chão ≥ água + 50 m; ganho do cume das mesas; inclinação máxima
  da trilha no jogo (passo 5 m).

## Fontes (todas CC0 / domínio público, USGS)

| Onde | Fonte |
|---|---|
| Onde existe (~33% do 28×25) | HiRISE DTM 1 m, mosaico Mars 2020 TRN |
| Resto do mapa | CTX DTM 20 m, mosaico Mars 2020 TRN |
| Fora do mosaico CTX (norte) | DTMs CTX 20 m do catálogo STAC da USGS, cada um com o desvio vertical corrigido contra o mosaico |
| Canyon | DTM HiRISE 1 m das Hephaestus Fossae (catálogo STAC) |
| Mesas (stamp) | forma da Kodiak no mosaico CTX 20 m (o mesmo `cache/ctx_20m.tif`) |
| Fundo além de 8 km da borda | MOLA 463 m global |

Transições suaves: 30 m HiRISE→CTX, 500 m mosaico→catálogo, 3 km CTX→MOLA. Onde só há CTX o relevo é mais liso.

## Rodar

```bash
python exportar_heightmap.py     # ~9 min com os dados em cache (1ª vez ~25 min, baixa ~1,5 GB)
python exportar_fundo.py         # ~1 min
python preview_edicoes.py        # ~40 s, sem tiles: testa as edições (abaixo)
```

Python 3.12 com `numpy scipy rasterio matplotlib pillow requests`. O processamento é feito em faixas de 1 km; a grade
intermediária fica em `cache/grade_XxZ.npy` (mapeada em disco, ~2,9 GB). O HiRISE baixado é reaproveitado se a
janela nova couber num recorte já em cache. `cache/` e `saida/` ficam fora do git, exceto `saida/metadata.json`,
`saida/preview.png` e `saida/fundo_preview.png`.

### Preview das edições (qualquer PC)
`preview_edicoes.py` monta a grade a partir de `cache/ctx_20m.tif` (CTX 20 m; baixe rodando o exportador uma vez ou
copie o arquivo), aplica **todas** as edições com as **mesmas funções** do exportador e salva em `referencias/terreno/`:
`20_edicoes_aplicadas.png` (mapa inteiro), `21_base_depois.png` (base, 5 m) e `22_trilha_do_mirante.png` (trilha, 2 m +
perfil). Imprime a mesma autoverificação. Na 1ª vez baixa o stamp do canyon (~94 MB) para `cache/`. O CTX é mais liso
que o HiRISE do jogo: os números valem como estimativa; os do exportador (em `metadata.json`) valem de verdade.

### Depois de mudar `mapa.json`/`edicoes.json` (PC com o cache completo)
1. `python exportar_heightmap.py` e `python exportar_fundo.py`. O stamp do canyon agora fica em cache pelo nome do
   arquivo da fonte: renomeie `cache/stamp_canyon_norte.npy/.json` para `cache/stamp_DTEEC_069071_2020_063847_2020_A01.npy/.json`
   para não baixar de novo.
2. Conferir no log/`metadata.json → verificacao_edicoes` (base ≤ 1,5°, ≥ 50 m acima da água; mesas; trilha) e o `preview.png`.
3. No Unity: **Marte → Terrain → Import Jezero** e depois **Marte → Scene → Setup World, Water and Player** (salvar a cena).

## Saída (`saida/`)

| Arquivo | Conteúdo |
|---|---|
| `Jezero_x_z.raw` | 1025×1025, uint16 little-endian, linha 0 = **sul**, sem cabeçalho |
| `metadata.json` | alturas, tamanho no Unity, água, início, **área jogável** (metros, origem no centro), deslocamento da referência, fontes usadas, fração HiRISE por tile, fundo, edições e `verificacao_edicoes` |
| `preview.png` | sombreado com grade de tiles, água, área jogável (vermelho), início, platôs, nivelamento e trilha |
| `fundo.raw` / `fundo_preview.png` | fundo 1001×1001 a 100 m, origem no centro do mapa |
| `Jezero_mapa_16bit.png` | mapa inteiro em PNG 16-bit, norte em cima (inspeção) |

**Orientação:** `x` → leste, `z` → norte, tile `(0,0)` = canto sudoeste. Tiles vizinhos compartilham a borda; o
script confere bordas e ida-e-volta da codificação a cada execução.
**Alturas:** reais, um min/max global (`h = min_codificado_m + valor/65535 · faixa_m`); o exagero entra no Unity.

## Importar no Unity
`Marte → Terrain → Import Jezero` e depois `Marte → Scene → Setup World, Water and Player` (ver `Unity/README.md`).

## Citação
Fergason et al. (2020), Mars 2020 TRN HiRISE/CTX DTMs; USGS MRO CTX/HiRISE controlled DTMs (STAC); Mars MGS MOLA DEM
463 m. Textos completos em `metadata.json → fontes`.
