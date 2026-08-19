# Mesa desayunador

Ficha de carpintería / equipamiento para **Comedor Diario**.

## Identificación
- **Archivo:** `FURNITURE_MESA_DESAYUNADOR`
- **Espacio:** Comedor Diario (`comedor_diario`)
- **Tipo:** mesa

## Medidas
- **Frente:** 1.200 m
- **Profundidad:** 0.800 m
- **Alto:** 0.750 m
- **Huella en planta (w × d):** 1.200 × 0.800 m

## Ubicación
- **Descripción:** Centro del local, junto al ventanal.
- **Origen (x, y):** (0.44, 1.20) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Roble** — tablero (clave `roble`)
- **Metal negro** — patas (clave `metal`)

## Texturas
Mesa cuadrada-rectangular para 4, canto vivo.

## Componentes
- 4 puestos

## Generar render

```bash
cd espacios/comedor_diario
python3 FURNITURE_MESA_DESAYUNADOR.py
```

Salida: `renders/muebles/FURNITURE_MESA_DESAYUNADOR.png`
