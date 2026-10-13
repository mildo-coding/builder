# Escobero

Ficha de carpintería / equipamiento para **Lavadero**.

## Identificación
- **Archivo:** `FURNITURE_ESCOBERO`
- **Espacio:** Lavadero (`lavadero`)
- **Tipo:** placard

## Medidas
- **Frente:** 0.300 m
- **Profundidad:** 0.625 m
- **Alto:** 2.800 m
- **Huella en planta (w × d):** 0.625 × 0.300 m
- **z piso:** 0.000 m

## Ubicación
- **Descripción:** Muro oeste, inmediato al norte del placard de secado. Piso a techo.
- **Origen (x, y):** (0.00, 1.50) m desde el rincón SO del local
- **Frente hacia:** E

## Materiales
- **Roble** — frente (clave `roble`)
- **Grafito** — interior (clave `grafito`)

## Texturas
Módulo estrecho para escobas y trapeadores. Al norte queda un paso libre hasta el banitori / pileta del rincón NW.

## Componentes
- piso a techo 2.80 m
- frente 30 cm
- fondo 62.5 cm

## Generar render

```bash
cd espacios/lavadero
python3 FURNITURE_ESCOBERO.py
```

Salida: `renders/muebles/FURNITURE_ESCOBERO.png`
