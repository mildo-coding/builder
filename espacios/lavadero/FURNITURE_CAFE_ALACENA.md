# Coffee station — alacena

Ficha de carpintería / equipamiento para **Lavadero**.

## Identificación
- **Archivo:** `FURNITURE_CAFE_ALACENA`
- **Espacio:** Lavadero (`lavadero`)
- **Tipo:** placard

## Medidas
- **Frente:** 1.225 m
- **Profundidad:** 0.320 m
- **Alto:** 1.250 m
- **Huella en planta (w × d):** 1.225 × 0.320 m
- **z piso:** 1.550 m

## Ubicación
- **Descripción:** Muro sur, de 1.55 m a techo. Tazas, café y vajilla de desayuno.
- **Origen (x, y):** (1.43, 0.00) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Roble** — frentes (clave `roble`)
- **Grafito** — interior (clave `grafito`)
- **LED 3000K** — tira bajo alacena (clave `blanco`)

## Texturas
Hueco 65 cm para la máquina. Dos puertas.

## Componentes
- arranque 1.55 m
- alto 1.25 m
- fondo 32 cm

## Generar render

```bash
cd espacios/lavadero
python3 FURNITURE_CAFE_ALACENA.py
```

Salida: `renders/muebles/FURNITURE_CAFE_ALACENA.png`
