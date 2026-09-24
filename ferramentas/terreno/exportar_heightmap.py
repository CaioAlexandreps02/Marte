"""Exporta o relevo real de Jezero (Marte) em tiles de heightmap RAW 16-bit para o Unity.

Fontes (USGS, dominio publico / CC0):
  - HiRISE DTM 1 m  (Mars 2020 TRN)  -> relevo principal
  - CTX DTM 20 m    (Mars 2020 TRN)  -> preenche buracos (NaN) do HiRISE

Uso:  python exportar_heightmap.py [--saida DIR] [--exagero 2.0] [--tiles 8] [--norte-primeiro]
Detalhes e importacao no Unity: README.md desta pasta.
"""
import argparse, json, math, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import rasterio
import requests
from scipy.ndimage import affine_transform, distance_transform_edt, gaussian_filter, uniform_filter

AQUI = Path(__file__).resolve().parent
URL_HIRISE = ("https://asc-pds-services.s3.us-west-2.amazonaws.com/mosaic/mars2020_trn/HiRISE/"
              "JEZ_hirise_soc_006_DTM_MOLAtopography_DeltaGeoid_1m_Eqc_latTs0_lon0_blend40.tif")
URL_CTX = ("https://planetarymaps.usgs.gov/mosaic/mars2020_trn/CTX/"
           "JEZ_ctx_B_soc_008_DTM_MOLAtopography_DeltaGeoid_20m_Eqc_latTs0_lon0.tif")
R_MARTE = 3396190.0                       # esfera IAU Mars 2000 (CRS dos dois DTMs)
M_POR_GRAU = R_MARTE * math.pi / 180      # equiretangular lat_ts=0: metros projetados por grau
AMOSTRAS_TILE = 1024                      # 1025 amostras por tile, borda compartilhada
NIVEL_AGUA = -2530.0
CITACAO = ("Fergason, R.L., et al. (2020). Mars 2020 Terrain Relative Navigation Flight Product "
           "Generation: Digital Terrain Model and Orthorectified Image Mosaics. 51st LPSC, abstract #2020. "
           "USGS Astrogeology Science Center. Dados de dominio publico (CC0 / USGS).")


def baixar_ctx(cache):
    p = cache / "ctx_20m.tif"
    if not p.exists():
        print("baixando CTX 20 m ...")
        r = requests.get(URL_CTX, timeout=300); r.raise_for_status(); p.write_bytes(r.content)
    return p


def ler_hirise(cache, r0, r1, c0, c1):
    """Le linhas [r0,r1) x colunas [c0,c1) do HiRISE via HTTP Range (o TIFF e em faixas de 1 linha,
    nao e COG, entao ler janela pelo GDAL e lento). Resultado em cache como .npy."""
    p = cache / f"hirise_{r0}_{r1}_{c0}_{c1}.npy"
    if p.exists():
        return np.load(p)
    with rasterio.open("/vsicurl/" + URL_HIRISE) as d:
        assert d.block_shapes[0] == (1, d.width) and d.dtypes[0] == "float32"
        offs = [int(d.get_tag_item(f"BLOCK_OFFSET_0_{r}", "TIFF", bidx=1)) for r in range(r0, r1)]
    sess = {}
    def linha(i):
        import threading
        s = sess.setdefault(threading.get_ident(), requests.Session())
        a, n = offs[i] + c0 * 4, (c1 - c0) * 4
        for k in range(6):
            try:
                r = s.get(URL_HIRISE, headers={"Range": f"bytes={a}-{a + n - 1}"}, timeout=60)
                if r.status_code == 206 and len(r.content) == n:
                    return np.frombuffer(r.content, "<f4")
            except requests.RequestException:
                pass
            time.sleep(1 + k)
        raise RuntimeError(f"falha lendo linha {r0 + i}")
    print(f"baixando HiRISE: {r1 - r0} linhas x {c1 - c0} colunas ...")
    with ThreadPoolExecutor(16) as ex:
        z = np.stack(list(ex.map(linha, range(r1 - r0))))
    z = np.where(z < -1e30, np.nan, z).astype(np.float32)
    np.save(p, z)
    return z


def hillshade(z, d, az=315, alt=40):
    gy, gx = np.gradient(z, d); gy = -gy
    sl = np.arctan(np.hypot(gx, gy)); asp = np.arctan2(-gx, gy); a = np.radians(360 - az + 90); e = np.radians(alt)
    return np.clip(np.sin(e) * np.cos(sl) + np.cos(e) * np.sin(sl) * np.cos(a - asp), 0, 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--saida", type=Path, default=AQUI / "saida")
    ap.add_argument("--cache", type=Path, default=AQUI / "cache")
    ap.add_argument("--exagero", type=float, default=2.0, help="exagero vertical sugerido (so vai no metadata)")
    ap.add_argument("--tiles", type=int, default=8, help="tiles por lado (1 km cada)")
    ap.add_argument("--margem", type=float, default=5.0, help="margem (m) abaixo do min e acima do max")
    ap.add_argument("--lat", type=float, default=18.4975, help="centro do mapa (graus N)")
    ap.add_argument("--lon", type=float, default=77.3761, help="centro do mapa (graus L)")
    ap.add_argument("--norte-primeiro", action="store_true",
                    help="grava a linha 0 do RAW = borda NORTE (usar com 'Flip Vertically' no Unity)")
    a = ap.parse_args()
    t0 = time.time()
    a.saida.mkdir(parents=True, exist_ok=True); a.cache.mkdir(parents=True, exist_ok=True)

    # ---- grade: N x N amostras cobrindo L x L metros de chao (Leste-Oeste corrigido por cos(lat)) ----
    N = a.tiles * AMOSTRAS_TILE + 1
    L = a.tiles * 1000.0
    d = L / (N - 1)                                        # espacamento em metros de chao
    cosl = math.cos(math.radians(a.lat))
    Xc, Yc = a.lon * M_POR_GRAU, a.lat * M_POR_GRAU        # centro em metros projetados
    Xw, Yn = Xc - L / 2 / cosl, Yc + L / 2                 # canto noroeste (projetado)
    limites = dict(oeste=Xw / M_POR_GRAU, leste=(Xc + L / 2 / cosl) / M_POR_GRAU,
                   sul=(Yc - L / 2) / M_POR_GRAU, norte=Yn / M_POR_GRAU)

    with rasterio.open("/vsicurl/" + URL_HIRISE) as h:
        th = h.transform                                   # 1 m, canto superior esquerdo
    # coordenada fracionaria (linha, coluna) no HiRISE do centro do pixel; margem p/ o filtro cubico
    fr = lambda Y: (th.f - Y) / -th.e - 0.5
    fc = lambda X: (X - th.c) / th.a - 0.5
    r0, r1 = int(fr(Yn)) - 4, int(fr(Yn - L)) + 6
    c0, c1 = int(fc(Xw)) - 4, int(fc(Xw + L / cosl)) + 6
    zh = ler_hirise(a.cache, r0, r1, c0, c1)
    buracos = np.isnan(zh)
    print(f"HiRISE janela {zh.shape}, buracos {buracos.mean() * 100:.3f}%")

    # ---- CTX reamostrado (bilinear) na grade do HiRISE e usado nos buracos, com transicao suave ----
    with rasterio.open(baixar_ctx(a.cache)) as c:
        zc, tc, nd = c.read(1).astype(np.float32), c.transform, c.nodata
    zc[(zc == nd) | ~np.isfinite(zc)] = np.nan
    zc = np.where(np.isnan(zc), np.nanmedian(zc), zc)
    # pixel HiRISE (i,j) -> pixel CTX: separavel, entao affine_transform com matriz diagonal
    ctx = affine_transform(zc, [th.a / tc.a, th.a / tc.a],
                           offset=[(tc.f - (th.f - (r0 + 0.5))) / -tc.e - 0.5, (th.c + c0 + 0.5 - tc.c) / tc.a - 0.5],
                           output_shape=zh.shape, order=1, mode="nearest").astype(np.float32)
    dif = zh[~buracos] - ctx[~buracos]
    print(f"HiRISE - CTX: media {dif.mean():.2f} m, desvio {dif.std():.2f} m")
    if buracos.any():
        w = np.clip(distance_transform_edt(~buracos).astype(np.float32) / 30.0, 0, 1)   # 30 m de transicao
        zh = np.where(buracos, ctx, zh * w + ctx * (1 - w))
        del w
    del ctx, zc

    # ---- reamostragem cubica (B-spline) para a grade do jogo; linha 0 = NORTE aqui ----
    z = affine_transform(zh, [d, d / cosl], offset=[fr(Yn) - r0, fc(Xw) - c0],
                         output_shape=(N, N), order=3, mode="nearest").astype(np.float32)
    del zh
    print(f"grade {N}x{N}, espacamento {d:.6f} m  ({time.time() - t0:.0f}s)")

    # ---- codificacao 16-bit com UM min/max global ----
    zmin, zmax = float(z.min()), float(z.max())
    hmin, hmax = math.floor(zmin - a.margem), math.ceil(zmax + a.margem)
    faixa = hmax - hmin
    u = np.round((z - hmin) / faixa * 65535).astype(np.uint16)
    sul = u[::-1]                                          # linha 0 = SUL (convencao do Unity: z=0)

    # ---- tiles Jezero_x_z.raw (x -> leste, z -> norte, (0,0) = sudoeste) ----
    for tz in range(a.tiles):
        for tx in range(a.tiles):
            t = sul[tz * 1024: tz * 1024 + 1025, tx * 1024: tx * 1024 + 1025]
            (t[::-1] if a.norte_primeiro else t).astype("<u2").tofile(a.saida / f"Jezero_{tx}_{tz}.raw")

    # ---- autoverificacao: bordas identicas entre vizinhos e ida-e-volta dentro de meio degrau ----
    def ler(tx, tz):
        t = np.fromfile(a.saida / f"Jezero_{tx}_{tz}.raw", "<u2").reshape(1025, 1025)
        return t[::-1] if a.norte_primeiro else t          # devolve sempre com linha 0 = sul
    passo = faixa / 65535
    for tz in range(a.tiles):
        for tx in range(a.tiles):
            t = ler(tx, tz)
            if tx + 1 < a.tiles: assert np.array_equal(t[:, -1], ler(tx + 1, tz)[:, 0]), (tx, tz, "leste")
            if tz + 1 < a.tiles: assert np.array_equal(t[-1, :], ler(tx, tz + 1)[0, :]), (tx, tz, "norte")
            ref = z[::-1][tz * 1024: tz * 1024 + 1025, tx * 1024: tx * 1024 + 1025]
            assert np.abs(hmin + t * passo - ref).max() <= passo / 2 + 1e-3, (tx, tz, "ida-e-volta")
    print("autoverificacao OK (bordas compartilhadas e ida-e-volta)")

    # ---- PNG 16-bit do mapa inteiro (reduzido p/ 4097^2, amostra sim/amostra nao; norte em cima) ----
    from PIL import Image
    Image.fromarray(u[::2, ::2]).save(a.saida / "Jezero_mapa_16bit_4097.png")

    # ---- ponto de inicio: mesma logica do estudo map8.py (grade ~4 m, fundo plano do lago seco) ----
    z4, d4 = z[::4, ::4], d * 4                            # 2049^2, linha 0 = norte
    n4 = z4.shape[0]
    zs = gaussian_filter(z4, 2); gy, gx = np.gradient(zs, d4)
    ms = uniform_filter(np.degrees(np.arctan(np.hypot(gx, gy))), 75)
    baixo = uniform_filter(((z4 < -2512) & (z4 > NIVEL_AGUA + 2)).astype(float), 75) > 0.999
    yy, xx = np.mgrid[0:n4, 0:n4]; X, Y = xx * d4 / 1000, (n4 - 1 - yy) * d4 / 1000
    i = np.unravel_index(np.argmin(np.where(baixo, ms + 0.4 * np.hypot(X - 7.0, Y - 2.2), 1e9)), z4.shape)
    sx, sz, sh = float(X[i]) * 1000, float(Y[i]) * 1000, float(z4[i])

    # ---- preview (hillshade + grade de tiles) ----
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, matplotlib.patheffects as pe
    from matplotlib.colors import LinearSegmentedColormap
    mars = LinearSegmentedColormap.from_list("mars", ["#2e1d14", "#5a3322", "#8a5233", "#b07a45", "#cfa46a", "#e6caa0", "#f4e6cc"])
    hs = hillshade(gaussian_filter(z4, 1), d4)
    img = np.clip(mars(((z4 - zmin) / (zmax - zmin)) ** 0.6)[..., :3] * (0.2 + 1.05 * hs[..., None]), 0, 1)
    km = a.tiles
    fig, ax = plt.subplots(figsize=(11, 11), dpi=100)
    ax.imshow(img, extent=[0, km, 0, km], interpolation="bilinear")
    ax.contour(np.flipud(z4), levels=[NIVEL_AGUA], extent=[0, km, 0, km], colors="#8fd0ff", linewidths=1.2)
    stroke = [pe.withStroke(linewidth=2, foreground="black")]
    for v in range(km + 1):
        ax.axhline(v, color="white", lw=.6, alpha=.6); ax.axvline(v, color="white", lw=.6, alpha=.6)
    for tz in range(km):
        for tx in range(km):
            ax.text(tx + .05, tz + .95, f"{tx}_{tz}", color="white", fontsize=8, va="top", path_effects=stroke)
    ax.plot(sx / 1000, sz / 1000, marker="*", ms=20, color="yellow", mec="black")
    ax.set_xlim(0, km); ax.set_ylim(0, km); ax.set_xticks(range(km + 1)); ax.set_yticks(range(km + 1))
    ax.set_xlabel("x (km, oeste -> leste)"); ax.set_ylabel("z (km, sul -> norte)")
    ax.set_title(f"Jezero - tiles Jezero_x_z.raw ({N}^2, 1 km cada) - {hmin} a {hmax} m\n"
                 f"azul: agua em {NIVEL_AGUA:.0f} m | estrela: inicio do jogador | (0,0) = sudoeste", fontsize=11)
    plt.tight_layout(); prev = a.saida / "preview.png"; plt.savefig(prev); plt.close(fig)
    Image.open(prev).convert("RGB").quantize(256, method=Image.Quantize.MEDIANCUT).save(prev, optimize=True)

    # ---- metadata ----
    norm = lambda h: (h - hmin) / faixa
    meta = {
        "arquivos": {"tiles": "Jezero_{x}_{z}.raw", "indice": "x = leste (0 = oeste), z = norte (0 = sul); (0,0) = canto sudoeste",
                     "formato": "RAW uint16 little-endian (Windows), 1025x1025, sem cabecalho",
                     "linha_0_do_raw": "NORTE (ativar Flip Vertically no Unity)" if a.norte_primeiro else "SUL (Unity padrao, sem Flip Vertically)",
                     "bordas": "tiles vizinhos compartilham a linha/coluna de borda (grade global 8193 -> tile = amostras [i*1024 .. i*1024+1024])",
                     "png_16bit": "Jezero_mapa_16bit_4097.png: mapa inteiro, 1 a cada 2 amostras, NORTE em cima (convencao de imagem)"},
        "grade": {"tiles_por_lado": a.tiles, "tamanho_tile_m": 1000.0, "amostras_por_tile": 1025, "amostras_global": N,
                  "espacamento_m": d, "tamanho_mapa_m": L},
        "altura": {"min_real_m": round(zmin, 3), "max_real_m": round(zmax, 3), "margem_m": a.margem,
                   "min_codificado_m": hmin, "max_codificado_m": hmax, "faixa_m": faixa,
                   "precisao_por_degrau_m": passo, "decodificar": "h_m = min_codificado_m + valor/65535 * faixa_m",
                   "alturas_reais_sem_exagero": True},
        "unity": {"terrain_size": {"x": 1000.0, "y": faixa * a.exagero, "z": 1000.0}, "heightmap_resolution": 1025,
                  "exagero_vertical": a.exagero,
                  "y_mundo": "y = (h_m - min_codificado_m) * exagero_vertical (terreno em y=0)",
                  "posicao_tile_origem_no_centro": f"tile (x,z) em ({{x}}*1000 - {L / 2:.0f}, 0, {{z}}*1000 - {L / 2:.0f})"},
        "agua": {"nivel_m": NIVEL_AGUA, "normalizado": norm(NIVEL_AGUA), "y_mundo_com_exagero": (NIVEL_AGUA - hmin) * a.exagero},
        "inicio_jogador": {"x_m": round(sx, 1), "z_m": round(sz, 1), "tile": [int(sx // 1000), int(sz // 1000)],
                           "altura_m": round(sh, 2), "normalizado": norm(sh), "y_mundo_com_exagero": (sh - hmin) * a.exagero,
                           "criterio": "menor inclinacao media em 300 m, fundo do lago entre agua+2 m e -2512 m, perto de (7,0; 2,2) km"},
        "geo": {"centro_lat": a.lat, "centro_lon": a.lon, "limites_graus": limites,
                "projecao": "Equiretangular Mars 2000 esfera (R=3396190 m, lat_ts=0); largura L-O corrigida por cos(lat do centro)",
                "correcao_cos_lat": cosl},
        "fontes": {"hirise_dtm_1m": URL_HIRISE, "ctx_dtm_20m": URL_CTX, "licenca": "Dominio publico (USGS / CC0)",
                   "citacao": CITACAO, "uso_ctx": "somente buracos NaN do HiRISE (transicao de 30 m)",
                   "hirise_menos_ctx_m": {"media": float(dif.mean()), "desvio": float(dif.std())},
                   "buracos_hirise_pct": float(buracos.mean() * 100)},
        "reamostragem": "B-spline cubica (scipy affine_transform order=3) a partir do HiRISE 1 m",
    }
    (a.saida / "metadata.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: meta[k] for k in ("altura", "agua", "inicio_jogador")}, indent=1, ensure_ascii=False))
    print(f"limites: {limites}\npronto em {time.time() - t0:.0f}s -> {a.saida}")


if __name__ == "__main__":
    main()
