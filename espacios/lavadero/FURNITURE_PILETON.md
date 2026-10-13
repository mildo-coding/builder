# Pileta de lavar

Ficha de carpintería / equipamiento para **Lavadero**.

## Identificación
- **Archivo:** `FURNITURE_PILETON`
- **Espacio:** Lavadero (`lavadero`)
- **Tipo:** pileta

## Medidas
- **Frente:** 0.405 m
- **Profundidad:** 0.500 m
- **Alto:** 0.350 m
- **Huella en planta (w × d):** 0.500 × 0.405 m
- **z piso:** 0.500 m

## Ubicación
- **Descripción:** Muro oeste, rincón NW. Cuba de 0.50 m a 0.85 m de altura. Visible también desde el alzado norte.
- **Origen (x, y):** (0.00, 2.00) m desde el rincón SO del local
- **Frente hacia:** E

## Materiales
- **Acero inoxidable** — cuba (clave `metal`)
- **Grifería negra** — pico alto (clave `negro`)

## Texturas
Entre el escobero y el banitori queda un paso; la pileta cuelga / apoya en el tramo norte del oeste. Cota superior 0.85 m = mesada de planchar.

## Componentes
- cuba 40×35×25
- cota superior 0.85 m

## Generar render

```bash
cd espacios/lavadero
python3 FURNITURE_PILETON.py
```

Salida: `renders/muebles/FURNITURE_PILETON.png`
