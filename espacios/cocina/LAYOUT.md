# Cocina Principal — LAYOUT

## Identificación
- **Slug:** `cocina`
- **Grupo:** C. Área de servicios y cocina
- **Superficie:** 7.4 m²
- **Alto de local:** 2.50 m

## Medidas
- **Ancho (X, este):** 2.00 m
- **Largo (Y, norte):** 3.69 m
- **Origen de coordenadas:** rincón interior sudoeste. +X este, +Y norte.

## Descripción
Cocina longitudinal eficiente (pasillo útil ~1.23 m). Mesadas de Silestone, bajo y sobre mesada en madera cálida y grafito, equipamiento integrado.

## Criterio de diseño
Línea de trabajo en un solo frente: fregadero, anafe, torre de hornos. Alacenas superiores.

## Adyacencias
- **N:** Comedor diario
- **S:** Lavadero / hall de servicio
- **E:** Living

## Vanos
- **A comedor diario** en muro N, ancho 0.80 m
- **A lavadero** en muro S, ancho 0.80 m

## Componentes / muebles

| ID | Nombre | Frente × fondo × alto | Posición (x, y) | Frente hacia |
| --- | --- | --- | --- | --- |
| `BAJO_MESADA` | Bajo mesada | 3.69 × 0.60 × 0.90 m | (0.00, 0.00) | E |
| `MESADA` | Mesada Silestone | 3.69 × 0.62 × 0.04 m | (0.00, 0.00) | E |
| `ALACENA` | Alacenas superiores | 3.69 × 0.35 × 0.70 m | (0.00, 0.00) | E |
| `TORRE_HORNOS` | Torre de hornos | 0.60 × 0.60 × 2.20 m | (0.00, 3.09) | E |

- [Bajo mesada](FURNITURE_BAJO_MESADA.md) — `python3 FURNITURE_BAJO_MESADA.py`
- [Mesada Silestone](FURNITURE_MESADA.md) — `python3 FURNITURE_MESADA.py`
- [Alacenas superiores](FURNITURE_ALACENA.md) — `python3 FURNITURE_ALACENA.py`
- [Torre de hornos](FURNITURE_TORRE_HORNOS.md) — `python3 FURNITURE_TORRE_HORNOS.py`

## Salidas
- Plantas: `planos/`
- Renders de espacio: `renders/`
- Fichas de mueble: `renders/muebles/`
