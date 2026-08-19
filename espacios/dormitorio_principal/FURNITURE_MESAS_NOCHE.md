# Mesas de noche flotantes

Ficha de carpintería / equipamiento para **Dormitorio Principal**.

## Identificación
- **Archivo:** `FURNITURE_MESAS_NOCHE`
- **Espacio:** Dormitorio Principal (`dormitorio_principal`)
- **Tipo:** mesa

## Medidas
- **Frente:** 0.500 m
- **Profundidad:** 0.350 m
- **Alto:** 0.120 m
- **Huella en planta (w × d):** 0.500 × 0.350 m

## Ubicación
- **Descripción:** A ambos lados de la cama, voladas del respaldo a 0.55 m del piso.
- **Origen (x, y):** (0.42, 1.40) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Roble** — cajón volado (clave `roble`)
- **Metal negro** — herraje invisible (clave `metal`)

## Texturas
Par de cajones flotantes, canto fino, sin patas.

## Componentes
- 2 unidades 50×35×12 cm
- toma USB oculta

## Notas
La ficha representa una unidad; se colocan en espejo a izquierda y derecha.

## Generar render

```bash
cd espacios/dormitorio_principal
python3 FURNITURE_MESAS_NOCHE.py
```

Salida: `renders/muebles/FURNITURE_MESAS_NOCHE.png`
