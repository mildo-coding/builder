"""Paleta, tipografías y convenciones gráficas del proyecto Beruti 3336."""

from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/mplconfig")

ROOT = Path(__file__).resolve().parents[2]
ESPACIOS_DIR = ROOT / "espacios"
PLANOS_DIR = ROOT / "planos"
RENDERS_DIR = ROOT / "renders"

# Materiales de obra
MADERA_ROBLE = "#c4a36a"
MADERA_PETIRIBI = "#b8894a"
MADERA_OSCURA = "#5c4030"
GRAFITO = "#3a3a3c"
BLANCO_CALIDO = "#f4f1ea"
SILSTONE = "#ece8e1"
NEGRO = "#1a1a1a"
LINO = "#d9d2c5"
PORCELANATO = "#e8e4dc"
METAL_NEGRO = "#2b2b2b"
VIDRIO = "#c5d5e0"
AGUA = "#8fb8c9"
TERRAZZO = "#d4cfc4"

PALETA = {
    "roble": MADERA_ROBLE,
    "petiribi": MADERA_PETIRIBI,
    "madera_oscura": MADERA_OSCURA,
    "grafito": GRAFITO,
    "blanco": BLANCO_CALIDO,
    "silestone": SILSTONE,
    "negro": NEGRO,
    "lino": LINO,
    "porcelanato": PORCELANATO,
    "metal": METAL_NEGRO,
    "vidrio": VIDRIO,
    "agua": AGUA,
}

FONT = "Arial"

MPL_RC = {
    "font.family": "Arial",
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
    "axes.edgecolor": "#1a1a1a",
    "text.color": "#1a1a1a",
}


def aplicar_estilo() -> None:
    import matplotlib.pyplot as plt

    plt.rcParams.update(MPL_RC)
