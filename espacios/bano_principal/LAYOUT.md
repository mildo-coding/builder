# Baño Principal (en suite) — LAYOUT

## Identificación
- **Slug:** `bano_principal`
- **Grupo:** D. Núcleo de baños
- **Superficie:** 2.8 m²
- **Alto de local:** 2.50 m

## Medidas
- **Ancho (X, este):** 1.88 m
- **Largo (Y, norte):** 1.49 m
- **Origen de coordenadas:** rincón interior sudoeste. +X este, +Y norte.

## Descripción
Baño completo de la suite. Revestimientos de gran formato, vanitory flotante de madera, mampara de vidrio templado y grifería negra/embutida.

## Criterio de diseño
Ducha al fondo con mampara, vanitory flotante sobre el muro largo, inodoro lineal.

## Adyacencias
- **O:** Dormitorio principal

## Vanos
- **Desde suite** en muro O, ancho 0.70 m

## Componentes / muebles

| ID | Nombre | Frente × fondo × alto | Posición (x, y) | Frente hacia |
| --- | --- | --- | --- | --- |
| `VANITORY` | Vanitory flotante | 1.00 × 0.45 × 0.40 m | (0.70, 0.00) | N |
| `MAMPARA` | Mampara de ducha | 0.90 × 0.08 × 2.00 m | (0.00, 0.80) | E |
| `INODORO` | Inodoro | 0.37 × 0.68 × 0.40 m | (1.40, 0.70) | S |

- [Vanitory flotante](FURNITURE_VANITORY.md) — `python3 FURNITURE_VANITORY.py`
- [Mampara de ducha](FURNITURE_MAMPARA.md) — `python3 FURNITURE_MAMPARA.py`
- [Inodoro](FURNITURE_INODORO.md) — `python3 FURNITURE_INODORO.py`

## Salidas
- Plantas: `planos/`
- Renders de espacio: `renders/`
- Fichas de mueble: `renders/muebles/`
