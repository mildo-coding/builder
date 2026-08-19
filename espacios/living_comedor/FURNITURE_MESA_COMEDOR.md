# Mesa de comedor

Ficha de carpintería / equipamiento para **Living Comedor**.

## Identificación
- **Archivo:** `FURNITURE_MESA_COMEDOR`
- **Espacio:** Living Comedor (`living_comedor`)
- **Tipo:** mesa

## Medidas
- **Frente:** 2.400 m
- **Profundidad:** 1.100 m
- **Alto:** 0.750 m
- **Huella en planta (w × d):** 2.400 × 1.100 m

## Ubicación
- **Descripción:** Sector norte del local, próxima a la salida al balcón.
- **Origen (x, y):** (1.55, 5.70) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Roble de Eslavonia** — tablero 40 mm (clave `roble`)
- **Metal negro** — base (clave `metal`)

## Texturas
Tablero de madera maciza, canto vivo, base metálica en T.

## Componentes
- 8 puestos habituales
- extensible a 10

## Generar render

```bash
cd espacios/living_comedor
python3 FURNITURE_MESA_COMEDOR.py
```

Salida: `renders/muebles/FURNITURE_MESA_COMEDOR.png`
