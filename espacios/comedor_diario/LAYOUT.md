# Comedor Diario — LAYOUT

## Identificación
- **Slug:** `comedor_diario`
- **Grupo:** C. Área de servicios y cocina
- **Superficie:** 6.0 m²
- **Alto de local:** 2.50 m

## Medidas
- **Ancho (X, este):** 2.08 m
- **Largo (Y, norte):** 2.89 m
- **Origen de coordenadas:** rincón interior sudoeste. +X este, +Y norte.

## Descripción
Breakfast nook para comidas rápidas. Semintegrado con la cocina mediante barra de madera o cerramiento de vidrio y perfilería negra.

## Criterio de diseño
Mesa compacta para 4 y barra de conexión visual con la cocina.

## Adyacencias
- **S:** Cocina
- **E:** Living
- **N:** Fachada / luz

## Vanos
- **Desde cocina** en muro S, ancho 0.90 m

## Componentes / muebles

| ID | Nombre | Frente × fondo × alto | Posición (x, y) | Frente hacia |
| --- | --- | --- | --- | --- |
| `MESA_DESAYUNADOR` | Mesa desayunador | 1.20 × 0.80 × 0.75 m | (0.44, 1.20) | N |
| `BANCOS` | Sillas / bancos del nook | 0.45 × 0.45 × 0.78 m | (0.30, 1.05) | N |
| `BARRA` | Barra de conexión con cocina | 1.60 × 0.40 × 1.10 m | (0.24, 0.00) | S |

- [Mesa desayunador](FURNITURE_MESA_DESAYUNADOR.md) — `python3 FURNITURE_MESA_DESAYUNADOR.py`
- [Sillas / bancos del nook](FURNITURE_BANCOS.md) — `python3 FURNITURE_BANCOS.py`
- [Barra de conexión con cocina](FURNITURE_BARRA.md) — `python3 FURNITURE_BARRA.py`

## Salidas
- Plantas: `planos/`
- Renders de espacio: `renders/`
- Fichas de mueble: `renders/muebles/`
