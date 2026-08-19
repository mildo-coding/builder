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


def generar_plano(slug: str) -> Path:
    aplicar_estilo()
    esp = get_espacio(slug)
    out = salidas_espacio(slug)
    W, L = esp["ancho"], esp["largo"]
    if esp.get("ancho_total"):
        W = esp["ancho_total"]
    T = 0.15

    fig = plt.figure(figsize=(14, 10), dpi=160)
    fig.subplots_adjust(left=0.06, right=0.97, top=0.86, bottom=0.08)
    fig.add_artist(FancyBboxPatch((0.02, 0.03), 0.96, 0.94, boxstyle="square,pad=0",
                                  fill=False, edgecolor="#1a1a1a", lw=0.8,
                                  transform=fig.transFigure))
    fig.text(0.05, 0.94, "BERUTI 3336  ·  PISO 23  ·  PALERMO", fontsize=8, color="#666")
    fig.text(0.05, 0.905, f"PLANTA {esp['nombre'].upper()}", fontsize=14, fontweight="bold")
    fig.text(0.97, 0.94, "ESCALA 1:25  ·  PROPUESTA", fontsize=8, color="#666", ha="right")
    fig.text(0.97, 0.905, f"{esp['ancho']:.2f} × {esp['largo']:.2f} m   ·   {esp['superficie']:.1f} m²",
             fontsize=9, ha="right")

    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.1, W + 1.3)
    ax.set_ylim(-1.0, L + 1.1)

    # poche
    ax.add_patch(Rectangle((-T, -T), W + 2 * T, L + 2 * T, facecolor="#1a1a1a",
                           edgecolor="none", zorder=1))
    ax.add_patch(Rectangle((0, 0), W, L, facecolor="#f4f1ea", edgecolor="none", zorder=2))

    for m in esp["muebles"].values():
        ax.add_patch(Rectangle((m["x"], m["y"]), m["w"], m["d"],
                               facecolor=_color_mueble(m), edgecolor="#2b1d10",
                               lw=0.7, zorder=3, alpha=0.92))
        ax.text(m["x"] + m["w"] / 2, m["y"] + m["d"] / 2, m["nombre"],
                ha="center", va="center", fontsize=5.6, fontname="Arial",
                color="#1a1a1a", zorder=4, path_effects=FX)

    # cotas
    ax.plot([0, W], [-0.45, -0.45], color="#222", lw=0.55)
    ax.text(W / 2, -0.52, f"{W:.2f}", ha="center", va="top", fontsize=8)
    ax.plot([-0.45, -0.45], [0, L], color="#222", lw=0.55)
    ax.text(-0.52, L / 2, f"{L:.2f}", ha="right", va="center", fontsize=8, rotation=90)

    ax.annotate("", xy=(W + 0.55, L - 0.05), xytext=(W + 0.55, L - 0.45),
                arrowprops=dict(arrowstyle="-|>", color="#111", lw=1.0))
    ax.text(W + 0.55, L + 0.02, "N", ha="center", fontsize=8, fontweight="bold")

    adj = esp.get("adjacencias") or {}
    if "N" in adj:
        ax.text(W / 2, L + 0.28, f"↑  {adj['N']}", ha="center", fontsize=7, color="#666")
    if "S" in adj:
        ax.text(W / 2, -0.78, adj["S"], ha="center", fontsize=7, color="#666")
    if "E" in adj:
        ax.text(W + 0.22, L / 2, f"{adj['E']} →", ha="left", va="center", fontsize=7, color="#666")
    if "O" in adj:
        ax.text(-0.72, L / 2, f"← {adj['O']}", ha="right", va="center", fontsize=7, color="#666")

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
    W, L, H = esp.get("ancho_total", esp["ancho"]), esp["largo"], esp["alto"]

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
    face([(0, 0, 0), (W, 0, 0), (W, L, 0), (0, L, 0)], "#e8e0d2", z=1)
    # muros recortados (sin techo, sin muro sur para ver adentro)
    face([(0, L, 0), (W, L, 0), (W, L, H), (0, L, H)], "#d9d2c5", z=2)
    face([(0, 0, 0), (0, L, 0), (0, L, H), (0, 0, H)], "#cfc6b6", z=2)

    for m in esp["muebles"].values():
        x, y, w, d, h = m["x"], m["y"], m["w"], m["d"], min(m["alto"], H)
        c = _color_mueble(m)
        face([(x, y + d, 0), (x + w, y + d, 0), (x + w, y + d, h), (x, y + d, h)], c, z=4)
        face([(x + w, y, 0), (x + w, y + d, 0), (x + w, y + d, h), (x + w, y, h)], c, z=5)
        face([(x, y, h), (x + w, y, h), (x + w, y + d, h), (x, y + d, h)], "#f7f3ea", z=6)
        face([(x, y, 0), (x + w, y, 0), (x + w, y, h), (x, y, h)], c, z=7)
        cx, cy = _iso(x + w / 2, y + d / 2, h + 0.05)
        ax.text(cx, cy, m["nombre"], fontsize=5.2, ha="center", va="bottom",
                fontname="Arial", zorder=8)

    dest = out["renders"] / f"{slug}_axonometria.png"
    fig.savefig(dest, dpi=180, bbox_inches="tight", pad_inches=0.14)
    fig.savefig(out["renders_global"] / f"{slug}_axonometria.png", dpi=180,
                bbox_inches="tight", pad_inches=0.14)
    plt.close(fig)
    return dest
