# Mueble divisor lavadero–cocina

Ficha de carpintería / equipamiento para **Lavadero**.

## Identificación
- **Archivo:** `FURNITURE_MUEBLE_DIVISOR`
- **Espacio:** Lavadero (`lavadero`)
- **Tipo:** placard

## Medidas
- **Frente:** 1.200 m
- **Profundidad:** 0.600 m
- **Alto:** 2.800 m
- **Huella en planta (w × d):** 0.600 × 1.200 m
- **z piso:** 0.000 m

## Ubicación
- **Descripción:** Cierre este del tramo norte (sin muro de obra). 1.20 × 0.60 × 2.80 m. Inferior al lavadero (cestos), medio a cocina (columna de cocción), superior baulera.
- **Origen (x, y):** (1.48, 1.60) m desde el rincón SO del local
- **Frente hacia:** O

## Materiales
- **MDF laqueado grafito** — frente cocina (clave `grafito`)
- **Melamina roble** — frente lavadero e interiores (clave `roble`)

## Texturas
Tres bandas: 0–0.70 cestos al lavadero; 0.70–1.90 columna horno/micro a cocina + alacena ciega al lavadero; 1.90–2.80 baulera push-to-open.

## Componentes
- cestos extraíbles 0–0.70
- columna cocción a cocina
- baulera 1.90–2.80

## Generar render

```bash
cd espacios/lavadero
python3 FURNITURE_MUEBLE_DIVISOR.py
```

Salida: `renders/muebles/FURNITURE_MUEBLE_DIVISOR.png`
