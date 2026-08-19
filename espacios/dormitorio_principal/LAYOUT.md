# Dormitorio Principal — LAYOUT

## Identificación
- **Slug:** `dormitorio_principal`
- **Grupo:** B. Área privada
- **Superficie:** 16.3 m²
- **Alto de local:** 2.50 m

## Medidas
- **Ancho (X, este):** 3.23 m
- **Largo (Y, norte):** 5.05 m
- **Origen de coordenadas:** rincón interior sudoeste. +X este, +Y norte.

## Descripción
Suite con cama King, respaldo de madera integrado, mesas de noche flotantes y vestidor/placard. Conecta en suite con el baño principal.

## Criterio de diseño
Cama al eje, respaldo-panel de madera con LED, vestidor en el tramo de circulación.

## Adyacencias
- **E:** Baño en suite
- **O:** Hall / placard
- **S:** Oficina

## Vanos
- **Acceso** en muro O, ancho 0.80 m
- **Baño en suite** en muro E, ancho 0.70 m

## Componentes / muebles

| ID | Nombre | Frente × fondo × alto | Posición (x, y) | Frente hacia |
| --- | --- | --- | --- | --- |
| `CAMA_KING` | Cama King Size | 2.00 × 2.00 × 0.45 m | (0.62, 1.40) | N |
| `RESPALDO_MADERA` | Respaldo panelado | 2.40 × 0.08 × 1.20 m | (0.42, 1.32) | N |
| `MESAS_NOCHE` | Mesas de noche flotantes | 0.50 × 0.35 × 0.12 m | (0.42, 1.40) | N |
| `PLACARD_VESTIDOR` | Vestidor / placard | 2.40 × 0.60 × 2.50 m | (0.00, 3.80) | S |

- [Cama King Size](FURNITURE_CAMA_KING.md) — `python3 FURNITURE_CAMA_KING.py`
- [Respaldo panelado](FURNITURE_RESPALDO_MADERA.md) — `python3 FURNITURE_RESPALDO_MADERA.py`
- [Mesas de noche flotantes](FURNITURE_MESAS_NOCHE.md) — `python3 FURNITURE_MESAS_NOCHE.py`
- [Vestidor / placard](FURNITURE_PLACARD_VESTIDOR.md) — `python3 FURNITURE_PLACARD_VESTIDOR.py`

## Salidas
- Plantas: `planos/`
- Renders de espacio: `renders/`
- Fichas de mueble: `renders/muebles/`
