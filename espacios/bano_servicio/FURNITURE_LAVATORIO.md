# Lavatorio compacto

Ficha de carpintería / equipamiento para **Baño de Servicio**.

## Identificación
- **Archivo:** `FURNITURE_LAVATORIO`
- **Espacio:** Baño de Servicio (`bano_servicio`)
- **Tipo:** pileta

## Medidas
- **Frente:** 0.450 m
- **Profundidad:** 0.320 m
- **Alto:** 0.850 m
- **Huella en planta (w × d):** 0.450 × 0.320 m

## Ubicación
- **Descripción:** Muro este, junto a la puerta, para no interferir la apertura.
- **Origen (x, y):** (0.80, 0.75) m desde el rincón SO del local
- **Frente hacia:** O

## Materiales
- **Loza blanca** — bacha (clave `blanco`)
- **Roble tratado** — ménsula (clave `roble`)
- **Grifería negra** — monocomando (clave `negro`)

## Texturas
Bacha de apoyo 45 cm sobre ménsula de madera.

## Componentes
- sifón visto negro
- espejo 40×60

## Generar render

```bash
cd espacios/bano_servicio
python3 FURNITURE_LAVATORIO.py
```

Salida: `renders/muebles/FURNITURE_LAVATORIO.png`
