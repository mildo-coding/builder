# Piletón de lavar

Ficha de carpintería / equipamiento para **Lavadero**.

## Identificación
- **Archivo:** `FURNITURE_PILETON`
- **Espacio:** Lavadero (`lavadero`)
- **Tipo:** pileta

## Medidas
- **Frente:** 0.500 m
- **Profundidad:** 0.400 m
- **Alto:** 0.900 m
- **Huella en planta (w × d):** 0.500 × 0.400 m

## Ubicación
- **Descripción:** Rincón noroeste, en el piso útil ganado al recortar el placard original.
- **Origen (x, y):** (0.00, 2.20) m desde el rincón SO del local
- **Frente hacia:** E

## Materiales
- **Acero inoxidable** — cuba (clave `metal`)
- **Roble tratado** — mueble bajo pileta (clave `roble`)
- **Grifería negra** — pico alto (clave `negro`)

## Texturas
Cuba profunda sobre mueble de 90 cm. Grifería negra de pico alto para palanganas.

## Componentes
- cuba 40×35×25
- mueble con estante de limpieza

## Generar render

```bash
cd espacios/lavadero
python3 FURNITURE_PILETON.py
```

Salida: `renders/muebles/FURNITURE_PILETON.png`
