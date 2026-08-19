# Mampara de ducha

Ficha de carpintería / equipamiento para **Baño Principal (en suite)**.

## Identificación
- **Archivo:** `FURNITURE_MAMPARA`
- **Espacio:** Baño Principal (en suite) (`bano_principal`)
- **Tipo:** vidrio

## Medidas
- **Frente:** 0.900 m
- **Profundidad:** 0.080 m
- **Alto:** 2.000 m
- **Huella en planta (w × d):** 0.080 × 0.900 m

## Ubicación
- **Descripción:** Cierre de la ducha en el extremo este, vidrio templado 8 mm.
- **Origen (x, y):** (0.00, 0.80) m desde el rincón SO del local
- **Frente hacia:** E

## Materiales
- **Vidrio templado** — hoja fija + abatible (clave `vidrio`)
- **Perfil negro mate** — herrajes (clave `metal`)

## Texturas
Hoja fija + batiente, perfil mínimo negro, sin umbral alto.

## Componentes
- vidrio 8 mm
- herraje negro

## Generar render

```bash
cd espacios/bano_principal
python3 FURNITURE_MAMPARA.py
```

Salida: `renders/muebles/FURNITURE_MAMPARA.png`
