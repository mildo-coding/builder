# Consola de recibo

Ficha de carpintería / equipamiento para **Hall de Distribución**.

## Identificación
- **Archivo:** `FURNITURE_CONSOLA`
- **Espacio:** Hall de Distribución (`hall_distribucion`)
- **Tipo:** mesa

## Medidas
- **Frente:** 1.000 m
- **Profundidad:** 0.320 m
- **Alto:** 0.800 m
- **Huella en planta (w × d):** 1.000 × 0.320 m

## Ubicación
- **Descripción:** Muro largo, apoyo para llaves, bandeja y punto de luz.
- **Origen (x, y):** (0.19, 1.40) m desde el rincón SO del local
- **Frente hacia:** S

## Materiales
- **Roble** — tablero y fuste (clave `roble`)
- **Metal negro** — herraje (clave `metal`)

## Texturas
Consola liviana de 32 cm de fondo para no estrechar la circulación.

## Componentes
- cajón único
- bandeja

## Generar render

```bash
cd espacios/hall_distribucion
python3 FURNITURE_CONSOLA.py
```

Salida: `renders/muebles/FURNITURE_CONSOLA.png`
