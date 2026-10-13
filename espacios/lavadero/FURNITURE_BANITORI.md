# Mueble banitori

Ficha de carpintería / equipamiento para **Lavadero**.

## Identificación
- **Archivo:** `FURNITURE_BANITORI`
- **Espacio:** Lavadero (`lavadero`)
- **Tipo:** placard

## Medidas
- **Frente:** 0.510 m
- **Profundidad:** 0.600 m
- **Alto:** 0.850 m
- **Huella en planta (w × d):** 0.510 × 0.600 m
- **z piso:** 0.000 m

## Ubicación
- **Descripción:** Rincón NW, muro norte. Bajo de apoyo hasta 0.85 m (misma cota que la pileta).
- **Origen (x, y):** (0.00, 2.20) m desde el rincón SO del local
- **Frente hacia:** S

## Materiales
- **Roble** — frentes (clave `roble`)
- **Grafito** — interior (clave `grafito`)

## Texturas
Mueble bajo junto a la pileta. Visible en alzado norte y oeste.

## Componentes
- alto 0.85 m
- fondo 60 cm
- frente 51 cm

## Generar render

```bash
cd espacios/lavadero
python3 FURNITURE_BANITORI.py
```

Salida: `renders/muebles/FURNITURE_BANITORI.png`
