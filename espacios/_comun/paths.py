"""Rutas de salida de planos y renders."""

from __future__ import annotations

from pathlib import Path

from .estilo import PLANOS_DIR, RENDERS_DIR, ESPACIOS_DIR


def carpeta_espacio(slug: str) -> Path:
    return ESPACIOS_DIR / slug


def salidas_espacio(slug: str) -> dict[str, Path]:
    base = carpeta_espacio(slug)
    dirs = {
        "espacio": base,
        "planos": base / "planos",
        "renders": base / "renders",
        "renders_muebles": base / "renders" / "muebles",
        "planos_global": PLANOS_DIR,
        "renders_global": RENDERS_DIR / slug,
    }
    for p in dirs.values():
        p.mkdir(parents=True, exist_ok=True)
    return dirs
