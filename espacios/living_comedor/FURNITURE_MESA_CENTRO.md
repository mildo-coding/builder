# Mesa de centro

Ficha de carpintería / equipamiento para **Living Comedor**.

## Identificación
- **Archivo:** `FURNITURE_MESA_CENTRO`
- **Espacio:** Living Comedor (`living_comedor`)
- **Tipo:** mesa

## Medidas
- **Frente:** 1.200 m
- **Profundidad:** 0.700 m
- **Alto:** 0.380 m
- **Huella en planta (w × d):** 1.200 × 0.700 m

## Ubicación
- **Descripción:** Entre el sofá y el panelado, eje de la zona de estar.
- **Origen (x, y):** (2.15, 1.45) m desde el rincón SO del local
- **Frente hacia:** S

## Materiales
- **Roble** — estructura y fuste (clave `roble`)
- **Silestone** — tapa (clave `silestone`)

## Texturas
Tapa de piedra de 20 mm sobre base de madera maciza.

## Componentes
- tapa 1.20 × 0.70
- base en U

## Generar render

```bash
cd espacios/living_comedor
python3 FURNITURE_MESA_CENTRO.py
```

Salida: `renders/muebles/FURNITURE_MESA_CENTRO.png`
