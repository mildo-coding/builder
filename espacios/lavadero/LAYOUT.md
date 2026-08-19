# Lavadero — LAYOUT

## Identificación
- **Slug:** `lavadero`
- **Grupo:** C. Área de servicios y cocina
- **Superficie:** 5.6 m²
- **Alto de local:** 2.50 m

## Medidas
- **Ancho (X, este):** 2.00 m útiles / 2.62 m totales
- **Largo (Y, norte):** 2.81 m
- **Origen de coordenadas:** rincón interior sudoeste. +X este, +Y norte.

## Descripción
Local técnico extraído del plano original. Placard de secado ajustado a 1.50 × 0.625 m, con puerta piso a techo y cierre de tabique sólido. Incluye lavarropas, secarropas, piletón y guardado de limpieza.

## Criterio de diseño
El placard arranca contra el muro junto a la puerta de servicio y termina con tabique sólido de 10 cm. El tramo norte original se libera como piso útil (pileta y circulación).

## Adyacencias
- **N:** Baño de servicio
- **S:** Puerta de servicio / circulación
- **E:** Cocina

## Vanos
- **Puerta de servicio** en muro S, ancho 0.80 m
- **A cocina** en muro E, ancho 0.80 m

## Componentes / muebles

| ID | Nombre | Frente × fondo × alto | Posición (x, y) | Frente hacia |
| --- | --- | --- | --- | --- |
| `PLACARD_SECADO` | Placard de secado | 1.500 × 0.625 × 2.500 m | (0.00, 0.00) | E |
| `LAVARROPAS` | Lavarropas | 0.60 × 0.60 × 0.85 m | (2.02, 0.90) | O |
| `PILETON` | Piletón de lavar | 0.50 × 0.40 × 0.90 m | (0.00, 2.20) | E |
| `MUEBLE_LIMPIEZA` | Mueble de limpieza | 0.40 × 0.35 × 2.00 m | (2.23, 1.70) | O |

- [Placard de secado](FURNITURE_PLACARD_SECADO.md) — `python3 FURNITURE_PLACARD_SECADO.py`
- [Lavarropas](FURNITURE_LAVARROPAS.md) — `python3 FURNITURE_LAVARROPAS.py`
- [Piletón de lavar](FURNITURE_PILETON.md) — `python3 FURNITURE_PILETON.py`
- [Mueble de limpieza](FURNITURE_MUEBLE_LIMPIEZA.md) — `python3 FURNITURE_MUEBLE_LIMPIEZA.py`

## Salidas
- Plantas: `planos/`
- Renders de espacio: `renders/`
- Fichas de mueble: `renders/muebles/`
