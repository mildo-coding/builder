#!/usr/bin/env python3
"""Genera plantas y renders de todos los espacios."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _comun.catalogo import ORDEN_ESPACIOS  # noqa: E402


def main() -> None:
    for slug in ORDEN_ESPACIOS:
        script = HERE / slug / "generar_renders.py"
        print(f"\n=== {slug} ===")
        runpy.run_path(str(script), run_name="__main__")


if __name__ == "__main__":
    main()
