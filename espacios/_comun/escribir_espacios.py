#!/usr/bin/env python3
"""Escribe README, LAYOUT, fichas y generadores de cada espacio."""

from __future__ import annotations

import sys
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from _comun.catalogo import ESPACIOS, ORDEN_ESPACIOS, ids_muebles  # noqa: E402

GEN_PLANO = '''#!/usr/bin/env python3
"""Genera la planta del espacio {nombre}."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _comun.render_espacio import generar_plano


def main() -> None:
    dest = generar_plano("{slug}")
    print(f"OK planta: {{dest}}")


if __name__ == "__main__":
    main()
'''

GEN_RENDERS = '''#!/usr/bin/env python3
"""Genera renders de espacio y de cada mueble — {nombre}."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _comun.catalogo import ids_muebles, mueble
from _comun.render_espacio import generar_axonometria, generar_plano
from _comun.render_mueble import generar_lamina


def main() -> None:
    print(generar_plano("{slug}"))
    print(generar_axonometria("{slug}"))
    base = Path(__file__).resolve().parent
    for mid in ids_muebles("{slug}"):
        dest = generar_lamina(mueble("{slug}", mid), base)
        print(dest)


if __name__ == "__main__":
    main()
'''

GEN_TODO = '''#!/usr/bin/env python3
"""Genera planta + renders + fichas de muebles de {nombre}."""
from __future__ import annotations
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    runpy.run_path(str(HERE / "generar_renders.py"), run_name="__main__")


if __name__ == "__main__":
    main()
'''

GEN_MUEBLE = '''#!/usr/bin/env python3
"""Render del mueble {nombre_mueble} — {nombre_espacio}."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _comun.catalogo import mueble
from _comun.render_mueble import generar_lamina


def main() -> None:
    spec = mueble("{slug}", "{mid}")
    dest = generar_lamina(spec, Path(__file__).resolve().parent)
    print(f"OK {{dest}}")


if __name__ == "__main__":
    main()
'''


def _md_layout(slug: str, esp: dict) -> str:
    muebles_rows = []
    for mid, m in esp["muebles"].items():
        muebles_rows.append(
            f"| `{mid}` | {m['nombre']} | {m['frente']:.3f} × {m['profundidad']:.3f} × {m['alto']:.3f} m "
            f"| ({m['x']:.2f}, {m['y']:.2f}) | {m['frente_hacia']} |"
        )
    adj = esp.get("adjacencias") or {}
    adj_txt = "\n".join(f"- **{k}:** {v}" for k, v in adj.items()) or "- —"
    puertas = esp.get("puertas") or []
    ptxt = "\n".join(
        f"- **{p['nombre']}** en muro {p['muro']}, ancho {p['ancho']:.2f} m"
        for p in puertas
    ) or "- —"
    ancho_txt = f"{esp['ancho']:.2f}"
    if esp.get("ancho_total"):
        ancho_txt += f" m útiles / {esp['ancho_total']:.2f} m totales"
    else:
        ancho_txt += " m"
    lista = "\n".join(
        f"- [{m['nombre']}](FURNITURE_{mid}.md) — `python3 FURNITURE_{mid}.py`"
        for mid, m in esp["muebles"].items()
    )
    return f"""# {esp['nombre']} — LAYOUT

## Identificación
- **Slug:** `{slug}`
- **Grupo:** {esp['grupo']}
- **Superficie:** {esp['superficie']:.1f} m²
- **Alto de local:** {esp['alto']:.2f} m

## Medidas
- **Ancho (X, este):** {ancho_txt}
- **Largo (Y, norte):** {esp['largo']:.2f} m
- **Origen de coordenadas:** rincón interior sudoeste. +X este, +Y norte.

## Descripción
{esp['descripcion']}

## Criterio de diseño
{esp['criterio']}

## Adyacencias
{adj_txt}

## Vanos
{ptxt}

## Componentes / muebles

| ID | Nombre | Frente × fondo × alto | Posición (x, y) | Frente hacia |
| --- | --- | --- | --- | --- |
{chr(10).join(muebles_rows)}

{lista}

## Salidas
- Plantas: `planos/`
- Renders de espacio: `renders/`
- Fichas de mueble: `renders/muebles/`
"""


def _md_readme(slug: str, esp: dict) -> str:
    muebles = "\n".join(
        f"- `FURNITURE_{mid}.md` + `FURNITURE_{mid}.py` — {m['nombre']}"
        for mid, m in esp["muebles"].items()
    )
    cmds_m = "\n".join(
        f"python3 FURNITURE_{mid}.py"
        for mid in esp["muebles"]
    )
    return f"""# {esp['nombre']}

Carpeta de trabajo de Arqui para el espacio **{esp['nombre']}** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta del espacio
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
{muebles}

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/{slug}`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
{cmds_m}
```

Los PNG se guardan en:
- `espacios/{slug}/planos/`
- `espacios/{slug}/renders/`
- `planos/{slug}_planta.png`
- `renders/{slug}/`

## Medidas de referencia
- Local: {esp['ancho']:.2f} × {esp['largo']:.2f} m ({esp['superficie']:.1f} m²)
- Alto: {esp['alto']:.2f} m
"""


def _md_mueble(slug: str, esp: dict, mid: str, m: dict) -> str:
    mats = "\n".join(
        f"- **{x['nombre']}** — {x['uso']} (clave `{x['clave']}`)"
        for x in m["materiales"]
    )
    comps = "\n".join(f"- {c}" for c in m["componentes"])
    notas = f"\n## Notas\n{m['notas']}\n" if m.get("notas") else ""
    return f"""# {m['nombre']}

Ficha de carpintería / equipamiento para **{esp['nombre']}**.

## Identificación
- **Archivo:** `FURNITURE_{mid}`
- **Espacio:** {esp['nombre']} (`{slug}`)
- **Tipo:** {m['tipo']}

## Medidas
- **Frente:** {m['frente']:.3f} m
- **Profundidad:** {m['profundidad']:.3f} m
- **Alto:** {m['alto']:.3f} m
- **Huella en planta (w × d):** {m['w']:.3f} × {m['d']:.3f} m

## Ubicación
- **Descripción:** {m['ubicacion']}
- **Origen (x, y):** ({m['x']:.2f}, {m['y']:.2f}) m desde el rincón SO del local
- **Frente hacia:** {m['frente_hacia']}

## Materiales
{mats}

## Texturas
{m['texturas']}

## Componentes
{comps}
{notas}
## Generar render

```bash
cd espacios/{slug}
python3 FURNITURE_{mid}.py
```

Salida: `renders/muebles/FURNITURE_{mid}.png`
"""


def escribir_espacio(slug: str) -> Path:
    esp = ESPACIOS[slug]
    dest = ROOT / slug
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "planos").mkdir(exist_ok=True)
    (dest / "renders" / "muebles").mkdir(parents=True, exist_ok=True)

    (dest / "README.md").write_text(_md_readme(slug, esp), encoding="utf-8")
    (dest / "LAYOUT.md").write_text(_md_layout(slug, esp), encoding="utf-8")
    (dest / "generar_plano.py").write_text(GEN_PLANO.format(nombre=esp["nombre"], slug=slug), encoding="utf-8")
    (dest / "generar_renders.py").write_text(GEN_RENDERS.format(nombre=esp["nombre"], slug=slug), encoding="utf-8")
    (dest / "generar_todo.py").write_text(GEN_TODO.format(nombre=esp["nombre"]), encoding="utf-8")

    for mid, m in esp["muebles"].items():
        (dest / f"FURNITURE_{mid}.md").write_text(_md_mueble(slug, esp, mid, m), encoding="utf-8")
        (dest / f"FURNITURE_{mid}.py").write_text(
            GEN_MUEBLE.format(
                nombre_mueble=m["nombre"],
                nombre_espacio=esp["nombre"],
                slug=slug,
                mid=mid,
            ),
            encoding="utf-8",
        )
    return dest


def main() -> None:
    for slug in ORDEN_ESPACIOS:
        p = escribir_espacio(slug)
        n = len(ids_muebles(slug))
        print(f"OK {p.name}  ({n} muebles)")


if __name__ == "__main__":
    main()
