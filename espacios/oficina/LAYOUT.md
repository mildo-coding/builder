# Oficina / Estudio — LAYOUT

## Identificación
- **Slug:** `oficina`
- **Grupo:** B. Área privada
- **Superficie:** 5.3 m²
- **Alto de local:** 2.50 m

## Medidas
- **Ancho (X, este):** 3.10 m
- **Largo (Y, norte):** 1.70 m
- **Origen de coordenadas:** rincón interior sudoeste. +X este, +Y norte.

## Descripción
Home office y lectura. Ventanal con luz natural. Biblioteca a medida, escritorio corrido y aislamiento acústico.

## Criterio de diseño
Escritorio bajo la ventana, biblioteca en el muro largo opuesto o continuo.

## Adyacencias
- **N:** Dormitorio principal
- **S:** Fachada / ventanal

## Vanos
- **Acceso** en muro O, ancho 0.70 m

## Componentes / muebles

| ID | Nombre | Frente × fondo × alto | Posición (x, y) | Frente hacia |
| --- | --- | --- | --- | --- |
| `ESCRITORIO` | Escritorio corrido | 2.40 × 0.60 × 0.75 m | (0.35, 0.05) | S |
| `BIBLIOTECA` | Biblioteca a medida | 3.10 × 0.32 × 2.50 m | (0.00, 1.38) | S |
| `SILLA_ESCRITORIO` | Silla de trabajo | 0.65 × 0.65 × 1.10 m | (1.20, 0.70) | S |

- [Escritorio corrido](FURNITURE_ESCRITORIO.md) — `python3 FURNITURE_ESCRITORIO.py`
- [Biblioteca a medida](FURNITURE_BIBLIOTECA.md) — `python3 FURNITURE_BIBLIOTECA.py`
- [Silla de trabajo](FURNITURE_SILLA_ESCRITORIO.md) — `python3 FURNITURE_SILLA_ESCRITORIO.py`

## Salidas
- Plantas: `planos/`
- Renders de espacio: `renders/`
- Fichas de mueble: `renders/muebles/`
