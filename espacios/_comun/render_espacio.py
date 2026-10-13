"""Planta genérica y vista axonométrica de un espacio."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle
import matplotlib.patheffects as pe

from .catalogo import espacio as get_espacio
from .estilo import PALETA, aplicar_estilo
from .paths import salidas_espacio
from .render_mueble import _iso

Spec = dict[str, Any]
FX = [pe.withStroke(linewidth=2.8, foreground="#f7f3ea")]


def _color_mueble(m: Spec) -> str:
    mats = m.get("materiales") or []
    if mats:
        return PALETA.get(mats[0].get("clave", "roble"), PALETA["roble"])
    return PALETA["roble"]


def _fmt_m(v: float) -> str:
    s = f"{float(v):.3f}".rstrip("0").rstrip(".")
    return s if s else "0"


def _nombre_corto(nombre: str, max_len: int = 20) -> str:
    n = str(nombre or "").strip()
    while True:
        low = n.casefold()
        if low.startswith("mueble"):
            n = n[6:].lstrip(" :—–-")
            continue
        if low.startswith("placard"):
            n = n[7:].lstrip(" :—–-")
            continue
        break
    n = n.strip() or str(nombre or "").strip()
    return n if len(n) <= max_len else n[:max_len]


def _z_tope(m: Spec) -> float:
    return float(m.get("z0") or 0.0) + float(m.get("alto") or 0.0)


def _huellas_solapan(a: Spec, b: Spec, min_frac: float = 0.25) -> bool:
    """True si las huellas se solapan de forma apreciable en planta."""
    ax0, ay0 = a["x"], a["y"]
    ax1, ay1 = ax0 + a["w"], ay0 + a["d"]
    bx0, by0 = b["x"], b["y"]
    bx1, by1 = bx0 + b["w"], by0 + b["d"]
    ix0, iy0 = max(ax0, bx0), max(ay0, by0)
    ix1, iy1 = min(ax1, bx1), min(ay1, by1)
    if ix1 <= ix0 or iy1 <= iy0:
        return False
    inter = (ix1 - ix0) * (iy1 - iy0)
    area_a = max(a["w"] * a["d"], 1e-6)
    area_b = max(b["w"] * b["d"], 1e-6)
    return inter >= min_frac * min(area_a, area_b)


def _mostrar_nombre_planta(m: Spec, visibles: list[Spec]) -> bool:
    """En solapes, solo el módulo con mayor cota superior (z0+alto)."""
    z = _z_tope(m)
    for o in visibles:
        if o is m:
            continue
        if not _huellas_solapan(m, o):
            continue
        zo = _z_tope(o)
        if zo > z + 1e-6:
            return False
        if abs(zo - z) <= 1e-6 and id(o) < id(m):
            return False
    return True


def _cota_h(ax, x0: float, x1: float, y: float, txt: str | None = None, tick: float = 0.045) -> None:
    if abs(x1 - x0) < 0.03:
        return
    txt = txt or _fmt_m(abs(x1 - x0))
    ax.plot([x0, x1], [y, y], color="#222", lw=0.45, zorder=8)
    ax.plot([x0, x0], [y - tick, y + tick], color="#222", lw=0.45, zorder=8)
    ax.plot([x1, x1], [y - tick, y + tick], color="#222", lw=0.45, zorder=8)
    ax.text((x0 + x1) / 2, y + 0.015, txt, ha="center", va="bottom",
            fontsize=5.6, fontname="Arial", color="#111", zorder=9)


def _cota_v(ax, x: float, y0: float, y1: float, txt: str | None = None, tick: float = 0.045) -> None:
    if abs(y1 - y0) < 0.03:
        return
    txt = txt or _fmt_m(abs(y1 - y0))
    ax.plot([x, x], [y0, y1], color="#222", lw=0.45, zorder=8)
    ax.plot([x - tick, x + tick], [y0, y0], color="#222", lw=0.45, zorder=8)
    ax.plot([x - tick, x + tick], [y1, y1], color="#222", lw=0.45, zorder=8)
    ax.text(x - 0.02, (y0 + y1) / 2, txt, ha="right", va="center",
            fontsize=5.6, fontname="Arial", color="#111", zorder=9, rotation=90)


def _dibujar_muebles_planta(ax, esp: Spec) -> None:
    W, L, _H = _dim_local(esp)
    visibles = [m for m in esp["muebles"].values() if m.get("en_planta", True)]
    # Dibujar de abajo hacia arriba para que los elevados queden encima.
    visibles_draw = sorted(visibles, key=_z_tope)
    for m in visibles_draw:
        overhead = _es_overhead(m)
        ls = (0, (3, 1.8)) if overhead else None
        ax.add_patch(Rectangle(
            (m["x"], m["y"]), m["w"], m["d"],
            facecolor=_color_mueble(m),
            edgecolor="#2b1d10",
            lw=0.75,
            linestyle=ls or "solid",
            zorder=3,
            alpha=0.55 if overhead else 0.92,
        ))
        saturada = _pared_saturada(esp, m, W, L)
        grande = _modulo_grande(m) and not _cubierto_por_mesada(m, visibles)
        if _mostrar_nombre_planta(m, visibles):
            cx, cy = m["x"] + m["w"] / 2, m["y"] + m["d"] / 2
            label = _nombre_corto(m["nombre"])
            fs = 5.2 if min(m["w"], m["d"]) >= 0.35 else 4.4
            ax.text(cx, cy, label, ha="center", va="center", fontsize=fs,
                    fontname="Arial", color="#1a1a1a", zorder=4,
                    linespacing=1.15, path_effects=FX)
        if not saturada or grande:
            _cota_h(ax, m["x"], m["x"] + m["w"], m["y"] - 0.07)
            _cota_v(ax, m["x"] - 0.07, m["y"], m["y"] + m["d"])


def _dibujar_cotas_local(ax, esp: Spec, W: float, L: float) -> None:
    wn = float(esp.get("ancho_norte") or W)
    ws = float(esp.get("ancho_sur") or W)
    _cota_h(ax, 0, ws, -0.42, txt=_fmt_m(ws) if abs(ws - wn) < 0.01 else f"{_fmt_m(ws)} sur")
    if abs(ws - wn) >= 0.01:
        _cota_h(ax, 0, wn, L + 0.42, txt=f"{_fmt_m(wn)} norte")
    _cota_v(ax, -0.42, 0, L)
    for p in esp.get("puertas") or []:
        off, ancho, muro = p.get("offset", 0.0), p["ancho"], p["muro"]
        if muro == "S":
            _cota_h(ax, off, off + ancho, -0.22)
        elif muro == "N":
            _cota_h(ax, off, off + ancho, L + 0.22)
        elif muro == "E":
            xe = _x_este(esp, off)
            _cota_v(ax, xe + 0.22, off, off + ancho)
        elif muro == "O":
            _cota_v(ax, -0.22, off, off + ancho)


def _muros_obra(esp: Spec) -> set[str]:
    omitidos = {str(m).upper() for m in (esp.get("muros_omitidos") or [])}
    return {"N", "S", "E", "O"} - omitidos


def _dibujar_poche(ax, esp: Spec, T: float, muros: set[str]) -> None:
    """Muros de obra en poche. Omite los lados que no existen. Respeta anchos N ≠ S."""
    W, L, _H = _dim_local(esp)
    wn = float(esp.get("ancho_norte") or W)
    ws = float(esp.get("ancho_sur") or W)
    n, s, e, o = "N" in muros, "S" in muros, "E" in muros, "O" in muros
    x0 = -T if o else 0.0
    y0 = -T if s else 0.0
    if o:
        ax.add_patch(Rectangle((x0, 0), T, L, facecolor="#1a1a1a", edgecolor="none", zorder=1))
    if e:
        ax.add_patch(Rectangle((W, 0), T, L, facecolor="#1a1a1a", edgecolor="none", zorder=1))
    if n:
        ax.add_patch(Rectangle((0, L), wn, T, facecolor="#1a1a1a", edgecolor="none", zorder=1))
    if s:
        ax.add_patch(Rectangle((0, y0), ws, T, facecolor="#1a1a1a", edgecolor="none", zorder=1))
    if n and o:
        ax.add_patch(Rectangle((x0, L), T, T, facecolor="#1a1a1a", edgecolor="none", zorder=1))
    if n and e:
        ax.add_patch(Rectangle((wn, L), T, T, facecolor="#1a1a1a", edgecolor="none", zorder=1))
    if s and o:
        ax.add_patch(Rectangle((x0, y0), T, T, facecolor="#1a1a1a", edgecolor="none", zorder=1))
    if s and e:
        ax.add_patch(Rectangle((ws, y0), T, T, facecolor="#1a1a1a", edgecolor="none", zorder=1))


def _dibujar_contenido_planta(ax, esp: Spec) -> tuple[float, float]:
    W, L, _H = _dim_local(esp)
    T = 0.15
    muros = _muros_obra(esp)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.25, W + 1.45)
    ax.set_ylim(-1.15, L + 1.15)
    _dibujar_poche(ax, esp, T, muros)
    ax.add_patch(Polygon(_contorno(esp), closed=True, facecolor="#f4f1ea",
                         edgecolor="none", zorder=2))
    _dibujar_vanos_planta(ax, esp, W, L, T, muros)
    _dibujar_muebles_planta(ax, esp)
    _dibujar_cotas_local(ax, esp, W, L)
    return W, L


def _dibujar_norte_y_adyacencias(ax, esp: Spec, W: float, L: float) -> None:
    ax.annotate("", xy=(W + 0.70, L - 0.05), xytext=(W + 0.70, L - 0.45),
                arrowprops=dict(arrowstyle="-|>", color="#111", lw=1.0))
    ax.text(W + 0.70, L + 0.02, "N", ha="center", fontsize=8, fontweight="bold")
    adj = esp.get("adjacencias") or {}
    if "N" in adj:
        ax.text(W / 2, L + 0.55, f"↑  {adj['N']}", ha="center", fontsize=7, color="#666")
    if "S" in adj:
        ax.text(W / 2, -0.95, adj["S"], ha="center", fontsize=7, color="#666")
    if "E" in adj:
        ax.text(W + 0.85, L / 2, f"{adj['E']} →", ha="left", va="center", fontsize=7, color="#666")
    if "O" in adj:
        ax.text(-0.95, L / 2, f"← {adj['O']}", ha="right", va="center", fontsize=7, color="#666")


def _tabla_medidas(ax, esp: Spec) -> None:
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("MEDIDAS DE COMPONENTES  (m)", loc="left", fontsize=8, pad=8)
    headers = ["Componente", "Ancho", "Fondo", "Alto", "z piso", "x", "y"]
    rows = [headers]
    for m in esp["muebles"].values():
        if not m.get("en_planta", True):
            continue
        rows.append([
            m["nombre"],
            _fmt_m(m["w"]),
            _fmt_m(m["d"]),
            _fmt_m(m["alto"]),
            _fmt_m(m.get("z0") or 0.0),
            _fmt_m(m["x"]),
            _fmt_m(m["y"]),
        ])
    for p in esp.get("puertas") or []:
        rows.append([
            p["nombre"],
            _fmt_m(p["ancho"]),
            "vano",
            _fmt_m(p.get("alto", 2.10)),
            "0",
            p["muro"],
            _fmt_m(p.get("offset", 0)),
        ])
    col_x = [0.0, 0.38, 0.50, 0.62, 0.74, 0.86, 0.94]
    y = 0.96
    for r, row in enumerate(rows):
        weight = "bold" if r == 0 else "normal"
        color = "#111" if r == 0 else "#222"
        if r == 0:
            ax.plot([0, 1], [y + 0.03, y + 0.03], color="#1a1a1a", lw=0.6)
        for x, cell in zip(col_x, row):
            ax.text(x, y, cell, fontsize=6.1, fontname="Arial", fontweight=weight,
                    color=color, va="top", ha="left")
        y -= 0.055
        if r == 0:
            ax.plot([0, 1], [y + 0.035, y + 0.035], color="#1a1a1a", lw=0.4)
    ax.text(0, max(y, 0.04),
            "Cotas en planta = huella (ancho × fondo). El alto se lee en cada pieza y en esta tabla.\n"
            "Línea de trazo: componente elevado (mesada, alacena).",
            fontsize=5.8, fontname="Arial", color="#444", va="top")


def generar_plano(slug: str) -> Path:
    aplicar_estilo()
    esp = get_espacio(slug)
    out = salidas_espacio(slug)
    W, L, _H = _dim_local(esp)

    fig = plt.figure(figsize=(14.5, 10.4), dpi=160)
    fig.subplots_adjust(left=0.05, right=0.97, top=0.86, bottom=0.07)
    fig.add_artist(FancyBboxPatch((0.015, 0.025), 0.97, 0.95, boxstyle="square,pad=0",
                                  fill=False, edgecolor="#1a1a1a", lw=0.8,
                                  transform=fig.transFigure))
    fig.text(0.04, 0.94, "BERUTI 3336  ·  PISO 23  ·  PALERMO", fontsize=8, color="#666")
    fig.text(0.04, 0.905, f"PLANTA {esp['nombre'].upper()}", fontsize=14, fontweight="bold")
    fig.text(0.97, 0.94, "ESCALA 1:25  ·  VISTA SUPERIOR ACOTADA", fontsize=8,
             color="#666", ha="right")
    fig.text(0.97, 0.905,
             f"N {_fmt_m(esp.get('ancho_norte', esp['ancho']))}  ·  S {_fmt_m(esp.get('ancho_sur', esp['ancho']))}  ·  "
             f"L {esp['largo']:.2f} m   ·   {esp['superficie']:.1f} m²   ·   H {_fmt_m(esp.get('alto', 2.5))}",
             fontsize=8, ha="right")

    ax = fig.add_subplot(111)
    _dibujar_contenido_planta(ax, esp)
    _dibujar_norte_y_adyacencias(ax, esp, W, L)

    dest = out["planos"] / f"{slug}_planta.png"
    fig.savefig(dest, dpi=180, bbox_inches="tight", pad_inches=0.12)
    fig.savefig(out["planos_global"] / f"{slug}_planta.png", dpi=180,
                bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    return dest



def generar_axonometria(slug: str) -> Path:
    aplicar_estilo()
    esp = get_espacio(slug)
    out = salidas_espacio(slug)
    W, L, H = _dim_local(esp)

    fig = plt.figure(figsize=(12, 9), dpi=160)
    fig.subplots_adjust(left=0.05, right=0.97, top=0.88, bottom=0.07)
    fig.text(0.05, 0.94, "BERUTI 3336  ·  RENDER DE ESPACIO", fontsize=8, color="#666")
    fig.text(0.05, 0.90, f"AXONOMÉTRICA  ·  {esp['nombre'].upper()}", fontsize=13, fontweight="bold")
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")

    def face(pts, color, z=2, alpha=0.95):
        ax.add_patch(Polygon([_iso(*p) for p in pts], closed=True,
                             facecolor=color, edgecolor="#2b1d10", lw=0.6,
                             alpha=alpha, zorder=z))

    # piso
    poly = _contorno(esp)
    face([(x, y, 0) for x, y in poly], "#e8e0d2", z=1)
    wn = float(esp.get("ancho_norte") or W)
    # muros recortados (sin techo, sin muro sur para ver adentro)
    face([(0, L, 0), (wn, L, 0), (wn, L, H), (0, L, H)], "#d9d2c5", z=2)
    face([(0, 0, 0), (0, L, 0), (0, L, H), (0, 0, H)], "#cfc6b6", z=2)

    for m in esp["muebles"].values():
        if not m.get("en_planta", True):
            continue
        x, y, w, d, h = m["x"], m["y"], m["w"], m["d"], min(m["alto"], H)
        c = _color_mueble(m)
        face([(x, y + d, 0), (x + w, y + d, 0), (x + w, y + d, h), (x, y + d, h)], c, z=4)
        face([(x + w, y, 0), (x + w, y + d, 0), (x + w, y + d, h), (x + w, y, h)], c, z=5)
        face([(x, y, h), (x + w, y, h), (x + w, y + d, h), (x, y + d, h)], "#f7f3ea", z=6)
        face([(x, y, 0), (x + w, y, 0), (x + w, y, h), (x, y, h)], c, z=7)
        cx, cy = _iso(x + w / 2, y + d / 2, h + 0.05)
        ax.text(cx, cy, _nombre_corto(m["nombre"]), fontsize=5.2, ha="center", va="bottom",
                fontname="Arial", zorder=8)

    dest = out["renders"] / f"{slug}_axonometria.png"
    fig.savefig(dest, dpi=180, bbox_inches="tight", pad_inches=0.14)
    fig.savefig(out["renders_global"] / f"{slug}_axonometria.png", dpi=180,
                bbox_inches="tight", pad_inches=0.14)
    plt.close(fig)
    return dest


def _dim_local(esp: Spec) -> tuple[float, float, float]:
    W, L = esp["ancho"], esp["largo"]
    if esp.get("ancho_total"):
        W = esp["ancho_total"]
    W = max(W, float(esp.get("ancho_sur") or 0), float(esp.get("ancho_norte") or 0))
    return W, L, float(esp.get("alto", 2.50))


def _contorno(esp: Spec) -> list[tuple[float, float]]:
    if esp.get("contorno"):
        return [(float(a), float(b)) for a, b in esp["contorno"]]
    W, L, _H = _dim_local(esp)
    wn = float(esp.get("ancho_norte") or W)
    ws = float(esp.get("ancho_sur") or W)
    yj = float(esp.get("y_escalon") or 0.0)
    if abs(wn - ws) < 0.01 or yj <= 0.01:
        return [(0.0, 0.0), (W, 0.0), (W, L), (0.0, L)]
    return [
        (0.0, 0.0), (ws, 0.0), (ws, yj), (wn, yj), (wn, L), (0.0, L),
    ]


def _x_este(esp: Spec, y: float) -> float:
    W, L, _H = _dim_local(esp)
    wn = float(esp.get("ancho_norte") or W)
    ws = float(esp.get("ancho_sur") or W)
    yj = float(esp.get("y_escalon") or 0.0)
    if yj > 0.01 and y + 0.001 >= yj:
        return wn
    return ws if abs(ws - wn) >= 0.01 else W


def _dibujar_vanos_planta(ax, esp: Spec, W: float, L: float, T: float,
                          muros: set[str] | None = None) -> None:
    muros = muros if muros is not None else _muros_obra(esp)
    for p in esp.get("puertas") or []:
        muro = p["muro"]
        ancho = p["ancho"]
        off = p.get("offset", 0.0)
        if muro not in muros:
            # Abertura hacia un local vecino: no hay jambas de obra.
            if muro == "E":
                xe = _x_este(esp, off)
                ax.plot([xe, xe], [off, off + ancho], color="#666", lw=0.8,
                        ls=(0, (4, 2)), zorder=5)
                ax.annotate("", xy=(xe + 0.28, off + ancho / 2),
                            xytext=(xe, off + ancho / 2),
                            arrowprops=dict(arrowstyle="-|>", color="#666", lw=0.7))
                ax.text(xe + 0.32, off + ancho / 2, p["nombre"], ha="left", va="center",
                        fontsize=5.5, color="#333", rotation=90)
            elif muro == "O":
                ax.plot([0, 0], [off, off + ancho], color="#666", lw=0.8,
                        ls=(0, (4, 2)), zorder=5)
                ax.text(-0.12, off + ancho / 2, p["nombre"], ha="right", va="center",
                        fontsize=5.5, color="#333", rotation=90)
            elif muro == "S":
                ax.plot([off, off + ancho], [0, 0], color="#666", lw=0.8,
                        ls=(0, (4, 2)), zorder=5)
                ax.text(off + ancho / 2, -0.18, p["nombre"], ha="center", va="top",
                        fontsize=5.5, color="#333")
            elif muro == "N":
                ax.plot([off, off + ancho], [L, L], color="#666", lw=0.8,
                        ls=(0, (4, 2)), zorder=5)
                ax.text(off + ancho / 2, L + 0.08, p["nombre"], ha="center", va="bottom",
                        fontsize=5.5, color="#333")
            continue
        if muro == "S":
            ax.add_patch(Rectangle((off, -T), ancho, T, facecolor="#f4f1ea",
                                   edgecolor="none", zorder=3))
            ax.plot([off, off], [-T, 0], color="#1a1a1a", lw=1.0, zorder=5)
            ax.plot([off + ancho, off + ancho], [-T, 0], color="#1a1a1a", lw=1.0, zorder=5)
            ax.plot([off, off + ancho], [0, 0], color="#1a1a1a", lw=0.5, ls=(0, (2, 1)), zorder=5)
            ax.text(off + ancho / 2, -T - 0.18, p["nombre"], ha="center", va="top",
                    fontsize=5.5, color="#333")
        elif muro == "N":
            ax.add_patch(Rectangle((off, L), ancho, T, facecolor="#f4f1ea",
                                   edgecolor="none", zorder=3))
            ax.plot([off, off], [L, L + T], color="#1a1a1a", lw=1.0, zorder=5)
            ax.plot([off + ancho, off + ancho], [L, L + T], color="#1a1a1a", lw=1.0, zorder=5)
            ax.text(off + ancho / 2, L + T + 0.08, p["nombre"], ha="center", va="bottom",
                    fontsize=5.5, color="#333")
        elif muro == "E":
            ax.add_patch(Rectangle((W, off), T, ancho, facecolor="#f4f1ea",
                                   edgecolor="none", zorder=3))
            ax.plot([W, W + T], [off, off], color="#1a1a1a", lw=1.0, zorder=5)
            ax.plot([W, W + T], [off + ancho, off + ancho], color="#1a1a1a", lw=1.0, zorder=5)
            ax.plot([W, W], [off, off + ancho], color="#1a1a1a", lw=0.5, ls=(0, (2, 1)), zorder=5)
            ax.text(W + T + 0.08, off + ancho / 2, p["nombre"], ha="left", va="center",
                    fontsize=5.5, color="#333", rotation=90)
        elif muro == "O":
            ax.add_patch(Rectangle((-T, off), T, ancho, facecolor="#f4f1ea",
                                   edgecolor="none", zorder=3))
            ax.plot([-T, 0], [off, off], color="#1a1a1a", lw=1.0, zorder=5)
            ax.plot([-T, 0], [off + ancho, off + ancho], color="#1a1a1a", lw=1.0, zorder=5)
            ax.text(-T - 0.08, off + ancho / 2, p["nombre"], ha="right", va="center",
                    fontsize=5.5, color="#333", rotation=90)


def _en_muro(m: Spec, muro: str, W: float, L: float, tol: float = 0.28) -> bool:
    if not m.get("en_planta", True):
        return False
    if m["w"] > 0.85 * W and m["d"] > 0.85 * L:
        return False
    if muro == "N":
        return (m["y"] + m["d"]) >= L - tol
    if muro == "S":
        return m["y"] <= tol
    if muro == "E":
        return (m["x"] + m["w"]) >= W - tol
    if muro == "O":
        return m["x"] <= tol
    return False


def _es_overhead(m: Spec) -> bool:
    return float(m.get("z0") or 0.0) >= 0.4


def _modulo_grande(m: Spec) -> bool:
    """Pieza que se acota en una pared saturada: corrida larga, mesada o piso a techo."""
    if m.get("cota") is False:
        return False
    if m.get("cota") is True:
        return True
    if _es_overhead(m) and m.get("tipo") != "mesada":
        return False
    if float(m.get("alto") or 0.0) >= 2.0:
        return True
    return max(m["w"], m["d"]) >= 1.0 or (m["w"] * m["d"]) >= 0.70


def _cubierto_por_mesada(m: Spec, visibles: list[Spec]) -> bool:
    if m.get("tipo") == "mesada":
        return False
    for o in visibles:
        if o.get("tipo") != "mesada":
            continue
        if abs(o["x"] - m["x"]) < 0.06 and abs(o["w"] - m["w"]) < 0.10:
            return True
    return False


def _pared_saturada(esp: Spec, m: Spec, W: float, L: float) -> bool:
    visibles = [x for x in esp["muebles"].values() if x.get("en_planta", True)]
    vanos = esp.get("puertas") or []
    for muro in "NSEO":
        if not _en_muro(m, muro, W, L):
            continue
        n = sum(1 for x in visibles if _en_muro(x, muro, W, L))
        n += sum(1 for p in vanos if p.get("muro") == muro)
        if n >= 3:
            return True
    return False


def _span_alzado(m: Spec, muro: str, W: float, L: float) -> tuple[float, float]:
    if muro == "N":
        return m["x"], m["x"] + m["w"]
    if muro == "S":
        return W - (m["x"] + m["w"]), W - m["x"]
    if muro == "E":
        return L - (m["y"] + m["d"]), L - m["y"]
    return m["y"], m["y"] + m["d"]


def _largo_muro(esp: Spec, muro: str, W: float, L: float) -> float:
    if muro == "N":
        return float(esp.get("ancho_norte") or W)
    if muro == "S":
        return float(esp.get("ancho_sur") or W)
    return L


def _vanos_en_alzado(p: Spec, muro: str, W: float, L: float) -> tuple[float, float] | None:
    if p["muro"] != muro:
        return None
    off, ancho = p.get("offset", 0.0), p["ancho"]
    if muro == "N":
        return off, off + ancho
    if muro == "S":
        return W - (off + ancho), W - off
    if muro == "E":
        return L - (off + ancho), L - off
    return off, off + ancho


def _alzado_principal(esp: Spec, W: float, L: float) -> str:
    if esp.get("alzado_principal"):
        return esp["alzado_principal"]
    counts = {k: 0.0 for k in "NSEO"}
    for m in esp["muebles"].values():
        for muro in counts:
            if _en_muro(m, muro, W, L):
                counts[muro] += m["w"] * m["d"]
    return max(counts, key=counts.get)


def _dibujar_alzado(ax, esp: Spec, muro: str) -> None:
    W_bbox, L, H = _dim_local(esp)
    largo = _largo_muro(esp, muro, W_bbox, L)
    W = largo if muro in ("N", "S") else W_bbox
    nombres = {"N": "NORTE", "S": "SUR", "E": "ESTE", "O": "OESTE"}
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-0.55, largo + 0.85)
    ax.set_ylim(-0.55, H + 0.55)

    obra = muro in _muros_obra(esp)
    if obra:
        ax.add_patch(Rectangle((0, 0), largo, H, facecolor="#f4f1ea",
                               edgecolor="#1a1a1a", lw=1.1, zorder=1))
        ax.plot([0, largo], [0, 0], color="#888", lw=2.2, zorder=2)
    else:
        ax.add_patch(Rectangle((0, 0), largo, H, facecolor="#f7f4ee",
                               edgecolor="none", zorder=1))
        ax.plot([0, largo], [0, 0], color="#888", lw=1.0, ls=(0, (4, 2)), zorder=2)
        ax.plot([0, largo], [H, H], color="#bbb", lw=0.6, ls=(0, (3, 2)), zorder=2)
        ax.text(largo / 2, H + 0.12, "sin muro de obra  ·  cierre de carpintería / vacío",
                ha="center", fontsize=6, color="#666", fontname="Arial")

    for p in esp.get("puertas") or []:
        span = _vanos_en_alzado(p, muro, W, L)
        if not span:
            continue
        u0, u1 = span
        alto = p.get("alto", 2.10)
        if muro not in _muros_obra(esp):
            ax.add_patch(Rectangle((u0, 0), u1 - u0, alto, facecolor="#ffffff",
                                   edgecolor="#888", lw=0.7, linestyle=(0, (4, 2)), zorder=3))
            ax.text((u0 + u1) / 2, alto / 2, "abertura\n(sin muro)", ha="center", va="center",
                    fontsize=6, fontname="Arial", color="#666")
        else:
            ax.add_patch(Rectangle((u0, 0), u1 - u0, alto, facecolor="#ffffff",
                                   edgecolor="#1a1a1a", lw=1.0, zorder=3))
            ax.plot([u0, u0], [0, alto], color="#1a1a1a", lw=1.2, zorder=4)
            ax.plot([u1, u1], [0, alto], color="#1a1a1a", lw=1.2, zorder=4)
        ax.text((u0 + u1) / 2, alto + 0.06, p["nombre"], ha="center", va="bottom",
                fontsize=6, fontname="Arial", color="#333")
        ax.text((u0 + u1) / 2, -0.22, f"{p['ancho']:.2f}", ha="center", va="top",
                fontsize=6.5, fontname="Arial")

    muebles = [m for m in esp["muebles"].values()
               if m.get("en_planta", True) and _en_muro(m, muro, W_bbox, L)]
    muebles.sort(key=lambda m: (m.get("z0", 0.0), -m["alto"]))
    saturada = len(muebles) + (1 if any(p.get("muro") == muro for p in (esp.get("puertas") or [])) else 0) >= 3
    for m in muebles:
        u0, u1 = _span_alzado(m, muro, W, L)
        z0 = float(m.get("z0") or 0.0)
        h = min(m["alto"], H - z0)
        ax.add_patch(Rectangle((u0, z0), max(u1 - u0, 0.02), h,
                               facecolor=_color_mueble(m), edgecolor="#2b1d10",
                               lw=0.7, zorder=5))
        if (u1 - u0) > 0.28 and h > 0.18:
            ax.text((u0 + u1) / 2, z0 + h / 2, _nombre_corto(m["nombre"]),
                    ha="center", va="center",
                    fontsize=5.4, fontname="Arial", zorder=6, path_effects=FX)
        grande = _modulo_grande(m) and not _cubierto_por_mesada(m, muebles)
        if (not saturada or grande) and not (_es_overhead(m) and m.get("tipo") != "mesada"):
            ax.text((u0 + u1) / 2, -0.20, _fmt_m(abs(u1 - u0)), ha="center", va="top",
                    fontsize=6.2, fontname="Arial")

    ax.plot([0, 0], [0, H], color="#222", lw=0.55)
    ax.plot([-0.06, 0.06], [0, 0], color="#222", lw=0.55)
    ax.plot([-0.06, 0.06], [H, H], color="#222", lw=0.55)
    ax.text(-0.12, H / 2, f"{H:.2f}", ha="right", va="center", fontsize=7,
            fontname="Arial", rotation=90)
    ax.plot([0, largo], [-0.38, -0.38], color="#222", lw=0.55)
    ax.text(largo / 2, -0.44, f"{largo:.2f}", ha="center", va="top", fontsize=7)
    ax.set_title(f"ALZADO {nombres[muro]}  ·  vista de frente", loc="left",
                 fontsize=8, pad=6, color="#333")


def generar_alzado(slug: str, muro: str | None = None) -> Path:
    aplicar_estilo()
    esp = get_espacio(slug)
    out = salidas_espacio(slug)
    W, L, _H = _dim_local(esp)
    muro = muro or _alzado_principal(esp, W, L)
    H = _dim_local(esp)[2]

    fig = plt.figure(figsize=(14, 8.5), dpi=160)
    fig.subplots_adjust(left=0.06, right=0.97, top=0.86, bottom=0.08)
    fig.add_artist(FancyBboxPatch((0.02, 0.03), 0.96, 0.94, boxstyle="square,pad=0",
                                  fill=False, edgecolor="#1a1a1a", lw=0.8,
                                  transform=fig.transFigure))
    fig.text(0.05, 0.94, "BERUTI 3336  ·  PISO 23  ·  PALERMO", fontsize=8, color="#666")
    titulo = f"ALZADO {esp['nombre'].upper()}  ·  LADO {muro}"
    if muro not in _muros_obra(esp):
        titulo += "  (sin muro de obra)"
    fig.text(0.05, 0.905, titulo, fontsize=14, fontweight="bold")
    fig.text(0.97, 0.94, "ESCALA 1:25  ·  VISTA DE FRENTE", fontsize=8,
             color="#666", ha="right")
    fig.text(0.97, 0.905, f"H = {H:.2f} m", fontsize=9, ha="right")

    ax = fig.add_subplot(111)
    _dibujar_alzado(ax, esp, muro)

    dest = out["planos"] / f"{slug}_alzado_{muro}.png"
    fig.savefig(dest, dpi=180, bbox_inches="tight", pad_inches=0.12)
    fig.savefig(out["planos_global"] / f"{slug}_alzado_{muro}.png", dpi=180,
                bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    return dest


def generar_vistas(slug: str) -> list[Path]:
    """Planta (vista superior) + alzados N, S, E y O en lámina combinada y por separado."""
    aplicar_estilo()
    esp = get_espacio(slug)
    out = salidas_espacio(slug)
    W, L, _H = _dim_local(esp)
    paths: list[Path] = [generar_plano(slug)]

    muros = ["N", "S", "E", "O"]
    for muro in muros:
        paths.append(generar_alzado(slug, muro))

    fig = plt.figure(figsize=(18.5, 12.5), dpi=160)
    fig.subplots_adjust(left=0.04, right=0.98, top=0.88, bottom=0.05,
                        wspace=0.18, hspace=0.28)
    fig.add_artist(FancyBboxPatch((0.015, 0.02), 0.97, 0.96, boxstyle="square,pad=0",
                                  fill=False, edgecolor="#1a1a1a", lw=0.8,
                                  transform=fig.transFigure))
    fig.text(0.04, 0.955, "BERUTI 3336  ·  PISO 23  ·  PALERMO", fontsize=8, color="#666")
    fig.text(0.04, 0.92, f"VISTAS {esp['nombre'].upper()}  ·  PLANTA + ALZADOS N · S · E · O",
             fontsize=13, fontweight="bold")
    fig.text(0.97, 0.955, "SUPERIOR + FRENTES  ·  1:25", fontsize=8, color="#666", ha="right")

    gs = fig.add_gridspec(2, 4, height_ratios=[1.25, 1.0])
    ax_p = fig.add_subplot(gs[0, :])
    _dibujar_contenido_planta(ax_p, esp)
    _dibujar_norte_y_adyacencias(ax_p, esp, W, L)
    ax_p.set_title("PLANTA  ·  vista superior", loc="left", fontsize=8, pad=6)

    nombres = {"N": "NORTE", "S": "SUR", "E": "ESTE", "O": "OESTE"}
    for i, muro in enumerate(muros):
        ax = fig.add_subplot(gs[1, i])
        _dibujar_alzado(ax, esp, muro)
        nota = ""
        if muro not in _muros_obra(esp):
            nota = "  (sin muro de obra)"
        ax.set_title(f"ALZADO {nombres[muro]}{nota}", loc="left", fontsize=7.5, pad=4)

    dest = out["planos"] / f"{slug}_vistas.png"
    fig.savefig(dest, dpi=180, bbox_inches="tight", pad_inches=0.12)
    fig.savefig(out["planos_global"] / f"{slug}_vistas.png", dpi=180,
                bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    paths.append(dest)
    return paths

