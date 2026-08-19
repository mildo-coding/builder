# Mueble bar / vajillero

Ficha de carpintería / equipamiento para **Living Comedor**.

## Identificación
- **Archivo:** `FURNITURE_MUEBLE_BAR`
- **Espacio:** Living Comedor (`living_comedor`)
- **Tipo:** placard

## Medidas
- **Frente:** 1.800 m
- **Profundidad:** 0.450 m
- **Alto:** 1.200 m
- **Huella en planta (w × d):** 0.450 × 1.800 m

## Ubicación
- **Descripción:** Muro oeste, entre estar y comedor, a medida contra pared.
- **Origen (x, y):** (0.00, 3.60) m desde el rincón SO del local
- **Frente hacia:** E

## Materiales
- **Petiribí** — frente y costados (clave `petiribi`)
- **LED 2700K** — estante vidrio iluminado (clave `blanco`)
- **Grafito** — interior (clave `grafito`)

## Texturas
Frentes lisos con tirador integrado. Estante superior vidrio + LED.

## Componentes
- botellero
- vajilla
- iluminación indirecta

## Generar render

```bash
cd espacios/living_comedor
python3 FURNITURE_MUEBLE_BAR.py
```

Salida: `renders/muebles/FURNITURE_MUEBLE_BAR.png`
