# Hall de Distribución — LAYOUT

## Identificación
- **Slug:** `hall_distribucion`
- **Grupo:** D. Núcleo de baños
- **Superficie:** 3.2 m²
- **Alto de local:** 2.50 m

## Medidas
- **Ancho (X, este):** 1.38 m
- **Largo (Y, norte):** 2.30 m
- **Origen de coordenadas:** rincón interior sudoeste. +X este, +Y norte.

## Descripción
Transición limpia entre la recepción social y el área privada de dormitorios y baños.

## Criterio de diseño
Paredes limpias, panelado bajo o consola de apoyo, luz indirecta en cielorraso.

## Adyacencias
- **O:** Living
- **E:** Dormitorios
- **N:** Baños

## Vanos
- **Desde living** en muro O, ancho 0.90 m
- **A dormitorio principal** en muro E, ancho 0.80 m

## Componentes / muebles

| ID | Nombre | Frente × fondo × alto | Posición (x, y) | Frente hacia |
| --- | --- | --- | --- | --- |
| `CONSOLA` | Consola de recibo | 1.00 × 0.32 × 0.80 m | (0.19, 1.40) | S |
| `PANELADO_HALL` | Panelado de hall | 2.30 × 0.03 × 1.20 m | (0.00, 0.00) | E |

- [Consola de recibo](FURNITURE_CONSOLA.md) — `python3 FURNITURE_CONSOLA.py`
- [Panelado de hall](FURNITURE_PANELADO_HALL.md) — `python3 FURNITURE_PANELADO_HALL.py`

## Salidas
- Plantas: `planos/`
- Renders de espacio: `renders/`
- Fichas de mueble: `renders/muebles/`
