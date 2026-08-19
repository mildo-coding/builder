# Baño de Visitas — LAYOUT

## Identificación
- **Slug:** `bano_visitas`
- **Grupo:** D. Núcleo de baños
- **Superficie:** 2.6 m²
- **Alto de local:** 2.50 m

## Medidas
- **Ancho (X, este):** 1.80 m
- **Largo (Y, norte):** 1.45 m
- **Origen de coordenadas:** rincón interior sudoeste. +X este, +Y norte.

## Descripción
Baño de apoyo del dormitorio 2 y visitas. Vanitory con madera, espejo retroiluminado y duchero moderno.

## Criterio de diseño
Misma familia material que el baño principal, escala ligeramente menor.

## Adyacencias
- **N:** Dormitorio 2
- **O:** Hall

## Vanos
- **Acceso** en muro O, ancho 0.70 m

## Componentes / muebles

| ID | Nombre | Frente × fondo × alto | Posición (x, y) | Frente hacia |
| --- | --- | --- | --- | --- |
| `VANITORY` | Vanitory con madera | 0.90 × 0.45 × 0.40 m | (0.70, 0.00) | N |
| `ESPEJO_RETROILUMINADO` | Espejo retroiluminado | 0.90 × 0.04 × 0.90 m | (0.70, 0.00) | N |
| `DUCHERO` | Duchero moderno | 0.80 × 0.80 × 2.10 m | (0.00, 0.65) | E |

- [Vanitory con madera](FURNITURE_VANITORY.md) — `python3 FURNITURE_VANITORY.py`
- [Espejo retroiluminado](FURNITURE_ESPEJO_RETROILUMINADO.md) — `python3 FURNITURE_ESPEJO_RETROILUMINADO.py`
- [Duchero moderno](FURNITURE_DUCHERO.md) — `python3 FURNITURE_DUCHERO.py`

## Salidas
- Plantas: `planos/`
- Renders de espacio: `renders/`
- Fichas de mueble: `renders/muebles/`
