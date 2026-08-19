# Placard de secado

Ficha de carpintería / equipamiento para **Lavadero**.

## Identificación
- **Archivo:** `FURNITURE_PLACARD_SECADO`
- **Espacio:** Lavadero (`lavadero`)
- **Tipo:** placard

## Medidas
- **Frente:** 1.500 m
- **Profundidad:** 0.625 m
- **Alto:** 2.500 m
- **Huella en planta (w × d):** 0.625 × 1.500 m

## Ubicación
- **Descripción:** Muro oeste. Empieza contra la pared junto a la puerta de servicio y termina con tabique sólido de 10 cm. Frente al interior del lavadero.
- **Origen (x, y):** (0.00, 0.00) m desde el rincón SO del local
- **Frente hacia:** E

## Materiales
- **Roble / petiribí** — frente piso a techo, dos hojas de 0.75 m (clave `roble`)
- **Listones ventilados** — interior / trasdosado (clave `petiribi`)
- **Metal negro** — barra perchero y herrajes (clave `metal`)

## Texturas
Carpintería piso a techo (H = 2.50 m). Veta vertical. Interior ventilado para secado de ropa, con barra a 1.80 m y reja inferior.

## Componentes
- 2 hojas 0.75 m
- barra perchero
- ventilación inferior y superior
- tabique de cierre 0.10 m

## Notas
Profundidad 0.625 m (interior ~0.60 m para perchas). Largo de frente 1.50 m.

## Generar render

```bash
cd espacios/lavadero
python3 FURNITURE_PLACARD_SECADO.py
```

Salida: `renders/muebles/FURNITURE_PLACARD_SECADO.png`
