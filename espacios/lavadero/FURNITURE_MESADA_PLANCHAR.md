# Mesada de planchado

Ficha de carpintería / equipamiento para **Lavadero**.

## Identificación
- **Archivo:** `FURNITURE_MESADA_PLANCHAR`
- **Espacio:** Lavadero (`lavadero`)
- **Tipo:** mesada

## Medidas
- **Frente:** 1.480 m
- **Profundidad:** 0.600 m
- **Alto:** 0.020 m
- **Huella en planta (w × d):** 1.480 × 0.600 m
- **z piso:** 0.850 m

## Ubicación
- **Descripción:** Muro norte. Tablero 1.48 × 0.60 m a la misma altura que el tope de pileta (0.85 m).
- **Origen (x, y):** (0.51, 2.20) m desde el rincón SO del local
- **Frente hacia:** S

## Materiales
- **Silestone / compacto blanco cálido** — tablero 20 mm (clave `silestone`)
- **Opcional paño de planchar** — protección térmica móvil (clave `lino`)

## Texturas
Cubre lavarropas y sigue hacia el este. Cota superior 0.85 m.

## Componentes
- espesor 2 cm
- cota 0.85 m
- largo 1.48 m
- fondo 60 cm

## Generar render

```bash
cd espacios/lavadero
python3 FURNITURE_MESADA_PLANCHAR.py
```

Salida: `renders/muebles/FURNITURE_MESADA_PLANCHAR.png`
