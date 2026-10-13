# Coffee station — bajo

Ficha de carpintería / equipamiento para **Lavadero**.

## Identificación
- **Archivo:** `FURNITURE_CAFE_BAJO`
- **Espacio:** Lavadero (`lavadero`)
- **Tipo:** placard

## Medidas
- **Frente:** 1.225 m
- **Profundidad:** 0.500 m
- **Alto:** 0.880 m
- **Huella en planta (w × d):** 1.225 × 0.500 m
- **z piso:** 0.000 m

## Ubicación
- **Descripción:** Muro sur, al este de la puerta de servicio. Frente al local (norte).
- **Origen (x, y):** (1.43, 0.00) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Roble** — frentes de cajones y puerta (clave `roble`)
- **Grafito** — interior (clave `grafito`)

## Texturas
Minibar 45 cm + cajones/puerta 77.5 cm. La hoja de la puerta se estaciona contra el costado oeste del mueble.

## Componentes
- minibar 45 cm
- 2 cajones
- zócalo 8 cm

## Generar render

```bash
cd espacios/lavadero
python3 FURNITURE_CAFE_BAJO.py
```

Salida: `renders/muebles/FURNITURE_CAFE_BAJO.png`
