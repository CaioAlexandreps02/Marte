# Terreno — exportar heightmap de Jezero para o Unity

`exportar_heightmap.py` gera o mapa de jogo 8×8 km (recorte "candidato B") a partir do relevo **real**
de Marte (DTM HiRISE 1 m do USGS; buracos preenchidos com o DTM CTX 20 m) e grava 64 tiles RAW
16-bit prontos para o Terrain Toolbox.

## Rodar

```bash
python exportar_heightmap.py                   # padrão: 8×8 tiles, exagero 2.0, saída em ./saida
python exportar_heightmap.py --help            # todas as opções
python exportar_heightmap.py --norte-primeiro  # RAW com a linha 0 = norte (aí usar Flip Vertically)
```

Precisa de Python 3.12 com `numpy scipy rasterio matplotlib pillow requests`.
A 1ª execução baixa ~280 MB do HiRISE (leitura por HTTP Range, só as linhas do recorte) e ~10 MB do CTX
para `cache/` (≈6 min). Depois disso roda em ~20 s. `cache/` e `saida/` ficam fora do git, exceto
`saida/metadata.json` e `saida/preview.png`.

## O que sai em `saida/`

| Arquivo | Conteúdo |
|---|---|
| `Jezero_x_z.raw` (64×) | 1025×1025 amostras, uint16 little-endian, sem cabeçalho (2,1 MB cada) |
| `metadata.json` | min/max, precisão, tamanho do terreno no Unity, nível da água, início do jogador, limites geográficos, fontes/citação |
| `preview.png` | hillshade com a grade de tiles, água em −2530 m e o ponto de início |
| `Jezero_mapa_16bit_4097.png` | mapa inteiro em PNG 16-bit (1 a cada 2 amostras), **norte em cima** — só para inspeção |

**Orientação:** `x` → leste, `z` → norte, tile `(0,0)` = canto **sudoeste**. Por padrão a linha 0 do
RAW é a borda **sul** (é assim que o Unity lê: linha 0 = z = 0), então **não** marcar Flip Vertically.
Com `--norte-primeiro` é o contrário.

**Bordas:** a grade global tem 8193×8193 amostras; o tile `(x,z)` usa as amostras
`[x·1024 … x·1024+1024]`, então tiles vizinhos compartilham a mesma linha/coluna de borda (sem costura).
O script confere isso e a ida-e-volta da codificação toda vez que roda.

**Alturas:** reais, sem exagero, com UM min/max global para todos os tiles
(`h = min_codificado_m + valor/65535 · faixa_m`, ver `metadata.json`). O exagero vertical entra só na
altura do terreno no Unity.

## Importar no Unity 6.3 (Terrain Toolbox)

1. Package Manager → instalar **Terrain Tools** (`com.unity.terrain-tools`).
2. `Window → Terrain → Terrain Toolbox` → aba **Create New Terrain**.
3. Configurações (valores em `metadata.json → unity`):
   - **Total Terrain Width / Length:** 8000 · **Tiles X / Z:** 8 / 8 (cada tile fica com 1000 m)
   - **Terrain Height:** `terrain_size.y` (= faixa × exagero; com exagero 2.0 → 1562 m)
   - **Heightmap Resolution:** 1025
   - **Start Position:** (0,0,0) — ou (−4000, 0, −4000) para a origem ficar no centro do mapa
4. **Import Heightmap** ligado → **Heightmap Mode: Batch** → adicionar os 64 `Jezero_x_z.raw`
   (o Toolbox associa pelo sufixo `_x_z`, índice X depois Z, começando em 0).
   - RAW: **16 bit**, byte order **Windows** (little-endian), **Flip Vertically desmarcado**.
   - **Height Remap:** 0 → 1 (não remapear; a escala vem do Terrain Height).
5. Create. Água: plano em `agua.y_mundo_com_exagero` (−2530 m → y = 124 com exagero 2.0).
   Início do jogador: `inicio_jogador` (x, z em metros no mapa; y já com exagero).

Alternativa sem Batch: modo **Tiles** (arrastar cada RAW no slot certo) ou importar tile a tile pelo
Inspector do Terrain (Import Raw, mesmas opções).

## Fonte e licença

USGS Astrogeology, Mars 2020 TRN — HiRISE DTM 1 m e CTX DTM 20 m, domínio público (CC0).
Citação em `metadata.json → fontes.citacao`.
