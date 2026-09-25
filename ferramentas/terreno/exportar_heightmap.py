"""Exporta o relevo real de Jezero (Marte) em tiles de heightmap RAW 16-bit para o Unity.

Fontes (USGS, dominio publico / CC0):
  - HiRISE DTM 1 m  (mosaico Mars 2020 TRN)            -> relevo principal onde existe
  - CTX DTM 20 m    (mosaico Mars 2020 TRN)            -> base de 20 m
  - CTX DTMs 20 m   (catalogo STAC USGS, controlados)  -> completa a base fora do mosaico

O mapa e definido em mapa.json (tamanho, canto sudoeste, agua, inicio) e as edicoes a mao em edicoes.json
(ordem em aplicar_edicoes). O processamento e feito em faixas de 1 km para caber na memoria.
preview_edicoes.py importa as funcoes de edicao daqui para testar sem os tiles (grade CTX 20 m).

Uso:  python exportar_heightmap.py [--saida DIR] [--norte-primeiro]
Detalhes e importacao no Unity: README.md desta pasta.
"""
import argparse, json, math, threading, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import rasterio
import requests
from rasterio.transform import from_origin
from rasterio.warp import Resampling, reproject
from scipy.ndimage import affine_transform, distance_transform_edt, gaussian_filter, spline_filter

AQUI = Path(__file__).resolve().parent
URL_HIRISE = ("https://asc-pds-services.s3.us-west-2.amazonaws.com/mosaic/mars2020_trn/HiRISE/"
              "JEZ_hirise_soc_006_DTM_MOLAtopography_DeltaGeoid_1m_Eqc_latTs0_lon0_blend40.tif")
URL_CTX = ("https://planetarymaps.usgs.gov/mosaic/mars2020_trn/CTX/"
           "JEZ_ctx_B_soc_008_DTM_MOLAtopography_DeltaGeoid_20m_Eqc_latTs0_lon0.tif")
URL_STAC_CTX = "https://stac.astrogeology.usgs.gov/api/collections/mro_ctx_controlled_usgs_dtms/items"
R_MARTE = 3396190.0                       # esfera IAU Mars 2000 (CRS de todos os DTMs usados)
M_POR_GRAU = R_MARTE * math.pi / 180      # equiretangular lat_ts=0: metros projetados por grau
AMOSTRAS_TILE = 1024                      # 1025 amostras por tile, borda compartilhada
RES_BASE = 20.0                           # base CTX em 20 m
TRANSICAO_HIRISE_M = 30.0                 # HiRISE -> CTX nos buracos/bordas
TRANSICAO_CTX_M = 500.0                   # mosaico CTX -> DTMs CTX do catalogo
MARGEM_HIRISE = 64                        # linhas/colunas extras em volta (filtro cubico + transicao)
CITACAO = ("Fergason, R.L., et al. (2020). Mars 2020 Terrain Relative Navigation Flight Product "
           "Generation: Digital Terrain Model and Orthorectified Image Mosaics. 51st LPSC, abstract #2020. "
           "USGS Astrogeology Science Center. Dados de dominio publico (CC0 / USGS).")
CITACAO_STAC = ("USGS Astrogeology Science Center, MRO CTX controlled DTMs (Analysis Ready Data, "
                "stac.astrogeology.usgs.gov, colecao mro_ctx_controlled_usgs_dtms). CC0-1.0.")


def baixar(url, destino):
    if not destino.exists():
        print(f"baixando {destino.name} ...")
        r = requests.get(url, timeout=600); r.raise_for_status()
        tmp = destino.with_suffix(".part"); tmp.write_bytes(r.content); tmp.replace(destino)
    return destino


# ---------------------------------------------------------------- base CTX 20 m
def montar_base_ctx(cache, x0, y1, largura, altura, lim_graus):
    """Grade 20 m (linha 0 = norte) cobrindo o mapa + margem. Mosaico Mars 2020 onde existe; fora dele,
    mediana dos DTMs CTX do catalogo, cada um com o desvio vertical corrigido contra o mosaico."""
    tr = from_origin(x0, y1, RES_BASE, RES_BASE)
    shape = (int(math.ceil(altura / RES_BASE)), int(math.ceil(largura / RES_BASE)))

    def reproj(caminho):
        dst = np.full(shape, np.nan, np.float32)
        with rasterio.open(caminho) as s:
            reproject(rasterio.band(s, 1), dst, src_nodata=s.nodata, dst_transform=tr, dst_crs=s.crs,
                      dst_nodata=np.nan, resampling=Resampling.bilinear)
        dst[(dst < -1e30) | (dst < -30000)] = np.nan
        return dst

    mosaico = reproj(baixar(URL_CTX, cache / "ctx_20m.tif"))
    falta = np.isnan(mosaico)
    print(f"base CTX {shape}: mosaico cobre {100 * (1 - falta.mean()):.1f}%")
    usados = []
    if falta.any():
        o, s_, l, n = lim_graus
        bbox = f"{o - 0.05},{s_ - 0.05},{l + 0.05},{n + 0.05}"
        meta = cache / f"stac_ctx_{bbox}.json"
        if not meta.exists():
            meta.write_text(json.dumps(requests.get(f"{URL_STAC_CTX}?bbox={bbox}&limit=500", timeout=120).json()["features"]))
        pasta = cache / "ctx_stac"; pasta.mkdir(exist_ok=True)
        lin, col = np.where(falta.any(1))[0], np.where(falta.any(0))[0]
        f_n, f_s = (tr.f - lin.min() * RES_BASE) / M_POR_GRAU, (tr.f - (lin.max() + 1) * RES_BASE) / M_POR_GRAU
        f_o, f_l = (tr.c + col.min() * RES_BASE) / M_POR_GRAU, (tr.c + (col.max() + 1) * RES_BASE) / M_POR_GRAU
        camadas = []
        for f in json.loads(meta.read_text()):
            b = f["bbox"]
            if f["properties"].get("license") != "CC0-1.0" or b[2] < f_o or b[0] > f_l or b[3] < f_s or b[1] > f_n:
                continue
            a = reproj(baixar(f["assets"]["dtm"]["href"], pasta / f"{f['id']}.tif"))
            ambos = ~np.isnan(a) & ~falta
            if not (~np.isnan(a) & falta).any() or ambos.sum() < 2000:
                continue                                  # nao ajuda no buraco ou nao da pra alinhar
            dif = mosaico[ambos] - a[ambos]
            desvio, disp = float(np.median(dif)), float(np.std(dif))
            if disp > 15:
                print(f"  descartado {f['id']} (dispersao {disp:.1f} m)")
                continue
            camadas.append(a + desvio)
            usados.append({"id": f["id"], "desvio_m": round(desvio, 2), "dispersao_m": round(disp, 2)})
        print(f"  {len(camadas)} DTMs CTX do catalogo usados")
        if camadas:
            with np.errstate(all="ignore"):
                extra = np.nanmedian(np.stack(camadas), axis=0).astype(np.float32)
            del camadas
            w = np.clip(distance_transform_edt(~falta).astype(np.float32) * RES_BASE / TRANSICAO_CTX_M, 0, 1)
            tem_extra = ~np.isnan(extra)
            base = np.where(falta, extra, np.where(tem_extra, mosaico * w + np.nan_to_num(extra) * (1 - w), mosaico))
        else:
            base = mosaico
    else:
        base = mosaico
    if np.isnan(base).any():                              # ultimo recurso: vizinho mais proximo
        idx = distance_transform_edt(np.isnan(base), return_distances=False, return_indices=True)
        base = base[tuple(idx)]
    return base.astype(np.float32), tr, usados


# ---------------------------------------------------------------- HiRISE 1 m
def ler_hirise(cache, r0, r1, c0, c1):
    """Linhas [r0,r1) x colunas [c0,c1) do HiRISE via HTTP Range (o TIFF e em faixas de 1 linha, nao e COG).
    Grava direto num .npy mapeado em disco e devolve em modo leitura (nao carrega tudo na memoria)."""
    p = cache / f"hirise_{r0}_{r1}_{c0}_{c1}.npy"
    for q in cache.glob("hirise_*_*_*_*.npy"):             # reaproveita um recorte maior ja baixado
        try:
            R0, R1, C0, C1 = (int(v) for v in q.stem.split("_")[1:5])
        except ValueError:
            continue
        if not p.exists() and R0 <= r0 and r1 <= R1 and C0 <= c0 and c1 <= C1:
            print(f"HiRISE: reaproveitando {q.name}")
            return np.load(q, mmap_mode="r")[r0 - R0:r1 - R0, c0 - C0:c1 - C0]
    if not p.exists():
        with rasterio.open("/vsicurl/" + URL_HIRISE) as d:
            assert d.block_shapes[0] == (1, d.width) and d.dtypes[0] == "float32"
            offs = [int(d.get_tag_item(f"BLOCK_OFFSET_0_{r}", "TIFF", bidx=1)) for r in range(r0, r1)]
        tmp = p.with_suffix(".part.npy")
        mm = np.lib.format.open_memmap(tmp, mode="w+", dtype=np.float32, shape=(r1 - r0, c1 - c0))
        sess = {}

        def linha(i):
            s = sess.setdefault(threading.get_ident(), requests.Session())
            a, n = offs[i] + c0 * 4, (c1 - c0) * 4
            for k in range(6):
                try:
                    r = s.get(URL_HIRISE, headers={"Range": f"bytes={a}-{a + n - 1}"}, timeout=60)
                    if r.status_code == 206 and len(r.content) == n:
                        v = np.frombuffer(r.content, "<f4")
                        mm[i] = np.where(v < -1e30, np.nan, v)
                        return
                except requests.RequestException:
                    pass
                time.sleep(1 + k)
            raise RuntimeError(f"falha lendo linha {r0 + i}")

        print(f"baixando HiRISE: {r1 - r0} linhas x {c1 - c0} colunas ...")
        with ThreadPoolExecutor(16) as ex:
            list(ex.map(linha, range(r1 - r0)))
        mm.flush(); del mm
        tmp.replace(p)
    return np.load(p, mmap_mode="r")


# ---------------------------------------------------------------- edicoes
# Todas: grade com linha 0 = SUL, espacamento d (m), alturas reais; x_origem/z_origem = coordenada (m, sistema de
# referencia das edicoes) da amostra [0,0]. Posicoes em km ou m de referencia, como no edicoes.json.
def suave(t):
    return t * t * (3 - 2 * t)


def janela(z, d, xa, za, xb, zb):
    """Linhas/colunas da grade que cobrem o retangulo (m, ja relativo a amostra [0,0]); None se fora."""
    r0, r1 = max(0, int(za / d)), min(z.shape[0], int(zb / d) + 2)
    c0, c1 = max(0, int(xa / d)), min(z.shape[1], int(xb / d) + 2)
    return (r0, r1, c0, c1) if r1 > r0 and c1 > c0 else None


def borda_irregular(ang, irr, semente):
    """Fator que deforma um raio com senoides de fase fixa (divide a distancia por ele)."""
    rng = np.random.default_rng(semente)
    forma = sum(rng.uniform(0.5, 1) / k * np.sin(k * ang + rng.uniform(0, 2 * np.pi)) for k in range(2, 9))
    return 1 + irr * forma / 1.2


def aplicar_platos(z, d, platos, x_origem=0.0, z_origem=0.0):
    """Nivela areas circulares. Dentro do raio a altura vira `altura_m` mais uma fracao (`detalhe`) do microrrelevo
    original; na transicao mistura com o relevo real (smoothstep). `altura_m: null` = mediana do relevo dentro do
    raio (segue o terreno ja editado, ex.: pad sobre um nivelamento). `irregularidade` deforma a borda (`semente`)."""
    n_lin, n_col = z.shape
    for p in platos:
        alcance = p["raio_m"] + p["transicao_m"]
        irr = p.get("irregularidade", 0.0)
        c, r = (p["x_m"] - x_origem) / d, (p["z_m"] - z_origem) / d
        pad = int(alcance * (1 + 1.5 * irr) / d) + 2
        r0, r1 = max(0, int(r) - pad), min(n_lin, int(r) + pad)
        c0, c1 = max(0, int(c) - pad), min(n_col, int(c) + pad)
        if r1 <= r0 or c1 <= c0:
            continue
        win = np.array(z[r0:r1, c0:c1])
        yy, xx = np.mgrid[r0:r1, c0:c1]
        dist = np.hypot(yy - r, xx - c) * d
        ang = np.arctan2(r - yy, xx - c)                    # mesmo desenho da versao com linha 0 = norte
        dist = dist / borda_irregular(ang, irr, p.get("semente", 0))
        w = suave(np.clip((alcance - dist) / p["transicao_m"], 0, 1))
        altura = p["altura_m"] if p.get("altura_m") is not None else float(np.median(win[dist < p["raio_m"]]))
        detalhe = win - gaussian_filter(win, 20 / d)
        plano = altura + p["detalhe"] * detalhe
        z[r0:r1, c0:c1] = (win * (1 - w) + plano * w).astype(np.float32)
        print(f"plato '{p['nome']}': raio {p['raio_m']} m + transicao {p['transicao_m']} m em {altura:.1f} m")


def aplicar_nivelamentos(z, d, nivelamentos, x_origem=0.0, z_origem=0.0):
    """Area grande quase plana (D16): ajusta um plano (minimos quadrados) ao relevo dentro de `poligono_km`, guarda
    `inclinacao` da inclinacao dele e `manter` da ondulacao em volta do plano. Transicao de `transicao_m` para FORA
    do poligono (smoothstep). Plano e pesos numa grade 4x mais grossa, como nas suavizacoes."""
    from matplotlib.path import Path as Caminho
    st = 4
    for nv in nivelamentos:
        poly = np.array(nv["poligono_km"], float) * 1000 - [x_origem, z_origem]
        tr = nv["transicao_m"]
        jan = janela(z, d, *(poly.min(0) - tr - 2 * d * st), *(poly.max(0) + tr + 2 * d * st))
        if jan is None:
            continue
        r0, r1, c0, c1 = jan
        win = np.array(z[r0:r1, c0:c1], dtype=np.float32)
        xs, zs = (c0 + np.arange(c1 - c0)) * d, (r0 + np.arange(r1 - r0)) * d
        grosso = win[::st, ::st]
        gx, gz = np.meshgrid(xs[::st], zs[::st])
        dentro = Caminho(poly).contains_points(np.c_[gx.ravel(), gz.ravel()]).reshape(grosso.shape)
        cx, cz = gx[dentro].mean(), gz[dentro].mean()
        A = np.c_[gx[dentro] - cx, gz[dentro] - cz, np.ones(dentro.sum())]
        a, b, h = np.linalg.lstsq(A, grosso[dentro], rcond=None)[0]
        a, b = a * nv["inclinacao"], b * nv["inclinacao"]
        w = suave(np.clip(1 - distance_transform_edt(~dentro).astype(np.float32) * d * st / tr, 0, 1))
        w = affine_transform(w, [1 / st, 1 / st], output_shape=win.shape, order=1, mode="nearest")
        plano = (a * (xs - cx))[None, :] + (b * (zs - cz))[:, None] + h
        z[r0:r1, c0:c1] = (win - w * (1 - nv["manter"]) * (win - plano)).astype(np.float32)
        incl = math.degrees(math.atan(math.hypot(a, b)))
        print(f"nivelamento '{nv['nome']}': plano {h:.1f} m em ({(cx + x_origem) / 1000:.2f}; {(cz + z_origem) / 1000:.2f}) km, "
              f"inclinacao {incl:.2f} graus real, mantem {100 * nv['manter']:.0f}% da ondulacao")


def stamp_mesa_ctx(caminho_ctx, g, m, res=10.0):
    """Forma (0..1, linha 0 = sul, passo `res` m) de um morro real do mosaico CTX 20 m em volta de `fonte_km`
    (referencia), raio `fonte_raio_m`: relevo acima do plano do anel externo, normalizado pelo pico e zerado na borda.
    `topo_plano` (0..1) corta o pico nessa fracao -> topo plano de mesa."""
    R = m["fonte_raio_m"]
    u = np.arange(-R, R + res / 2, res)
    X = g["Xw"] + (m["fonte_km"][0] * 1000 + g["desloc_x"] + u) / g["cosl"]
    Y = g["Ys"] + m["fonte_km"][1] * 1000 + g["desloc_z"] + u
    with rasterio.open(caminho_ctx) as s:
        a, t = s.read(1).astype(np.float32), s.transform
    from scipy.ndimage import map_coordinates
    lin, col = np.meshgrid((Y - t.f) / t.e - 0.5, (X - t.c) / t.a - 0.5, indexing="ij")
    src = map_coordinates(a, [lin, col], order=1)
    assert (src > -30000).all(), f"stamp '{m['nome']}' fora do mosaico CTX"
    uu, vv = np.meshgrid(u, u)                               # x (colunas), z (linhas)
    r = np.hypot(uu, vv)
    anel = (r > 0.85 * R) & (r < R)
    c = np.linalg.lstsq(np.c_[uu[anel], vv[anel], np.ones(anel.sum())], src[anel], rcond=None)[0]
    rel = np.clip(src - (c[0] * uu + c[1] * vv + c[2]), 0, None)
    forma = rel / rel[r < R / 2].max() * (1 - suave(np.clip((r - 0.8 * R) / (0.2 * R), 0, 1)))
    return np.minimum(forma / m.get("topo_plano", 1.0), 1.0), res


def aplicar_mesas(z, d, mesas, carregar_stamp, x_origem=0.0, z_origem=0.0):
    """Soma relevo com a forma de um morro real (stamp): `somar_m` reais no topo, base de `base_raio_m`, girado
    `rotacao_graus`. `carregar_stamp(mesa) -> (forma, res)` (ver stamp_mesa_ctx). Devolve topo antes/depois."""
    from scipy.ndimage import map_coordinates
    res_ = {}
    for m in mesas:
        forma, res = carregar_stamp(m)
        R = res * (forma.shape[0] - 1) / 2
        Rb = m["base_raio_m"]
        cx, cz = m["x_km"] * 1000 - x_origem, m["z_km"] * 1000 - z_origem
        jan = janela(z, d, cx - Rb, cz - Rb, cx + Rb, cz + Rb)
        if jan is None:
            continue
        r0, r1, c0, c1 = jan
        win = np.array(z[r0:r1, c0:c1], dtype=np.float32)
        yy, xx = np.mgrid[r0:r1, c0:c1]
        dx, dz = xx * d - cx, yy * d - cz
        ang = math.radians(m.get("rotacao_graus", 0))
        u = (dx * math.cos(ang) + dz * math.sin(ang)) * R / Rb
        v = (-dx * math.sin(ang) + dz * math.cos(ang)) * R / Rb
        soma = map_coordinates(forma, [(v + R) / res, (u + R) / res], order=1, mode="constant", cval=0.0)
        topo = np.hypot(dx, dz) < 0.4 * Rb                  # vazio se o centro esta fora desta grade (preview)
        antes = float(win[topo].max()) if topo.any() else None
        win += m["somar_m"] * soma
        z[r0:r1, c0:c1] = win
        if antes is not None:                               # ganho visivel do cume (o maximo pode mudar de lugar)
            depois = float(win[topo].max())
            res_[m["nome"]] = {"topo_antes_m": round(antes, 1), "topo_depois_m": round(depois, 1), "somado_m": round(depois - antes, 1)}
            print(f"mesa '{m['nome']}': +{m['somar_m']} m, base {Rb} m, topo {antes:.1f} -> {depois:.1f} m")
    return res_


def aplicar_pocos(z, d, pocos, x_origem=0.0, z_origem=0.0):
    """Poços de colapso (D15): cava `profundidade_m` com fundo plano ate `fundo` x raio e paredes ingremes
    (smoothstep) ate `raio_m`; borda irregular como nos platos. O microrrelevo do fundo continua."""
    for p in pocos:
        irr, raio = p.get("irregularidade", 0.0), p["raio_m"]
        cx, cz = p["x_km"] * 1000 - x_origem, p["z_km"] * 1000 - z_origem
        alc = raio * (1 + irr) + 2 * d
        jan = janela(z, d, cx - alc, cz - alc, cx + alc, cz + alc)
        if jan is None:
            continue
        r0, r1, c0, c1 = jan
        yy, xx = np.mgrid[r0:r1, c0:c1]
        dx, dz = xx * d - cx, yy * d - cz
        dist = np.hypot(dx, dz) / borda_irregular(np.arctan2(dz, dx), irr, p.get("semente", 0))
        fundo = p.get("fundo", 0.35)
        w = suave(np.clip((raio - dist) / (raio * (1 - fundo)), 0, 1))
        z[r0:r1, c0:c1] = (np.array(z[r0:r1, c0:c1]) - p["profundidade_m"] * w).astype(np.float32)
        print(f"poco '{p['nome']}': raio {raio} m, profundidade real {p['profundidade_m']} m")


def perfil_trilha(t, ds):
    """Pontos da polilinha da trilha (m de referencia) a cada `ds` m."""
    P = np.array(t["polilinha_km"], float) * 1000
    s = np.r_[0, np.cumsum(np.hypot(*np.diff(P, axis=0).T))]
    a = np.arange(0, s[-1] + ds / 2, ds)
    return np.c_[np.interp(a, s, P[:, 0]), np.interp(a, s, P[:, 1])]


def aplicar_trilhas(z, d, trilhas, exagero, x_origem=0.0, z_origem=0.0):
    """Leito de trilha (D15, Mirante): faixa de `largura_m` com a altura do eixo, sem inclinacao lateral, e
    `transicao_m` de cada lado. O perfil do eixo e suavizado (`suavizar_m`) e depois so CORTADO onde passa de
    `max_inclinacao_jogo_graus` (com o exagero): rampa escavada nos degraus, nunca aterro. Devolve estatisticas."""
    from scipy.ndimage import gaussian_filter1d, map_coordinates
    from scipy.spatial import cKDTree
    res_ = {}
    for t in trilhas:
        ds = min(d / 2, 1.0)
        pts = perfil_trilha(t, ds) - [x_origem, z_origem]
        alc = t["largura_m"] / 2 + t["transicao_m"]
        jan = janela(z, d, *(pts.min(0) - alc - 2 * d), *(pts.max(0) + alc + 2 * d))
        if jan is None:
            continue
        r0, r1, c0, c1 = jan
        win = np.array(z[r0:r1, c0:c1], dtype=np.float32)
        h0 = map_coordinates(win, [pts[:, 1] / d - r0, pts[:, 0] / d - c0], order=1, mode="nearest")
        h = gaussian_filter1d(h0, t["suavizar_m"] / ds, mode="nearest")
        k = math.tan(math.radians(t["max_inclinacao_jogo_graus"])) / exagero * ds      # subida real maxima por passo
        i = np.arange(len(h))
        h = k * i + np.minimum.accumulate(h - k * i)                                     # limite subindo
        h = -k * i + np.minimum.accumulate((h + k * i)[::-1])[::-1]                      # limite descendo
        yy, xx = np.mgrid[r0:r1, c0:c1]
        dist, idx = cKDTree(pts).query(np.c_[(xx * d).ravel(), (yy * d).ravel()], distance_upper_bound=alc)
        perto = np.isfinite(dist)
        w = np.zeros(win.size, np.float32)
        w[perto] = suave(np.clip((alc - dist[perto]) / t["transicao_m"], 0, 1))
        leito = np.zeros(win.size, np.float32); leito[perto] = h[idx[perto]]
        w, leito = w.reshape(win.shape), leito.reshape(win.shape)
        z[r0:r1, c0:c1] = (win * (1 - w) + leito * w).astype(np.float32)
        incl = lambda p: float(np.degrees(np.arctan(exagero * np.abs(np.diff(p)) / ds)).max())
        res_[t["nome"]] = {"comprimento_km": round(len(pts) * ds / 1000, 2), "maior_corte_m": round(float((h0 - h).max()), 1),
                           "maior_aterro_m": round(float((h - h0).max()), 1),
                           "incl_max_eixo_jogo_antes_graus": round(incl(gaussian_filter1d(h0, 5 / ds)), 1),
                           "incl_max_eixo_jogo_leito_graus": round(incl(h), 1)}
        print(f"trilha '{t['nome']}': {res_[t['nome']]}")
    return res_


def aplicar_edicoes(z, d, edicoes, cache, carregar_stamp, exagero, x_origem=0.0, z_origem=0.0):
    """Aplica TODAS as edicoes nesta ordem (a mesma no exportador e no preview):
    1 suavizacoes  (forma grande)           2 nivelamentos (area da base)
    3 mesas        (soma relevo; depois do nivelamento para a transicao nao achatar a mesa)
    4 pocos, 5 canyons (cavam; somam diferenca ao terreno ja moldado)
    6 trilhas      (leito segue o terreno final)
    7 platos       (alturas exatas por ultimo: pads e cume por cima de tudo).
    Devolve estatisticas das mesas e trilhas."""
    aplicar_suavizacoes(z, d, edicoes.get("suavizacoes", []), x_origem, z_origem)
    aplicar_nivelamentos(z, d, edicoes.get("nivelamentos", []), x_origem, z_origem)
    est = {"mesas": aplicar_mesas(z, d, edicoes.get("mesas", []), carregar_stamp, x_origem, z_origem)}
    aplicar_pocos(z, d, edicoes.get("pocos", []), x_origem, z_origem)
    aplicar_canyons(z, d, edicoes.get("canyons", []), cache, x_origem, z_origem)
    est["trilhas"] = aplicar_trilhas(z, d, edicoes.get("trilhas", []), exagero, x_origem, z_origem)
    aplicar_platos(z, d, edicoes.get("platos", []), x_origem, z_origem)
    return est


def verificar_edicoes(z, d, edicoes, est, nivel_agua, exagero, x_origem=0.0, z_origem=0.0):
    """Autoverificacao das edicoes D15/D16 no terreno final (inclinacao 'no jogo' = com o exagero, escala ~20 m).
    Imprime OK/AVISO e devolve o resumo (vai para metadata.json). Nao aborta a geracao."""
    from matplotlib.path import Path as Caminho
    from scipy.ndimage import map_coordinates
    out = {"mesas": est["mesas"], "trilhas": est["trilhas"], "nivelamentos": {}}
    st = max(1, round(20 / d))
    for nv in edicoes.get("nivelamentos", []):
        poly = np.array(nv["poligono_km"], float) * 1000 - [x_origem, z_origem]
        jan = janela(z, d, *poly.min(0), *poly.max(0))
        if jan is None:
            continue
        r0, r1, c0, c1 = jan
        sub = np.array(z[r0:r1:st, c0:c1:st], dtype=np.float32)
        gz, gx = np.gradient(gaussian_filter(sub, 1) * exagero, d * st)
        incl = np.degrees(np.arctan(np.hypot(gx, gz)))
        xx, zz = np.meshgrid((c0 + np.arange(sub.shape[1]) * st) * d, (r0 + np.arange(sub.shape[0]) * st) * d)
        dentro = Caminho(poly).contains_points(np.c_[xx.ravel(), zz.ravel()]).reshape(sub.shape)
        v = {"incl_mediana_jogo_graus": round(float(np.median(incl[dentro])), 2),
             "incl_p90_jogo_graus": round(float(np.percentile(incl[dentro], 90)), 2),
             "chao_min_m": round(float(sub[dentro].min()), 1), "acima_da_agua_min_m": round(float(sub[dentro].min() - nivel_agua), 1)}
        v["ok"] = v["incl_mediana_jogo_graus"] <= 1.5 and v["acima_da_agua_min_m"] >= 50
        out["nivelamentos"][nv["nome"]] = v
        print(f"verificacao '{nv['nome']}': {'OK' if v['ok'] else 'AVISO'} {v} (meta: mediana <= 1,5 graus, >= 50 m acima da agua)")
    for m in edicoes.get("mesas", []):
        v = est["mesas"].get(m["nome"])
        if v:
            v["ok"] = v["somado_m"] >= 0.6 * m["somar_m"]    # em encosta o cume antigo pode ficar fora do stamp
            print(f"verificacao mesa '{m['nome']}': {'OK' if v['ok'] else 'AVISO'} cume {v['topo_antes_m']} -> {v['topo_depois_m']} m "
                  f"(+{v['somado_m']} m, pedido +{m['somar_m']} m)")
    for t in edicoes.get("trilhas", []):
        pts = perfil_trilha(t, 5.0) - [x_origem, z_origem]
        jan = janela(z, d, *(pts.min(0) - 2 * d), *(pts.max(0) + 2 * d))
        if jan is None:
            continue
        r0, r1, c0, c1 = jan
        h = map_coordinates(np.array(z[r0:r1, c0:c1]), [pts[:, 1] / d - r0, pts[:, 0] / d - c0], order=1, mode="nearest")
        incl = np.degrees(np.arctan(exagero * np.abs(np.diff(h)) / 5.0))
        v = out["trilhas"].setdefault(t["nome"], {})
        v.update({"incl_max_final_jogo_graus": round(float(incl.max()), 1), "incl_p95_final_jogo_graus": round(float(np.percentile(incl, 95)), 1),
                  "trechos_acima_25_graus_m": int((incl > 25).sum() * 5)})
        print(f"verificacao trilha '{t['nome']}': incl. no jogo (passo 5 m) max {v['incl_max_final_jogo_graus']} graus, "
              f"p95 {v['incl_p95_final_jogo_graus']}, {v['trechos_acima_25_graus_m']} m acima de 25 graus")
    return out


def aplicar_suavizacoes(z, d, suavizacoes, x_origem=0.0, z_origem=0.0):
    """Reduz a ondulacao dentro de poligonos (grade com linha 0 = SUL). A forma grande do relevo (escala acima de
    `escala_m`) fica; o que ondula abaixo dela fica com a fracao `manter`. Transicao suave de `transicao_m` para fora.
    `x_origem`/`z_origem`: coordenada (m, sistema das edicoes) da amostra [0,0]."""
    from matplotlib.path import Path as Caminho
    n_lin, n_col = z.shape
    st = 4                                                   # calculo da forma grande numa grade 4x mais grossa
    for s in suavizacoes:
        poly = np.array(s["poligono_km"], float) * 1000 - [x_origem, z_origem]
        borda, manter, sig = s["transicao_m"], s["manter"], s["escala_m"]
        pad = borda + 3 * sig
        (xa, za), (xb, zb) = poly.min(0) - pad, poly.max(0) + pad
        r0, r1 = max(0, int(za / d)), min(n_lin, int(zb / d) + 1)
        c0, c1 = max(0, int(xa / d)), min(n_col, int(xb / d) + 1)
        if r1 <= r0 or c1 <= c0:
            continue
        win = np.array(z[r0:r1, c0:c1], dtype=np.float32)
        grosso = win[::st, ::st]
        forma = gaussian_filter(grosso, sig / (d * st))
        yy, xx = np.mgrid[0:grosso.shape[0], 0:grosso.shape[1]]
        dentro = Caminho(poly).contains_points(np.c_[((c0 + xx * st) * d).ravel(), ((r0 + yy * st) * d).ravel()]).reshape(grosso.shape)
        t = np.clip(distance_transform_edt(dentro).astype(np.float32) * d * st / borda, 0, 1)
        w = t * t * (3 - 2 * t)
        forma = affine_transform(forma, [1 / st, 1 / st], output_shape=win.shape, order=1, mode="nearest")
        w = affine_transform(w, [1 / st, 1 / st], output_shape=win.shape, order=1, mode="nearest")
        z[r0:r1, c0:c1] = (win + w * (1 - manter) * (forma - win)).astype(np.float32)
        print(f"suavizacao '{s['nome']}': mantem {100 * manter:.0f}% da ondulacao abaixo de ~{sig * 5:.0f} m")


def aplicar_canyons(z, d, canyons, cache, x_origem=0.0, z_origem=0.0):
    """Escava vales reais (stamps de DTM HiRISE) no terreno (grade com linha 0 = SUL).
    O eixo do vale no DTM de origem e achado sozinho; o vale e girado para o eixo de destino (mantendo o lado
    esquerdo do eixo como esquerdo), esticado no comprimento e escavado com `profundidade_m` real. A altura soma
    ao terreno existente como diferenca em relacao ao planalto do proprio stamp. Pontas e laterais afinam suave."""
    from rasterio.windows import Window
    n_lin, n_col = z.shape
    for cy in canyons:
        # ---- origem: DTM 1 m em cache ----
        chave = Path(cy["fonte_url"]).stem                  # cache pela fonte (o nome do canyon pode mudar)
        src_npy = cache / f"stamp_{chave}.npy"
        if not src_npy.exists():
            with rasterio.open("/vsicurl/" + cy["fonte_url"]) as s:
                a = s.read(1).astype(np.float32)
                a[(a == s.nodata) | (a < -1e30) | ~np.isfinite(a)] = np.nan
                res = abs(s.res[0])
            np.save(src_npy, a); (cache / f"stamp_{chave}.json").write_text(json.dumps({"res": res}))
        src = np.load(src_npy)
        res = json.loads((cache / f"stamp_{chave}.json").read_text())["res"]
        valido = np.isfinite(src)
        # eixo: pontos mais fundos que o meio do caminho entre planalto e fundo (coordenadas x->direita, y->norte)
        planalto, fundo = np.nanpercentile(src, 90), np.nanpercentile(src, 1)
        ii, jj = np.nonzero(valido & (src < (planalto + fundo) / 2))
        pts = np.c_[jj * res, -ii * res]
        centro = pts.mean(0)
        _, _, vt = np.linalg.svd(pts - centro, full_matrices=False)
        eixo = vt[0] if vt[0][0] >= 0 else -vt[0]            # de oeste para leste
        perp = np.array([-eixo[1], eixo[0]])                 # esquerda do eixo (norte, se o eixo aponta p/ leste)
        u = (pts - centro) @ eixo
        u0, u1 = np.percentile(u, 1) + 300, np.percentile(u, 99) - 300   # evita as pontas cortadas pelo DTM
        comp_src = u1 - u0
        # ---- destino ----
        de = np.array(cy["de_km"], float) * 1000 - [x_origem, z_origem]
        ate = np.array(cy["ate_km"], float) * 1000 - [x_origem, z_origem]
        comp = np.linalg.norm(ate - de); ed = (ate - de) / comp; pd = np.array([-ed[1], ed[0]])
        meia = cy["largura_km"] * 500
        cantos = np.array([de + pd * meia, de - pd * meia, ate + pd * meia, ate - pd * meia])
        (xa, za), (xb, zb) = cantos.min(0) - 50, cantos.max(0) + 50
        r0, r1 = max(0, int(za / d)), min(n_lin, int(zb / d) + 1)
        c0, c1 = max(0, int(xa / d)), min(n_col, int(xb / d) + 1)
        if r1 <= r0 or c1 <= c0:
            continue
        from scipy.ndimage import map_coordinates
        cheio = np.where(valido, src, planalto)

        def amostrar(lin, col):
            """ud (ao longo), vd (de lado, > 0 = esquerda) e altura do stamp nas amostras (lin, col) da grade."""
            rx, rz = col * d - de[0], lin * d - de[1]
            ud, vd = rx * ed[0] + rz * ed[1], rx * pd[0] + rz * pd[1]
            us = u0 + np.clip(ud, 0, comp) * (comp_src / comp)   # comprimento esticado, largura igual
            px_ = centro[0] + us * eixo[0] + vd * perp[0]
            py_ = centro[1] + us * eixo[1] + vd * perp[1]
            return ud, vd, map_coordinates(cheio, [-py_ / res, px_ / res], order=1, mode="nearest").astype(np.float32)

        # planalto local de cada seccao (faixa lateral), medido numa grade ~10 m -> so a diferenca entra no terreno
        st = max(1, int(10 / d))
        ud, vd, s_amostra = amostrar(*np.mgrid[r0:r1:st, c0:c1:st])
        faixa_lat = (np.abs(vd) > meia * 0.7) & (np.abs(vd) < meia)
        bins = np.clip((ud / comp * 64).astype(int), 0, 63)
        ref = np.array([np.median(s_amostra[faixa_lat & (bins == b)]) if (faixa_lat & (bins == b)).any() else planalto for b in range(64)])
        ref = gaussian_filter(ref, 2)
        k = cy["profundidade_m"] / max(planalto - fundo, 1.0)
        for a0 in range(r0, r1, 1024):                       # em faixas: o canyon diagonal cobre ~7x7 km
            a1 = min(r1, a0 + 1024)
            ud, vd, s_amostra = amostrar(*np.mgrid[a0:a1, c0:c1])
            delta = (s_amostra - ref[np.clip((ud / comp * 64).astype(int), 0, 63)]) * k
            t_ponta = np.clip(np.minimum(ud, comp - ud) / (cy["afinar_pontas_km"] * 1000), 0, 1)
            t_lado = np.clip((meia - np.abs(vd)) / (meia * 0.3), 0, 1)
            z[a0:a1, c0:c1] = (np.array(z[a0:a1, c0:c1]) + delta * suave(t_ponta) * suave(t_lado)).astype(np.float32)
        print(f"canyon '{cy['nome']}': {comp / 1000:.1f} km (origem {comp_src / 1000:.1f} km), profundidade real {cy['profundidade_m']} m")


def hillshade(z, d, az=315, alt=40):
    gy, gx = np.gradient(z, d)
    sl = np.arctan(np.hypot(gx, gy)); asp = np.arctan2(-gx, gy); a = np.radians(360 - az + 90); e = np.radians(alt)
    return np.clip(np.sin(e) * np.cos(sl) + np.cos(e) * np.sin(sl) * np.cos(a - asp), 0, 1)


def geometria(cfg):
    """Grade do mapa (retangular, linha 0 = SUL, a partir do canto sudoeste) e deslocamento do sistema de
    referencia das edicoes: coordenada_mapa = coordenada_referencia + desloc."""
    tx, tz = cfg["tiles_x"], cfg["tiles_z"]
    g = dict(tiles_x=tx, tiles_z=tz, Nx=tx * AMOSTRAS_TILE + 1, Nz=tz * AMOSTRAS_TILE + 1, Lx=tx * 1000.0, Lz=tz * 1000.0)
    g["d"] = 1000.0 / AMOSTRAS_TILE
    g["Xw"], g["Ys"] = cfg["oeste_graus"] * M_POR_GRAU, cfg["sul_graus"] * M_POR_GRAU
    g["lat_c"] = (g["Ys"] + g["Lz"] / 2) / M_POR_GRAU
    g["cosl"] = math.cos(math.radians(g["lat_c"]))
    g["Xe"], g["Yn"] = g["Xw"] + g["Lx"] / g["cosl"], g["Ys"] + g["Lz"]
    ref = cfg.get("referencia", {"oeste_graus": cfg["oeste_graus"], "sul_graus": cfg["sul_graus"]})
    g["desloc_x"] = (ref["oeste_graus"] * M_POR_GRAU - g["Xw"]) * g["cosl"]
    g["desloc_z"] = ref["sul_graus"] * M_POR_GRAU - g["Ys"]
    return g


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--saida", type=Path, default=AQUI / "saida")
    ap.add_argument("--cache", type=Path, default=AQUI / "cache")
    ap.add_argument("--mapa", type=Path, default=AQUI / "mapa.json", help="tamanho, canto sudoeste, agua, inicio, area jogavel")
    ap.add_argument("--edicoes", type=Path, default=AQUI / "edicoes.json", help="platos e suavizacoes a mao")
    ap.add_argument("--margem", type=float, default=5.0, help="margem (m) abaixo do min e acima do max")
    ap.add_argument("--norte-primeiro", action="store_true",
                    help="grava a linha 0 do RAW = borda NORTE (usar com 'Flip Vertically' no Unity)")
    a = ap.parse_args()
    t0 = time.time()
    a.saida.mkdir(parents=True, exist_ok=True); a.cache.mkdir(parents=True, exist_ok=True)
    cfg = json.loads(a.mapa.read_text(encoding="utf-8"))
    edicoes = json.loads(a.edicoes.read_text(encoding="utf-8")) if a.edicoes.exists() else {}
    for f in a.saida.glob("Jezero_*"):
        f.unlink()

    g = geometria(cfg)
    TX, TZ, Nx, Nz, Lx, Lz, d = g["tiles_x"], g["tiles_z"], g["Nx"], g["Nz"], g["Lx"], g["Lz"], g["d"]
    Xw, Ys, Xe, Yn, cosl, lat_c = g["Xw"], g["Ys"], g["Xe"], g["Yn"], g["cosl"], g["lat_c"]
    ox, oz = -g["desloc_x"], -g["desloc_z"]                 # amostra [0,0] no sistema das edicoes
    limites = dict(oeste=Xw / M_POR_GRAU, leste=Xe / M_POR_GRAU, sul=Ys / M_POR_GRAU, norte=Yn / M_POR_GRAU)
    nivel_agua = float(cfg["nivel_agua_m"])
    print(f"mapa {TX}x{TZ} km, referencia deslocada ({g['desloc_x']:.0f}, {g['desloc_z']:.0f}) m")

    base, tb, ctx_usados = montar_base_ctx(a.cache, Xw - 1000, Yn + 1000, Lx / cosl + 2000, Lz + 2000,
                                           (limites["oeste"], limites["sul"], limites["leste"], limites["norte"]))
    base_f = spline_filter(base, order=3).astype(np.float32)

    with rasterio.open("/vsicurl/" + URL_HIRISE) as h:
        th, H, W = h.transform, h.height, h.width
    fr = lambda Y: (th.f - Y) / -th.e - 0.5                # coordenada fracionaria no HiRISE
    fc = lambda X: (X - th.c) / th.a - 0.5
    hr0, hr1 = max(0, int(fr(Yn)) - MARGEM_HIRISE), min(H, int(fr(Ys)) + MARGEM_HIRISE)
    hc0, hc1 = max(0, int(fc(Xw)) - MARGEM_HIRISE), min(W, int(fc(Xe)) + MARGEM_HIRISE)
    hir = ler_hirise(a.cache, hr0, hr1, hc0, hc1)
    print(f"HiRISE janela {hir.shape}  ({time.time() - t0:.0f}s)")

    # ---- faixas de 1 km (uma linha de tiles), resultado em float32 mapeado em disco ----
    z = np.lib.format.open_memmap(a.cache / f"grade_{TX}x{TZ}.npy", mode="w+", dtype=np.float32, shape=(Nz, Nx))
    peso_hirise = np.zeros((TZ, TX), np.float32)
    soma_w = 0.0
    for tz in range(TZ):
        ga, gb = tz * AMOSTRAS_TILE, tz * AMOSTRAS_TILE + AMOSTRAS_TILE + (1 if tz == TZ - 1 else 0)
        n = gb - ga
        # CTX cubico direto na grade do jogo (linha i -> Y = Ys + (ga+i)*d; base tem linha 0 = norte)
        zc = affine_transform(base_f, [-d / RES_BASE, d / cosl / RES_BASE],
                              offset=[(tb.f - (Ys + ga * d)) / RES_BASE - 0.5, (Xw - tb.c) / RES_BASE - 0.5],
                              output_shape=(n, Nx), order=3, mode="nearest", prefilter=False)
        # HiRISE da faixa (com margem), buracos preenchidos com CTX bilinear, peso de transicao
        ya, yb = Ys + ga * d, Ys + (gb - 1) * d
        s0 = max(hr0, int(fr(yb)) - MARGEM_HIRISE); s1 = min(hr1, int(fr(ya)) + MARGEM_HIRISE)
        w = None
        if s1 > s0:
            src = np.array(hir[s0 - hr0:s1 - hr0])
            topo, fundo = s0 == hr0, s1 == hr1              # borda real da janela -> sem dado alem dela
            src = np.pad(src, ((1 if topo else 0, 1 if fundo else 0), (1, 1)), constant_values=np.nan)
            e0, f0 = s0 - (1 if topo else 0), hc0 - 1       # linha/coluna HiRISE da posicao [0,0] de src
            buraco = np.isnan(src)
            if not buraco.all():
                w1 = np.clip(distance_transform_edt(~buraco).astype(np.float32) * abs(th.a) / TRANSICAO_HIRISE_M, 0, 1)
                ctxb = affine_transform(base, [-th.e / RES_BASE, th.a / RES_BASE],
                                        offset=[(tb.f - (th.f + (e0 + 0.5) * th.e)) / RES_BASE - 0.5,
                                                (th.c + (f0 + 0.5) * th.a - tb.c) / RES_BASE - 0.5],
                                        output_shape=src.shape, order=1, mode="nearest")
                src = np.where(buraco, ctxb, src); del ctxb, buraco
                mat = [-d / -th.e, d / cosl / th.a]
                off = [fr(Ys + ga * d) - e0, fc(Xw) - f0]
                zh = affine_transform(src, mat, offset=off, output_shape=(n, Nx), order=3, mode="nearest")
                w = affine_transform(w1, mat, offset=off, output_shape=(n, Nx), order=1, mode="constant", cval=0.0)
                del src, w1
        if w is not None:
            zs = zh * w + zc * (1 - w)
            for tx in range(TX):
                peso_hirise[tz, tx] = float(w[:, tx * 1024: tx * 1024 + 1025].mean())
            soma_w += float(w[: AMOSTRAS_TILE].sum())
            del zh
        else:
            zs = zc
        z[ga:gb] = zs.astype(np.float32)
        print(f"  faixa {tz + 1}/{TZ}  HiRISE {100 * peso_hirise[tz].mean():.0f}%  ({time.time() - t0:.0f}s)", flush=True)
    ex = cfg["exagero_vertical"]
    est = aplicar_edicoes(z, d, edicoes, a.cache, lambda m: stamp_mesa_ctx(a.cache / "ctx_20m.tif", g, m), ex, ox, oz)
    z.flush()
    verificacao = verificar_edicoes(z, d, edicoes, est, nivel_agua, ex, ox, oz)
    frac_hirise = soma_w / ((Nz - 1) * Nx)
    print(f"grade {Nx}x{Nz}, espacamento {d:.6f} m, {100 * frac_hirise:.1f}% do mapa em HiRISE 1 m  ({time.time() - t0:.0f}s)")

    # ---- codificacao 16-bit com UM min/max global ----
    zmin = min(float(z[i:i + 2048].min()) for i in range(0, Nz, 2048))
    zmax = max(float(z[i:i + 2048].max()) for i in range(0, Nz, 2048))
    hmin, hmax = math.floor(zmin - a.margem), math.ceil(zmax + a.margem)
    faixa = hmax - hmin
    passo = faixa / 65535
    cod = lambda t: np.round((np.asarray(t, np.float32) - hmin) / faixa * 65535).astype(np.uint16)

    # ---- tiles Jezero_x_z.raw (x -> leste, z -> norte, (0,0) = sudoeste) + autoverificacao ----
    def arquivo(tx, tz): return a.saida / f"Jezero_{tx}_{tz}.raw"
    for tz in range(TZ):
        for tx in range(TX):
            t = cod(z[tz * 1024: tz * 1024 + 1025, tx * 1024: tx * 1024 + 1025])
            (t[::-1] if a.norte_primeiro else t).astype("<u2").tofile(arquivo(tx, tz))

    def ler(tx, tz):
        t = np.fromfile(arquivo(tx, tz), "<u2").reshape(1025, 1025)
        return t[::-1] if a.norte_primeiro else t
    for tz in range(TZ):
        for tx in range(TX):
            t = ler(tx, tz)
            if tx + 1 < TX: assert np.array_equal(t[:, -1], ler(tx + 1, tz)[:, 0]), (tx, tz, "leste")
            if tz + 1 < TZ: assert np.array_equal(t[-1, :], ler(tx, tz + 1)[0, :]), (tx, tz, "norte")
            ref = z[tz * 1024: tz * 1024 + 1025, tx * 1024: tx * 1024 + 1025]
            assert np.abs(hmin + t * passo - ref).max() <= passo / 2 + 1e-3, (tx, tz, "ida-e-volta")
    print(f"autoverificacao OK ({TX * TZ} tiles)  ({time.time() - t0:.0f}s)")

    # ---- PNG 16-bit do mapa inteiro (1 a cada 2 amostras; norte em cima) ----
    from PIL import Image
    Image.fromarray(cod(z[::2, ::2])[::-1]).save(a.saida / "Jezero_mapa_16bit.png")

    # ---- ponto de inicio: exato, no pad de pouso da base (D16), mapa.json -> inicio_km (referencia) ----
    z4, d4 = np.array(z[::4, ::4]), d * 4
    sx, sz = cfg["inicio_km"][0] * 1000 + g["desloc_x"], cfg["inicio_km"][1] * 1000 + g["desloc_z"]
    sh = float(z[int(round(sz / d)), int(round(sx / d))])

    # ---- area jogavel: poligono no sistema de referencia -> coordenadas com origem no centro do mapa ----
    area = [[x * 1000 + g["desloc_x"] - Lx / 2, zz * 1000 + g["desloc_z"] - Lz / 2]
            for x, zz in cfg.get("area_jogavel_km", {}).get("poligono", [])]

    # ---- preview (hillshade + grade de tiles), reduzido ----
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, matplotlib.patheffects as pe
    from matplotlib.colors import LinearSegmentedColormap
    mars = LinearSegmentedColormap.from_list("mars", ["#2e1d14", "#5a3322", "#8a5233", "#b07a45", "#cfa46a", "#e6caa0", "#f4e6cc"])
    zp, dp = z4[::2, ::2], d4 * 2
    hs = hillshade(gaussian_filter(zp, 1), dp)
    img = np.clip(mars(((zp - zmin) / (zmax - zmin)) ** 0.6)[..., :3] * (0.2 + 1.05 * hs[..., None]), 0, 1)
    fig, ax = plt.subplots(figsize=(13 * TX / max(TX, TZ) + 1, 13 * TZ / max(TX, TZ)), dpi=100)
    ext = [0, TX, 0, TZ]
    ax.imshow(img, extent=ext, origin="lower", interpolation="bilinear")
    ax.contour(zp, levels=[nivel_agua], extent=ext, origin="lower", colors="#8fd0ff", linewidths=1.2)
    stroke = [pe.withStroke(linewidth=2, foreground="black")]
    for v in range(TX + 1): ax.axvline(v, color="white", lw=.4, alpha=.5)
    for v in range(TZ + 1): ax.axhline(v, color="white", lw=.4, alpha=.5)
    for tz in range(TZ):
        for tx in range(TX):
            ax.text(tx + .05, tz + .95, f"{tx}_{tz}", color="white", fontsize=5, va="top", path_effects=stroke)
    if area:
        pa = np.array(area + area[:1]) / 1000 + [Lx / 2000, Lz / 2000]
        ax.plot(pa[:, 0], pa[:, 1], color="red", lw=2)
    for p in edicoes.get("platos", []):
        ax.plot((p["x_m"] - ox) / 1000, (p["z_m"] - oz) / 1000, marker="s", ms=10, mfc="none", mec="cyan", mew=2)
    km = lambda pts: np.array(pts, float) - [ox / 1000, oz / 1000]          # referencia (km) -> mapa (km)
    for nv in edicoes.get("nivelamentos", []):
        pn = km(nv["poligono_km"] + nv["poligono_km"][:1]); ax.plot(pn[:, 0], pn[:, 1], color="cyan", lw=1.5)
    for t in edicoes.get("trilhas", []):
        pt = km(t["polilinha_km"]); ax.plot(pt[:, 0], pt[:, 1], color="yellow", lw=1.5)
    ax.plot(sx / 1000, sz / 1000, marker="*", ms=20, color="yellow", mec="black")
    ax.set_xlim(0, TX); ax.set_ylim(0, TZ)
    ax.set_xlabel("x (km, oeste -> leste)"); ax.set_ylabel("z (km, sul -> norte)")
    ax.set_title(f"Jezero {TX}x{TZ} km - {hmin} a {hmax} m | azul: agua em {nivel_agua:.0f} m | vermelho: area jogavel\n"
                 f"estrela: inicio | quadrado: plato | ciano: nivelamento | amarelo: trilha | HiRISE 1 m em {100 * frac_hirise:.0f}% do mapa", fontsize=11)
    plt.tight_layout(); prev = a.saida / "preview.png"; plt.savefig(prev); plt.close(fig)
    Image.open(prev).convert("RGB").quantize(256, method=Image.Quantize.MEDIANCUT).save(prev, optimize=True)

    # ---- metadata ----
    norm = lambda h: (h - hmin) / faixa
    meta = {
        "arquivos": {"tiles": "Jezero_{x}_{z}.raw", "indice": "x = leste (0 = oeste), z = norte (0 = sul); (0,0) = canto sudoeste",
                     "formato": "RAW uint16 little-endian (Windows), 1025x1025, sem cabecalho",
                     "linha_0_do_raw": "NORTE (ativar Flip Vertically no Unity)" if a.norte_primeiro else "SUL (Unity padrao, sem Flip Vertically)",
                     "bordas": f"tiles vizinhos compartilham a linha/coluna de borda (grade global {Nx}x{Nz} -> tile = amostras [i*1024 .. i*1024+1024])",
                     "png_16bit": "Jezero_mapa_16bit.png: mapa inteiro, 1 a cada 2 amostras, NORTE em cima (convencao de imagem)"},
        "grade": {"tiles_x": TX, "tiles_z": TZ, "tamanho_tile_m": 1000.0, "amostras_por_tile": 1025,
                  "amostras_x": Nx, "amostras_z": Nz, "espacamento_m": d, "tamanho_x_m": Lx, "tamanho_z_m": Lz},
        "referencia": {"desloc_x_m": g["desloc_x"], "desloc_z_m": g["desloc_z"],
                       "uso": "coordenada_mapa = coordenada_referencia + desloc (edicoes, inicio e area jogavel usam a referencia)"},
        "altura": {"min_real_m": round(zmin, 3), "max_real_m": round(zmax, 3), "margem_m": a.margem,
                   "min_codificado_m": hmin, "max_codificado_m": hmax, "faixa_m": faixa,
                   "precisao_por_degrau_m": passo, "decodificar": "h_m = min_codificado_m + valor/65535 * faixa_m",
                   "alturas_reais_sem_exagero": True},
        "unity": {"terrain_size": {"x": 1000.0, "y": faixa * ex, "z": 1000.0}, "heightmap_resolution": 1025,
                  "exagero_vertical": ex,
                  "y_mundo": "y = (h_m - min_codificado_m) * exagero_vertical (terreno em y=0)",
                  "posicao_tile_origem_no_centro": f"tile (x,z) em ({{x}}*1000 - {Lx / 2:.0f}, 0, {{z}}*1000 - {Lz / 2:.0f})"},
        "agua": {"nivel_m": nivel_agua, "normalizado": norm(nivel_agua), "y_mundo_com_exagero": (nivel_agua - hmin) * ex},
        "inicio_jogador": {"x_m": round(sx, 1), "z_m": round(sz, 1), "tile": [int(sx // 1000), int(sz // 1000)],
                           "altura_m": round(sh, 2), "normalizado": norm(sh), "y_mundo_com_exagero": (sh - hmin) * ex,
                           "criterio": f"mapa.json inicio_km {cfg['inicio_km']} (referencia): pad de pouso da base (D16)"},
        "area_jogavel": {"poligono_m_centro": area, "sistema": "metros, origem no centro do mapa, x leste, z norte"},
        "geo": {"centro_lat": lat_c, "limites_graus": limites,
                "projecao": "Equiretangular Mars 2000 esfera (R=3396190 m, lat_ts=0); largura L-O corrigida por cos(lat do centro)",
                "correcao_cos_lat": cosl},
        "fontes": {"hirise_dtm_1m": URL_HIRISE, "ctx_dtm_20m": URL_CTX, "ctx_dtms_catalogo": ctx_usados,
                   "licenca": "Dominio publico (USGS / CC0)", "citacao": [CITACAO, CITACAO_STAC],
                   "fracao_mapa_hirise": frac_hirise,
                   "uso_ctx": f"onde nao ha HiRISE (transicao de {TRANSICAO_HIRISE_M:.0f} m); catalogo so fora do mosaico CTX (transicao de {TRANSICAO_CTX_M:.0f} m)"},
        "hirise_por_tile": np.round(peso_hirise, 3).tolist(),
        "reamostragem": "B-spline cubica (scipy affine_transform order=3)",
        "mapa": cfg,
        "edicoes": edicoes,
        "verificacao_edicoes": verificacao,
    }
    (a.saida / "metadata.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: meta[k] for k in ("altura", "agua", "inicio_jogador")}, indent=1, ensure_ascii=False))
    print(f"limites: {limites}\npronto em {time.time() - t0:.0f}s -> {a.saida}")


if __name__ == "__main__":
    main()
