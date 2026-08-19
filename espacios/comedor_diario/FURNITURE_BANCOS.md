# Sillas / bancos del nook

Ficha de carpintería / equipamiento para **Comedor Diario**.

## Identificación
- **Archivo:** `FURNITURE_BANCOS`
- **Espacio:** Comedor Diario (`comedor_diario`)
- **Tipo:** silla

## Medidas
- **Frente:** 0.450 m
- **Profundidad:** 0.450 m
- **Alto:** 0.780 m
- **Huella en planta (w × d):** 1.500 × 1.100 m

## Ubicación
- **Descripción:** Alrededor de la mesa desayunador.
- **Origen (x, y):** (0.30, 1.05) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Roble** — estructura (clave `roble`)
- **Lino** — asiento (clave `lino`)

## Texturas
Cuatro sillas livianas, mismo lenguaje que el comedor principal.

## Componentes
- 4 unidades

## Generar render

```bash
cd espacios/comedor_diario
python3 FURNITURE_BANCOS.py
```

Salida: `renders/muebles/FURNITURE_BANCOS.png`
