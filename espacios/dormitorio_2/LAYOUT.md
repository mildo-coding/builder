# Dormitorio 2 — LAYOUT

## Identificación
- **Slug:** `dormitorio_2`
- **Grupo:** B. Área privada
- **Superficie:** 15.0 m²
- **Alto de local:** 2.50 m

## Medidas
- **Ancho (X, este):** 3.67 m
- **Largo (Y, norte):** 4.09 m
- **Origen de coordenadas:** rincón interior sudoeste. +X este, +Y norte.

## Descripción
Dormitorio secundario amplio. Huéspedes, hijos o uso multipropósito. Cama Queen (o dos individuales) y frente de placard.

## Criterio de diseño
Cama Queen al eje, placard en el muro más largo. Previsión de dos camas individuales.

## Adyacencias
- **S:** Baño de visitas
- **O:** Hall

## Vanos
- **Acceso** en muro O, ancho 0.80 m

## Componentes / muebles

| ID | Nombre | Frente × fondo × alto | Posición (x, y) | Frente hacia |
| --- | --- | --- | --- | --- |
| `CAMA_QUEEN` | Cama Queen | 1.60 × 2.00 × 0.45 m | (1.03, 1.10) | N |
| `MESA_NOCHE_2` | Mesa de noche | 0.45 × 0.35 × 0.50 m | (0.45, 1.10) | N |
| `PLACARD` | Placard de frente continuo | 2.80 × 0.60 × 2.50 m | (0.40, 3.49) | S |

- [Cama Queen](FURNITURE_CAMA_QUEEN.md) — `python3 FURNITURE_CAMA_QUEEN.py`
- [Mesa de noche](FURNITURE_MESA_NOCHE_2.md) — `python3 FURNITURE_MESA_NOCHE_2.py`
- [Placard de frente continuo](FURNITURE_PLACARD.md) — `python3 FURNITURE_PLACARD.py`

## Salidas
- Plantas: `planos/`
- Renders de espacio: `renders/`
- Fichas de mueble: `renders/muebles/`
