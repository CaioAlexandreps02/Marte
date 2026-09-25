"""Preview das edicoes do terreno SEM os tiles (roda em qualquer PC com cache/ctx_20m.tif).

Monta uma grade a partir do mosaico CTX 20 m em cache, aplica TODAS as edicoes do edicoes.json com as MESMAS funcoes
do exportar_heightmap.py (aplicar_edicoes / verificar_edicoes) e desenha antes/depois:
  20_edicoes_aplicadas.png  mapa inteiro (grade 20 m): relevo antes/depois, inclinacao no jogo, diferenca
  21_base_depois.png        zoom da base (grade 5 m, CTX reamostrado)
  22_trilha_do_mirante.png  zoom da trilha (grade 2 m) + perfil
O CTX e mais liso que o HiRISE 1 m do jogo: os numeros aqui sao uma boa estimativa, os do exportador valem.
Fora do mosaico CTX (x > ~26 km ou z > ~21 km de referencia) a grade e preenchida com o vizinho mais proximo (hachurado).

Uso:  python preview_edicoes.py [--saida ../../referencias/terreno]
"""
import argparse, json
from pathlib import Path

import numpy as np
import rasterio
from scipy.ndimage import distance_transform_edt, gaussian_filter, map_coordinates

import exportar_heightmap as ex

AQUI = Path(__file__).resolve().parent
COR = {"caverna": "#5FE3FF", "mesa": "#FF9F1C", "real": "#9BE37A", "historia": "#D7B8FF", "recurso": "#FFE066",
       "formacao": "#E8C9A0", "mirante": "#FFE14D", "base": "#FFFFFF", "inicio": "#FFFFFF"}


def grade_ctx(caminho, g, x0, x1, z0, z1, d, ordem):
    """Grade (linha 0 = sul) de referencia km [x0,x1]x[z0,z1] com passo d (m). Devolve z, sem_dado, origem (m)."""
    xs, zs = np.arange(x0 * 1000, x1 * 1000 + d / 2, d), np.arange(z0 * 1000, z1 * 1000 + d / 2, d)
    with rasterio.open(caminho) as s:
        a, t = s.read(1).astype(np.float32), s.transform
    falta = ~(a > -30000)
    a = a[tuple(distance_transform_edt(falta, return_distances=False, return_indices=True))]
    a = np.where(falta, gaussian_filter(a, 25), a)                          # sem dado: liso (so para desenhar)
    lin = (g["Ys"] + zs + g["desloc_z"] - t.f) / t.e - 0.5
    col = (g["Xw"] + (xs + g["desloc_x"]) / g["cosl"] - t.c) / t.a - 0.5
    L, C = np.meshgrid(lin, col, indexing="ij")
    z = map_coordinates(a, [L, C], order=ordem, mode="nearest").astype(np.float32)
    sem = map_coordinates(falta.astype(np.float32), [L, C], order=0, mode="constant", cval=1) > 0.5
    return z, sem, (xs[0], zs[0])


def inclinacao_jogo(z, d, exagero):
    gz, gx = np.gradient(gaussian_filter(z, 1) * exagero, d)
    return np.degrees(np.arctan(np.hypot(gx, gz)))


def relevo_rgb(z, d, zmin, zmax, exagero):
    from matplotlib.colors import LinearSegmentedColormap
    mars = LinearSegmentedColormap.from_list("mars", ["#2e1d14", "#5a3322", "#8a5233", "#b07a45", "#cfa46a", "#e6caa0", "#f4e6cc"])
    hs = ex.hillshade(gaussian_filter(z, 0.7) * exagero, d)
    return np.clip(mars(np.clip((z - zmin) / (zmax - zmin), 0, 1) ** 0.6)[..., :3] * (0.2 + 1.05 * hs[..., None]), 0, 1)


def desenhar_edicoes(ax, ed, cfg, marcos=None, rotulos=True):
    import matplotlib.patheffects as pe
    st = [pe.withStroke(linewidth=2.2, foreground="black")]
    P = np.array(cfg["area_jogavel_km"]["poligono"] + cfg["area_jogavel_km"]["poligono"][:1])
    ax.plot(P[:, 0], P[:, 1], color="white", lw=1.4, label="área jogável (Var. A + corredor)")
    for nv in ed.get("nivelamentos", []):
        q = np.array(nv["poligono_km"] + nv["poligono_km"][:1]); ax.plot(q[:, 0], q[:, 1], color="#00E5FF", lw=1.6, label="nivelamento (base)")
    for t in ed.get("trilhas", []):
        q = np.array(t["polilinha_km"]); ax.plot(q[:, 0], q[:, 1], color="#FFE14D", lw=1.6, label="trilha do Mirante")
    for c in ed.get("canyons", []):
        a, b = np.array(c["de_km"]), np.array(c["ate_km"]); e = (b - a) / np.linalg.norm(b - a); p = np.array([-e[1], e[0]]) * c["largura_km"] / 2
        q = np.array([a + p, b + p, b - p, a - p, a + p]); ax.plot(q[:, 0], q[:, 1], "--", color="#FF4FD8", lw=1.2, label="canyon (faixa do stamp)")
    ang = np.linspace(0, 2 * np.pi, 60)
    for p in ed.get("pocos", []):
        ax.plot(p["x_km"] + p["raio_m"] / 1000 * np.cos(ang), p["z_km"] + p["raio_m"] / 1000 * np.sin(ang), color="#FF4FD8", lw=1.2)
    for m in ed.get("mesas", []):
        ax.plot(m["x_km"] + m["base_raio_m"] / 1000 * np.cos(ang), m["z_km"] + m["base_raio_m"] / 1000 * np.sin(ang), color="#FF9F1C", lw=1.2)
    for p in ed.get("platos", []):
        ax.plot(p["x_m"] / 1000 + p["raio_m"] / 1000 * np.cos(ang), p["z_m"] / 1000 + p["raio_m"] / 1000 * np.sin(ang), color="#00E5FF", lw=1)
    for m in marcos or []:
        mk = {"caverna": "v", "mesa": "^", "mirante": "P", "base": "s", "inicio": "*"}.get(m["tipo"], "o")
        ax.plot(m["x_km"], m["z_km"], mk, color=COR[m["tipo"]], mec="black", ms=12 if mk == "*" else 7, zorder=5)
        if rotulos and m["numero"]:
            ax.text(m["x_km"] + 0.12, m["z_km"] + 0.08, str(m["numero"]), color=COR[m["tipo"]], fontsize=7.5, weight="bold", path_effects=st, zorder=6, clip_on=True)


def salvar(fig, caminho, dpi):
    import matplotlib.pyplot as plt
    from PIL import Image
    fig.savefig(caminho, dpi=dpi, facecolor=fig.get_facecolor()); plt.close(fig)
    Image.open(caminho).convert("RGB").quantize(256, method=Image.Quantize.MEDIANCUT).save(caminho, optimize=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--saida", type=Path, default=AQUI.parents[1] / "referencias" / "terreno")
    a = ap.parse_args()
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    cfg = json.loads((AQUI / "mapa.json").read_text(encoding="utf-8"))
    ed = json.loads((AQUI / "edicoes.json").read_text(encoding="utf-8"))
    marcos = json.loads((AQUI / "marcos.json").read_text(encoding="utf-8"))["marcos"]
    g = ex.geometria(cfg)
    cache, ctx = AQUI / "cache", AQUI / "cache" / "ctx_20m.tif"
    exg, agua = cfg["exagero_vertical"], float(cfg["nivel_agua_m"])
    stamp = lambda m: ex.stamp_mesa_ctx(ctx, g, m)
    x0, z0 = -g["desloc_x"] / 1000, -g["desloc_z"] / 1000                  # canto SW do mapa em referencia
    x1, z1 = x0 + g["Lx"] / 1000, z0 + g["Lz"] / 1000

    def rodar(ext, d, ordem):
        z, sem, (ox, oz) = grade_ctx(ctx, g, *ext, d, ordem)
        antes = z.copy()
        est = ex.aplicar_edicoes(z, d, ed, cache, stamp, exg, ox, oz)
        ver = ex.verificar_edicoes(z, d, ed, est, agua, exg, ox, oz)
        return antes, z, sem, ver

    # ---------------- 20: mapa inteiro, 20 m ----------------
    print("== mapa inteiro (20 m)")
    ext = (x0, x1, z0, z1)
    antes, depois, sem, ver = rodar(ext, 20.0, 1)
    im_ext = [x0, x1, z0, z1]
    zmin, zmax = np.percentile(antes, 0.5), np.percentile(antes, 99.8)
    fig, axs = plt.subplots(2, 2, figsize=(22, 20), facecolor="#1b1917")
    paineis = [(axs[0, 0], "Antes (CTX 20 m, sem edições)", relevo_rgb(antes, 20, zmin, zmax, exg), None),
               (axs[0, 1], "Depois: todas as edições do edicoes.json + marcos.json", relevo_rgb(depois, 20, zmin, zmax, exg), None),
               (axs[1, 0], "Inclinação no jogo depois (exagero 2×, escala ~40 m), 0–35°", np.where(sem, np.nan, inclinacao_jogo(depois, 20, exg)), dict(cmap="magma", vmin=0, vmax=35)),
               (axs[1, 1], "Diferença depois − antes (m reais), ±60 m", depois - antes, dict(cmap="BrBG", vmin=-60, vmax=60))]
    for ax, tit, img, kw in paineis:
        h = ax.imshow(img, extent=im_ext, origin="lower", interpolation="bilinear", **(kw or {}))
        ax.contourf(sem.astype(float), levels=[0.5, 1.5], extent=im_ext, origin="lower", colors="none", hatches=["////"])
        ax.contour(depois if ax is not axs[0, 0] else antes, levels=[agua], extent=im_ext, origin="lower", colors="#8fd0ff", linewidths=0.8)
        desenhar_edicoes(ax, ed, cfg, marcos if ax is not axs[0, 0] else None, rotulos=ax is axs[0, 1])
        if kw:
            plt.colorbar(h, ax=ax, fraction=0.035, pad=0.01).ax.tick_params(colors="w")
        ax.set_title(tit, color="w", fontsize=13); ax.tick_params(colors="w"); ax.set_xlim(x0, x1); ax.set_ylim(z0, z1)
        ax.set_facecolor("#1b1917")
    h, l = axs[0, 1].get_legend_handles_labels(); u = dict(zip(l, h))
    axs[0, 1].legend(u.values(), u.keys(), fontsize=9, loc="lower right", facecolor="#262320", labelcolor="w")
    b = ver["nivelamentos"].get("base_central", {}); ms = ver["mesas"]
    fig.suptitle("20 · Edições D15/D16 aplicadas (preview_edicoes.py, mesmas funções do exportar_heightmap.py) · km de referência\n"
                 "hachurado: fora do CTX em cache (sem dado) · "
                 f"base: inclinação mediana {b.get('incl_mediana_jogo_graus')}° no jogo, chão ≥ {b.get('acima_da_agua_min_m')} m acima da água\n"
                 "mesas (ganho do cume): " + " · ".join(f"{k} +{v['somado_m']:.0f} m" for k, v in ms.items()), color="w", fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.95]); a.saida.mkdir(parents=True, exist_ok=True)
    salvar(fig, a.saida / "20_edicoes_aplicadas.png", 75)

    # ---------------- 21: base, 5 m ----------------
    print("== base (5 m)")
    ext = (11.3, 17.3, 10.9, 16.4)
    antes, depois, _, verb = rodar(ext, 5.0, 3)
    e = list(ext); zmin, zmax = np.percentile(antes, 1), np.percentile(depois, 99.9)
    fig, axs = plt.subplots(1, 3, figsize=(27, 9.5), facecolor="#1b1917")
    sa, sd = inclinacao_jogo(antes, 5, exg), inclinacao_jogo(depois, 5, exg)
    for ax, tit, img, kw in [(axs[0], "Relevo depois (sombreado, exagero 2×)", relevo_rgb(depois, 5, zmin, zmax, exg), None),
                             (axs[1], "Inclinação no jogo ANTES, 0–15°", sa, dict(cmap="viridis", vmin=0, vmax=15)),
                             (axs[2], "Inclinação no jogo DEPOIS, 0–15°", sd, dict(cmap="viridis", vmin=0, vmax=15))]:
        h = ax.imshow(img, extent=e, origin="lower", interpolation="bilinear", **(kw or {}))
        ax.contour(depois if "DEPOIS" in tit or "depois" in tit else antes, levels=np.arange(-2600, -2300, 10), extent=e, origin="lower", colors="k", linewidths=0.3, alpha=0.5)
        desenhar_edicoes(ax, ed, cfg, marcos)
        if kw:
            plt.colorbar(h, ax=ax, fraction=0.04, pad=0.01).ax.tick_params(colors="w")
        ax.set_title(tit, color="w", fontsize=13); ax.tick_params(colors="w"); ax.set_xlim(e[0], e[1]); ax.set_ylim(e[2], e[3])
    b = verb["nivelamentos"]["base_central"]; mt = verb["mesas"]["mesa_do_terraco"]
    fig.suptitle(f"21 · Base B2 depois do nivelamento (CTX reamostrado a 5 m) · inclinação mediana {b['incl_mediana_jogo_graus']}° (p90 {b['incl_p90_jogo_graus']}°) no jogo · "
                 f"chão mín. {b['chao_min_m']} m = {b['acima_da_agua_min_m']} m acima da água · Mesa do Terraço {mt['topo_antes_m']} → {mt['topo_depois_m']} m", color="w", fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.94]); salvar(fig, a.saida / "21_base_depois.png", 70)

    # ---------------- 22: trilha, 2 m ----------------
    print("== trilha (2 m)")
    ext = (3.3, 5.5, 10.95, 13.15)
    antes, depois, _, vert = rodar(ext, 2.0, 3)
    e = list(ext)
    fig = plt.figure(figsize=(27, 10), facecolor="#1b1917")
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.25])
    for k, (tit, zz) in enumerate([("Inclinação no jogo ANTES, 0–40°", antes), ("Inclinação no jogo DEPOIS, 0–40°", depois)]):
        ax = fig.add_subplot(gs[k])
        h = ax.imshow(inclinacao_jogo(zz, 2, exg), extent=e, origin="lower", cmap="magma", vmin=0, vmax=40, interpolation="bilinear")
        ax.contour(zz, levels=np.arange(-2200, -1700, 20), extent=e, origin="lower", colors="w", linewidths=0.3, alpha=0.4)
        desenhar_edicoes(ax, ed, cfg, marcos)
        plt.colorbar(h, ax=ax, fraction=0.04, pad=0.01).ax.tick_params(colors="w")
        ax.set_title(tit, color="w", fontsize=13); ax.tick_params(colors="w"); ax.set_xlim(e[0], e[1]); ax.set_ylim(e[2], e[3])
    ax = fig.add_subplot(gs[2]); ax.set_facecolor("#262320")
    t = ed["trilhas"][0]
    pts = ex.perfil_trilha(t, 5.0) - [3300, 10950]
    s = np.arange(len(pts)) * 5 / 1000
    for zz, cor, nome in [(antes, "#9a8f84", "antes"), (depois, "#FFE14D", "depois (leito)")]:
        hh = map_coordinates(zz, [pts[:, 1] / 2, pts[:, 0] / 2], order=1)
        ax.plot(s, hh, color=cor, lw=1.6, label=f"altura {nome}")
        inc = np.degrees(np.arctan(exg * np.abs(np.diff(hh)) / 5))
        ax2 = ax.twinx() if nome == "antes" else ax2
        ax2.plot(s[1:], inc, color=cor, lw=0.7, alpha=0.8)
    ax2.axhline(25, color="#5FE3FF", lw=0.8); ax2.set_ylim(0, 45); ax2.set_ylabel("inclinação no jogo (°, linhas finas)", color="w"); ax2.tick_params(colors="w")
    ax.set_xlabel("distância ao longo da trilha (km)", color="w"); ax.set_ylabel("altura real (m)", color="w"); ax.tick_params(colors="w")
    ax.legend(loc="upper left", facecolor="#262320", labelcolor="w"); ax.set_title("Perfil da trilha (passo 5 m)", color="w", fontsize=13)
    v = vert["trilhas"][t["nome"]]
    fig.suptitle(f"22 · Trilha do Mirante (CTX reamostrado a 2 m) · leito {t['largura_m']} m, limite {t['max_inclinacao_jogo_graus']}° · "
                 f"eixo antes máx {v['incl_max_eixo_jogo_antes_graus']}° → final máx {v['incl_max_final_jogo_graus']}° (p95 {v['incl_p95_final_jogo_graus']}°), "
                 f"{v['trechos_acima_25_graus_m']} m acima de 25° · maior corte {v['maior_corte_m']} m", color="w", fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.94]); salvar(fig, a.saida / "22_trilha_do_mirante.png", 70)

    print(json.dumps({"mapa_20m": ver, "base_5m": verb, "trilha_2m": vert}, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
