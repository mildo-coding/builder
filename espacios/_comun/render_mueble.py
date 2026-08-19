"""Lámina de ficha + renders de un mueble (planta, alzado, isométrico)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle

from .estilo import PALETA, aplicar_estilo
from .paths import salidas_espacio

Spec = dict[str, Any]


def _iso(x: float, y: float, z: float) -> tuple[float, float]:
    return (x - y) * 0.82, z + (x + y) * 0.42


def _face(ax, pts, color, edge="#2b1d10", z=3, alpha=1.0) -> None:
    ax.add_patch(
        Polygon(
            [_iso(*p) for p in pts],
            closed=True,
            facecolor=color,
            edgecolor=edge,
            lw=0.7,
            alpha=alpha,
            zorder=z,
        )
    )


def _color(spec: Spec) -> str:
    mats = spec.get("materiales") or []
    if mats:
        return PALETA.get(mats[0].get("clave", "roble"), PALETA["roble"])
    return PALETA["roble"]


def dibujar_isometrico(ax, spec: Spec) -> None:
    ax.set_aspect("equal")
    ax.axis("off")
    a, f, h = spec["frente"], spec["profundidad"], spec["alto"]
    # El frente del mueble mira a +Y en el isométrico local (ancho en X, fondo en Y)
    w, d = a, f
    col = _color(spec)
    col_lado = PALETA.get("madera_oscura", "#5c4030")
    col_top = PALETA.get("blanco", "#f4f1ea")
    tipo = spec.get("tipo", "placard")

    if tipo in ("panel", "espejo", "vidrio"):
        d = max(d, 0.06)
        col_top = col

    # caras (orden: fondo, izq, der, tapa, frente)
    _face(ax, [(0, d, 0), (w, d, 0), (w, d, h), (0, d, h)], col_lado, z=1)
    _face(ax, [(0, 0, 0), (0, d, 0), (0, d, h), (0, 0, h)], col_lado, z=2)
    _face(ax, [(w, 0, 0), (w, d, 0), (w, d, h), (w, 0, h)], col_lado, z=2)
    _face(ax, [(0, 0, h), (w, 0, h), (w, d, h), (0, d, h)], col_top, z=4)
    _face(ax, [(0, 0, 0), (w, 0, 0), (w, 0, h), (0, 0, h)], col, z=5)

    if tipo in ("placard", "vanitory", "estanteria"):
        # división de hojas
        xmid = w / 2
        p1 = _iso(xmid, 0, 0.04)
        p2 = _iso(xmid, 0, h - 0.04)
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="#2b1d10", lw=0.6, zorder=6)
        for hx in (w * 0.46, w * 0.54):
            q1 = _iso(hx, 0, h * 0.48)
            q2 = _iso(hx, 0, h * 0.52)
            ax.plot([q1[0], q2[0]], [q1[1], q2[1]], color="#1a1a1a", lw=1.4, zorder=7)

    if tipo == "mesa":
        # patas
        for px, py in ((0.08, 0.08), (w - 0.08, 0.08), (0.08, d - 0.08), (w - 0.08, d - 0.08)):
            _face(
                ax,
                [(px - 0.03, py - 0.03, 0), (px + 0.03, py - 0.03, 0),
                 (px + 0.03, py - 0.03, h * 0.92), (px - 0.03, py - 0.03, h * 0.92)],
                PALETA["metal"],
                edge="#111",
                z=6,
            )

    if tipo == "sofa":
        _face(ax, [(0.08, 0.08, h * 0.45), (w - 0.08, 0.08, h * 0.45),
                   (w - 0.08, d * 0.55, h * 0.45), (0.08, d * 0.55, h * 0.45)],
              PALETA["lino"], z=6)
        _face(ax, [(0.08, d * 0.55, h * 0.45), (w - 0.08, d * 0.55, h * 0.45),
                   (w - 0.08, d * 0.55, h), (0.08, d * 0.55, h)],
              PALETA["lino"], z=6)

    if tipo == "cama":
        _face(ax, [(0.05, 0.05, h), (w - 0.05, 0.05, h),
                   (w - 0.05, d - 0.05, h), (0.05, d - 0.05, h)],
              "#f7f4ee", z=6, edge="#cfc6b6")

    if tipo in ("pileta", "vanitory"):
        # bacha
        bx0, bx1 = w * 0.18, w * 0.82
        by0, by1 = d * 0.2, d * 0.8
        _face(ax, [(bx0, by0, h + 0.02), (bx1, by0, h + 0.02),
                   (bx1, by1, h + 0.02), (bx0, by1, h + 0.02)],
              PALETA["silestone"], z=7)

    # cotas isométricas simples
    p0 = _iso(0, 0, 0)
    p1 = _iso(w, 0, 0)
    ax.text((p0[0] + p1[0]) / 2, min(p0[1], p1[1]) - 0.12, f"{a:.2f} m",
            ha="center", va="top", fontsize=7, fontname="Arial")

    xs, ys = zip(*[_iso(x, y, z) for x in (0, w) for y in (0, d) for z in (0, h)])
    pad = 0.35
    ax.set_xlim(min(xs) - pad, max(xs) + pad)
    ax.set_ylim(min(ys) - pad, max(ys) + pad)
    ax.set_title("ISOMÉTRICO", loc="left", fontsize=8, pad=4)


def dibujar_alzado(ax, spec: Spec) -> None:
    ax.set_aspect("equal")
    ax.axis("off")
    w, h = spec["frente"], spec["alto"]
    col = _color(spec)
    ax.add_patch(Rectangle((0, 0), w, h, facecolor=col, edgecolor="#1a1a1a", lw=1.1))
    if spec.get("tipo") in ("placard", "vanitory", "estanteria"):
        ax.plot([w / 2, w / 2], [0.04, h - 0.04], color="#1a1a1a", lw=0.6)
    ax.plot([0, w], [0, 0], color="#888", lw=2)
    ax.text(w / 2, -0.18, f"{w:.2f}", ha="center", fontsize=7, fontname="Arial")
    ax.text(w + 0.12, h / 2, f"{h:.2f}", ha="left", va="center", fontsize=7,
            fontname="Arial", rotation=90)
    ax.set_xlim(-0.3, w + 0.45)
    ax.set_ylim(-0.4, h + 0.35)
    ax.set_title("ALZADO FRENTE", loc="left", fontsize=8, pad=4)


def dibujar_planta(ax, spec: Spec) -> None:
    ax.set_aspect("equal")
    ax.axis("off")
    w, d = spec["w"], spec["d"]
    col = _color(spec)
    ax.add_patch(Rectangle((0, 0), w, d, facecolor=col, edgecolor="#1a1a1a",
                           lw=1.1, hatch="///", alpha=0.9))
    # flecha de frente
    fx = {"N": (w / 2, d, 0, 0.22), "S": (w / 2, 0, 0, -0.22),
          "E": (w, d / 2, 0.22, 0), "O": (0, d / 2, -0.22, 0)}
    x, y, dx, dy = fx.get(spec.get("frente_hacia", "N"), (w / 2, d, 0, 0.22))
    ax.annotate("", xy=(x + dx, y + dy), xytext=(x, y),
                arrowprops=dict(arrowstyle="-|>", color="#1a1a1a", lw=0.9))
    ax.text(x + dx, y + dy, "frente", fontsize=6, ha="center", va="bottom", fontname="Arial")
    ax.text(w / 2, -0.16, f"{w:.2f}", ha="center", fontsize=7, fontname="Arial")
    ax.text(-0.12, d / 2, f"{d:.2f}", ha="right", va="center", fontsize=7,
            fontname="Arial", rotation=90)
    ax.set_xlim(-0.45, w + 0.45)
    ax.set_ylim(-0.4, d + 0.45)
    ax.set_title("PLANTA", loc="left", fontsize=8, pad=4)


def dibujar_materiales(ax, spec: Spec) -> None:
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("MATERIALES Y TEXTURAS", loc="left", fontsize=8, pad=4)
    y = 0.92
    for mat in spec.get("materiales") or []:
        col = PALETA.get(mat.get("clave", "roble"), "#ccc")
        ax.add_patch(Rectangle((0.02, y - 0.07), 0.10, 0.07, facecolor=col,
                               edgecolor="#1a1a1a", lw=0.5, transform=ax.transAxes))
        ax.text(0.15, y - 0.02, f"{mat['nombre']}", fontsize=7.5, fontname="Arial",
                va="top", transform=ax.transAxes, fontweight="bold")
        ax.text(0.15, y - 0.055, mat.get("uso", ""), fontsize=6.4, fontname="Arial",
                va="top", color="#444", transform=ax.transAxes)
        y -= 0.14
    ax.text(0.02, 0.28, "TEXTURA", fontsize=7, fontname="Arial", fontweight="bold",
            transform=ax.transAxes)
    ax.text(0.02, 0.24, spec.get("texturas", ""), fontsize=6.5, fontname="Arial",
            va="top", wrap=True, transform=ax.transAxes)
    comps = spec.get("componentes") or []
    ax.text(0.02, 0.08, " · ".join(comps), fontsize=6, fontname="Arial",
            color="#333", va="top", transform=ax.transAxes)


def generar_lamina(spec: Spec, espacio_dir: Path | None = None) -> Path:
    aplicar_estilo()
    slug = spec.get("espacio_slug") or (espacio_dir.name if espacio_dir else "")
    out = salidas_espacio(slug)
    fig = plt.figure(figsize=(14.5, 9.2), dpi=160)
    fig.subplots_adjust(left=0.05, right=0.97, top=0.86, bottom=0.07)
    fig.add_artist(FancyBboxPatch((0.02, 0.03), 0.96, 0.94, boxstyle="square,pad=0",
                                  fill=False, edgecolor="#1a1a1a", lw=0.8,
                                  transform=fig.transFigure))
    fig.text(0.05, 0.94, f"BERUTI 3336  ·  {spec.get('espacio_nombre', slug).upper()}",
             fontsize=8, color="#666")
    fig.text(0.05, 0.905, spec["nombre"].upper(), fontsize=14, fontweight="bold")
    fig.text(0.97, 0.94, f"FURNITURE_{spec['id']}", fontsize=8, color="#666", ha="right")
    fig.text(0.97, 0.905,
             f"{spec['frente']:.3f} × {spec['profundidad']:.3f} × {spec['alto']:.3f} m",
             fontsize=9, ha="right")

    gs = fig.add_gridspec(2, 3, width_ratios=[1.15, 0.9, 0.85], height_ratios=[1.15, 0.9],
                          wspace=0.18, hspace=0.28)
    ax_iso = fig.add_subplot(gs[:, 0])
    ax_alz = fig.add_subplot(gs[0, 1])
    ax_pl = fig.add_subplot(gs[1, 1])
    ax_mat = fig.add_subplot(gs[:, 2])
    dibujar_isometrico(ax_iso, spec)
    dibujar_alzado(ax_alz, spec)
    dibujar_planta(ax_pl, spec)
    dibujar_materiales(ax_mat, spec)

    fig.text(0.05, 0.045, spec.get("ubicacion", ""), fontsize=7, color="#333")
    dest = out["renders_muebles"] / f"FURNITURE_{spec['id']}.png"
    fig.savefig(dest, dpi=170, bbox_inches="tight", pad_inches=0.12)
    fig.savefig(out["renders_global"] / f"FURNITURE_{spec['id']}.png",
                dpi=170, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    return dest
