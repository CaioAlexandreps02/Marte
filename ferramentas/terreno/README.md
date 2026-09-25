# Terreno — mapa real de Jezero para o Unity

Dois scripts geram o terreno a partir do relevo **real** de Marte:

| Script | Saída |
|---|---|
| `exportar_heightmap.py` | Mapa jogável em tiles RAW 16-bit de 1 km (1025×1025), hoje **28×25 km** |
| `exportar_fundo.py` | Terreno de **fundo só visual** de 100×100 km em volta (roda depois do anterior) |

## Configuração

- **`mapa.json`** — tamanho (`tiles_x`, `tiles_z`), canto sudoeste, nível da água (−2560 m), exagero vertical (2×),
  alvo do ponto de início, **área jogável** (polígono) e parâmetros do fundo.
- **`edicoes.json`** — edições feitas à mão, reaplicadas a cada geração:
  - `suavizacoes`: reduz a ondulação dentro de um polígono (`manter` = fração que sobra, `escala_m` = tamanho do que é suavizado);
  - `canyons`: escava um vale real (stamp de DTM HiRISE), girado, esticado e com as pontas afinando;
  - `platos`: nivela uma área circular com borda irregular.
- **Coordenadas de referência:** edições, início e área jogável usam metros/km a partir do canto sudoeste do mapa
  25×25 original (`mapa.json → referencia`). Assim, crescer ou deslocar o mapa não tira nada do lugar.

## Fontes (todas CC0 / domínio público, USGS)

| Onde | Fonte |
|---|---|
| Onde existe (~33% do 28×25) | HiRISE DTM 1 m, mosaico Mars 2020 TRN |
| Resto do mapa | CTX DTM 20 m, mosaico Mars 2020 TRN |
| Fora do mosaico CTX (norte) | DTMs CTX 20 m do catálogo STAC da USGS, cada um com o desvio vertical corrigido contra o mosaico |
| Canyon | DTM HiRISE 1 m das Hephaestus Fossae (catálogo STAC) |
| Fundo além de 8 km da borda | MOLA 463 m global |

Transições suaves: 30 m HiRISE→CTX, 500 m mosaico→catálogo, 3 km CTX→MOLA. Onde só há CTX o relevo é mais liso.

## Rodar

```bash
python exportar_heightmap.py     # ~9 min com os dados em cache (1ª vez ~25 min, baixa ~1,5 GB)
python exportar_fundo.py         # ~1 min
```

Python 3.12 com `numpy scipy rasterio matplotlib pillow requests`. O processamento é feito em faixas de 1 km; a grade
intermediária fica em `cache/grade_XxZ.npy` (mapeada em disco, ~2,9 GB). O HiRISE baixado é reaproveitado se a
janela nova couber num recorte já em cache. `cache/` e `saida/` ficam fora do git, exceto `saida/metadata.json`,
`saida/preview.png` e `saida/fundo_preview.png`.

## Saída (`saida/`)

| Arquivo | Conteúdo |
|---|---|
| `Jezero_x_z.raw` | 1025×1025, uint16 little-endian, linha 0 = **sul**, sem cabeçalho |
| `metadata.json` | alturas, tamanho no Unity, água, início, **área jogável** (metros, origem no centro), deslocamento da referência, fontes usadas, fração HiRISE por tile, fundo |
| `preview.png` | sombreado com grade de tiles, água, área jogável (vermelho), início e platôs |
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
