"""Gera o terreno de FUNDO (so visual, sem colisao) em volta do mapa jogavel, com relevo real.

  - ate `ctx_margem_km` alem da borda: CTX 20 m (mesma base do mapa), reduzido para a grade do fundo
  - mais longe: MOLA 463 m global (USGS, CC0), com desvio vertical alinhado ao CTX
  - dentro do mapa: a propria grade do jogo (a borda casa exatamente com o terreno jogavel)

Roda depois de exportar_heightmap.py (usa cache/grade_NxN.npy e saida/metadata.json).
Grava saida/fundo.raw (uint16, linha 0 = SUL) e acrescenta a secao "fundo" no metadata.json.
Uso:  python exportar_fundo.py
"""
import json, math, time
from pathlib import Path

import numpy as np
import rasterio
from rasterio.windows import from_bounds
from scipy.ndimage import distance_transform_edt, map_coordinates, uniform_filter

import exportar_heightmap as ex

AQUI = Path(__file__).resolve().parent
URL_MOLA = "https://asc-pds-services.s3.us-west-2.amazonaws.com/mosaic/Mars_MGS_MOLA_DEM_mosaic_global_463m.tif"
CITACAO_MOLA = ("Mars MGS MOLA DEM 463m (Mars_MGS_MOLA_DEM_mosaic_global_463m), USGS Astrogeology Science Center / "
                "NASA PDS. CC0 (dominio publico).")
TRANSICAO_MOLA_M = 3000.0


def main():
    t0 = time.time()
    cache, saida = AQUI / "cache", AQUI / "saida"
    cfg = json.loads((AQUI / "mapa.json").read_text(encoding="utf-8"))
    fundo_cfg = cfg["fundo"]
    meta_path = saida / "metadata.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    g = ex.geometria(cfg)
    TX, TZ, Nx, Nz, Lx, Lz, d = g["tiles_x"], g["tiles_z"], g["Nx"], g["Nz"], g["Lx"], g["Lz"], g["d"]
    Xw, Ys, cosl = g["Xw"], g["Ys"], g["cosl"]
    Xc, Yc = Xw + Lx / 2 / cosl, Ys + Lz / 2                # centro do mapa (projetado)

    meia = fundo_cfg["meia_largura_km"] * 1000.0
    esp = float(fundo_cfg["espacamento_m"])
    n = int(round(2 * meia / esp)) + 1
    for L in (Lx, Lz):
        assert abs((L / 2) / esp - round((L / 2) / esp)) < 1e-9, "borda do mapa precisa cair numa amostra do fundo"
    v = -meia + np.arange(n) * esp                          # coordenada verdadeira (m) de cada linha/coluna
    ZZ, XX = np.meshgrid(v, v, indexing="ij")               # linha 0 = SUL
    PX, PY = Xc + XX / cosl, Yc + ZZ                        # projetado

    # ---- MOLA (so a janela necessaria) ----
    with rasterio.open("/vsicurl/" + URL_MOLA) as s:
        w = from_bounds(PX.min() - 2000, PY.min() - 2000, PX.max() + 2000, PY.max() + 2000, s.transform)
        w = w.round_offsets().round_lengths()
        mola = s.read(1, window=w).astype(np.float32)
        mola[mola <= -32000] = np.nan
        tm = s.window_transform(w)
    print(f"MOLA janela {mola.shape}  ({time.time() - t0:.0f}s)")
    fundo_mola = map_coordinates(np.nan_to_num(mola, nan=np.nanmedian(mola)),
                                 [(tm.f - PY) / -tm.e - 0.5, (PX - tm.c) / tm.a - 0.5], order=1, mode="nearest")

    # ---- CTX 20 m perto do mapa ----
    m = fundo_cfg["ctx_margem_km"] * 1000.0
    larg, alt = Lx / cosl + 2 * m / cosl, Lz + 2 * m
    x0, y1 = Xw - m / cosl, Ys + Lz + m
    lim = (x0 / ex.M_POR_GRAU, (y1 - alt) / ex.M_POR_GRAU, (x0 + larg) / ex.M_POR_GRAU, y1 / ex.M_POR_GRAU)
    base, tb, ctx_usados = ex.montar_base_ctx(cache, x0, y1, larg, alt, lim)
    # media 5x5 (100 m) antes de amostrar, para nao serrilhar
    base100 = uniform_filter(base, 5)
    li, co = (tb.f - PY) / ex.RES_BASE - 0.5, (PX - tb.c) / ex.RES_BASE - 0.5
    dentro_ctx = (li >= 0) & (li <= base.shape[0] - 1) & (co >= 0) & (co <= base.shape[1] - 1)
    fundo_ctx = map_coordinates(base100, [li, co], order=1, mode="nearest")

    desvio = float(np.median(fundo_ctx[dentro_ctx] - fundo_mola[dentro_ctx]))
    print(f"MOLA alinhado ao CTX: desvio {desvio:.1f} m")
    fundo_mola += desvio
    wc = np.clip(distance_transform_edt(dentro_ctx).astype(np.float32) * esp / TRANSICAO_MOLA_M, 0, 1)
    z = fundo_ctx * wc + fundo_mola * (1 - wc)

    # ---- dentro do mapa (e na borda): grade do jogo ----
    grade = np.load(cache / f"grade_{TX}x{TZ}.npy", mmap_mode="r")
    no_mapa = (np.abs(XX) <= Lx / 2 + 1e-6) & (np.abs(ZZ) <= Lz / 2 + 1e-6)
    gi = np.clip(np.round((ZZ[no_mapa] + Lz / 2) / d).astype(np.int64), 0, Nz - 1)
    gj = np.clip(np.round((XX[no_mapa] + Lx / 2) / d).astype(np.int64), 0, Nx - 1)
    z[no_mapa] = grade[gi, gj]

    # ---- codificacao (propria faixa; no Unity y = (h - min_codificado_do_mapa) * exagero) ----
    fmin, fmax = math.floor(float(z.min()) - 5), math.ceil(float(z.max()) + 5)
    faixa = fmax - fmin
    u = np.round((z - fmin) / faixa * 65535).astype("<u2")
    u.tofile(saida / "fundo.raw")

    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    hs = ex.hillshade(z, esp)
    fig, axp = plt.subplots(figsize=(10, 10), dpi=90)
    axp.imshow(hs, cmap="gray", origin="lower", extent=[-meia / 1000, meia / 1000, -meia / 1000, meia / 1000])
    hx, hz = Lx / 2000, Lz / 2000
    axp.plot([-hx, hx, hx, -hx, -hx], [-hz, -hz, hz, hz, -hz], "c-")
    cx, cz = m / 1000 + hx, m / 1000 + hz
    axp.plot([-cx, cx, cx, -cx, -cx], [-cz, -cz, cz, cz, -cz], "y--", lw=.8)
    axp.set_title(f"Fundo {2 * meia / 1000:.0f} km (ciano: mapa jogavel, amarelo: limite do CTX 20 m, fora: MOLA 463 m)")
    axp.set_xlabel("x km"); axp.set_ylabel("z km")
    plt.tight_layout(); plt.savefig(saida / "fundo_preview.png"); plt.close(fig)

    meta["fundo"] = {"arquivo": "fundo.raw", "amostras": n, "espacamento_m": esp, "meia_largura_m": meia,
                     "min_codificado_m": fmin, "faixa_m": faixa, "linha_0": "SUL", "origem": "centro do mapa",
                     "decodificar": "h_m = min_codificado_m + valor/65535 * faixa_m",
                     "fontes": {"ctx_20m_ate_km_da_borda": fundo_cfg["ctx_margem_km"], "ctx_dtms_catalogo": ctx_usados,
                                "mola": URL_MOLA, "mola_desvio_m": desvio, "citacao": CITACAO_MOLA}}
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"fundo {n}x{n} a {esp:.0f} m, {fmin} a {fmax} m  -> {saida / 'fundo.raw'}  ({time.time() - t0:.0f}s)")


if __name__ == "__main__":
    main()
