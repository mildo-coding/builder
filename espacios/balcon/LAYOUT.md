# Balcón / Terraza — LAYOUT

## Identificación
- **Slug:** `balcon`
- **Grupo:** A. Área social y exterior
- **Superficie:** 11.0 m²
- **Alto de local:** 2.50 m

## Medidas
- **Ancho (X, este):** 5.50 m
- **Largo (Y, norte):** 2.01 m
- **Origen de coordenadas:** rincón interior sudoeste. +X este, +Y norte.

## Descripción
Expansión del living hacia el norte. Lounge exterior, deck y vegetación para disfrutar la vista panorámica del piso 23.

## Criterio de diseño
Deck simil madera, lounge bajo, mesa baja y vegetación perimetral.

## Adyacencias
- **S:** Living comedor
- **N:** Vista al Río de la Plata

## Vanos
- **Desde living** en muro S, ancho 1.80 m

## Componentes / muebles

| ID | Nombre | Frente × fondo × alto | Posición (x, y) | Frente hacia |
| --- | --- | --- | --- | --- |
| `DECK` | Deck / solado exterior | 5.50 × 2.01 × 0.02 m | (0.00, 0.00) | N |
| `LOUNGE_EXTERIOR` | Lounge exterior | 1.80 × 0.80 × 0.70 m | (0.35, 0.90) | N |
| `MESA_BAJA` | Mesa baja exterior | 1.00 × 0.60 × 0.35 m | (2.40, 1.05) | N |
| `MACETEROS` | Maceteros y vegetación | 0.40 × 1.80 × 0.50 m | (4.90, 0.10) | O |

- [Deck / solado exterior](FURNITURE_DECK.md) — `python3 FURNITURE_DECK.py`
- [Lounge exterior](FURNITURE_LOUNGE_EXTERIOR.md) — `python3 FURNITURE_LOUNGE_EXTERIOR.py`
- [Mesa baja exterior](FURNITURE_MESA_BAJA.md) — `python3 FURNITURE_MESA_BAJA.py`
- [Maceteros y vegetación](FURNITURE_MACETEROS.md) — `python3 FURNITURE_MACETEROS.py`

## Salidas
- Plantas: `planos/`
- Renders de espacio: `renders/`
- Fichas de mueble: `renders/muebles/`
