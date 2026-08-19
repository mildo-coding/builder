# Espejo retroiluminado

Ficha de carpintería / equipamiento para **Baño de Visitas**.

## Identificación
- **Archivo:** `FURNITURE_ESPEJO_RETROILUMINADO`
- **Espacio:** Baño de Visitas (`bano_visitas`)
- **Tipo:** espejo

## Medidas
- **Frente:** 0.900 m
- **Profundidad:** 0.040 m
- **Alto:** 0.900 m
- **Huella en planta (w × d):** 0.900 × 0.040 m

## Ubicación
- **Descripción:** Sobre el vanitory, centrado, LED perimetral 3000K.
- **Origen (x, y):** (0.70, 0.00) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Espejo 4 mm** — luna (clave `vidrio`)
- **LED 3000K** — halo perimetral (clave `blanco`)

## Texturas
Luna rectangular con halo LED difuso, sin marco visto.

## Componentes
- 90 × 90 cm
- IP44

## Generar render

```bash
cd espacios/bano_visitas
python3 FURNITURE_ESPEJO_RETROILUMINADO.py
```

Salida: `renders/muebles/FURNITURE_ESPEJO_RETROILUMINADO.png`
