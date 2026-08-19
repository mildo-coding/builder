# Juego de sillas de comedor

Ficha de carpintería / equipamiento para **Living Comedor**.

## Identificación
- **Archivo:** `FURNITURE_SILLAS_COMEDOR`
- **Espacio:** Living Comedor (`living_comedor`)
- **Tipo:** silla

## Medidas
- **Frente:** 0.500 m
- **Profundidad:** 0.550 m
- **Alto:** 0.800 m
- **Huella en planta (w × d):** 2.700 × 1.500 m

## Ubicación
- **Descripción:** Alrededor de la mesa de comedor (8 unidades, dos cabeceras).
- **Origen (x, y):** (1.40, 5.50) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Roble** — estructura (clave `roble`)
- **Lino** — asiento y respaldo (clave `lino`)

## Texturas
Silla de madera con tapizado desmontable. Perfil liviano.

## Componentes
- 8 sillas
- asiento 45 cm

## Generar render

```bash
cd espacios/living_comedor
python3 FURNITURE_SILLAS_COMEDOR.py
```

Salida: `renders/muebles/FURNITURE_SILLAS_COMEDOR.png`
