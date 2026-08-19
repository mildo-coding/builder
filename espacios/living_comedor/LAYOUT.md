# Living Comedor — LAYOUT

## Identificación
- **Slug:** `living_comedor`
- **Grupo:** A. Área social y exterior
- **Superficie:** 44.0 m²
- **Alto de local:** 2.50 m

## Medidas
- **Ancho (X, este):** 5.50 m
- **Largo (Y, norte):** 8.00 m
- **Origen de coordenadas:** rincón interior sudoeste. +X este, +Y norte.

## Descripción
Corazón del departamento. Espacio amplio y flexible que sectoriza estar/TV y comedor principal para 8-10 personas. Conexión directa con el balcón, luz natural y vistas al Río de la Plata.

## Criterio de diseño
Panelado de madera en la pared de TV, mueble bar a medida con LED indirecta, comedor cerca de la salida al balcón.

## Adyacencias
- **N:** Balcón / terraza
- **S:** Hall y acceso
- **E:** Dormitorios / núcleo húmedo
- **O:** Cocina / comedor diario

## Vanos
- **Salida a balcón** en muro N, ancho 1.80 m
- **Acceso desde hall** en muro S, ancho 0.90 m

## Componentes / muebles

| ID | Nombre | Frente × fondo × alto | Posición (x, y) | Frente hacia |
| --- | --- | --- | --- | --- |
| `PANELADO_TV` | Panelado TV / audio | 3.20 × 0.04 × 2.50 m | (1.15, 0.00) | N |
| `SOFA` | Sofá de estar | 2.80 × 1.00 × 0.85 m | (1.35, 2.40) | S |
| `MESA_CENTRO` | Mesa de centro | 1.20 × 0.70 × 0.38 m | (2.15, 1.45) | S |
| `MUEBLE_BAR` | Mueble bar / vajillero | 1.80 × 0.45 × 1.20 m | (0.00, 3.60) | E |
| `MESA_COMEDOR` | Mesa de comedor | 2.40 × 1.10 × 0.75 m | (1.55, 5.70) | N |
| `SILLAS_COMEDOR` | Juego de sillas de comedor | 0.50 × 0.55 × 0.80 m | (1.40, 5.50) | N |

- [Panelado TV / audio](FURNITURE_PANELADO_TV.md) — `python3 FURNITURE_PANELADO_TV.py`
- [Sofá de estar](FURNITURE_SOFA.md) — `python3 FURNITURE_SOFA.py`
- [Mesa de centro](FURNITURE_MESA_CENTRO.md) — `python3 FURNITURE_MESA_CENTRO.py`
- [Mueble bar / vajillero](FURNITURE_MUEBLE_BAR.md) — `python3 FURNITURE_MUEBLE_BAR.py`
- [Mesa de comedor](FURNITURE_MESA_COMEDOR.md) — `python3 FURNITURE_MESA_COMEDOR.py`
- [Juego de sillas de comedor](FURNITURE_SILLAS_COMEDOR.md) — `python3 FURNITURE_SILLAS_COMEDOR.py`

## Salidas
- Plantas: `planos/`
- Renders de espacio: `renders/`
- Fichas de mueble: `renders/muebles/`
