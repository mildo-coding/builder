# Panelado TV / audio

Ficha de carpintería / equipamiento para **Living Comedor**.

## Identificación
- **Archivo:** `FURNITURE_PANELADO_TV`
- **Espacio:** Living Comedor (`living_comedor`)
- **Tipo:** panel

## Medidas
- **Frente:** 3.200 m
- **Profundidad:** 0.040 m
- **Alto:** 2.500 m
- **Huella en planta (w × d):** 3.200 × 0.040 m

## Ubicación
- **Descripción:** Pared sur del living, eje de la zona de estar, frente al sofá.
- **Origen (x, y):** (1.15, 0.00) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Roble de Eslavonia** — listones piso a techo (clave `roble`)
- **LED 2700K** — garganta superior e inferior (clave `blanco`)

## Texturas
Listonado vertical de 40 mm con juntas de sombra. TV empotrada al eje.

## Componentes
- TV 65" empotrada
- pasacables oculto
- LED indirecta

## Generar render

```bash
cd espacios/living_comedor
python3 FURNITURE_PANELADO_TV.py
```

Salida: `renders/muebles/FURNITURE_PANELADO_TV.png`
