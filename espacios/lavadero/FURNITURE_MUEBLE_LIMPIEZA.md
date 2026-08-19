# Mueble de limpieza

Ficha de carpintería / equipamiento para **Lavadero**.

## Identificación
- **Archivo:** `FURNITURE_MUEBLE_LIMPIEZA`
- **Espacio:** Lavadero (`lavadero`)
- **Tipo:** placard

## Medidas
- **Frente:** 0.400 m
- **Profundidad:** 0.350 m
- **Alto:** 2.000 m
- **Huella en planta (w × d):** 0.400 × 0.350 m

## Ubicación
- **Descripción:** Muro este, al norte de la torre de lavado, para productos y palo de piso.
- **Origen (x, y):** (2.23, 1.70) m desde el rincón SO del local
- **Frente hacia:** O

## Materiales
- **Grafito** — frentes (clave `grafito`)
- **Roble** — interior (clave `roble`)

## Texturas
Módulo alto y estrecho, puerta de 40 cm, interior con ganchos y bandejas.

## Componentes
- guarda escoba
- bandejas de químicos

## Generar render

```bash
cd espacios/lavadero
python3 FURNITURE_MUEBLE_LIMPIEZA.py
```

Salida: `renders/muebles/FURNITURE_MUEBLE_LIMPIEZA.png`
