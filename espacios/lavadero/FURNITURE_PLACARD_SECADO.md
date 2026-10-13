# Placard de secado

Ficha de carpintería / equipamiento para **Lavadero**.

## Identificación
- **Archivo:** `FURNITURE_PLACARD_SECADO`
- **Espacio:** Lavadero (`lavadero`)
- **Tipo:** placard

## Medidas
- **Frente:** 1.500 m
- **Profundidad:** 0.625 m
- **Alto:** 2.800 m
- **Huella en planta (w × d):** 0.625 × 1.500 m
- **z piso:** 0.000 m

## Ubicación
- **Descripción:** Muro oeste, desde la puerta de servicio hacia el norte. Piso a techo.
- **Origen (x, y):** (0.00, 0.00) m desde el rincón SO del local
- **Frente hacia:** E

## Materiales
- **Roble / petiribí** — frente piso a techo, dos hojas de 0.75 m (clave `roble`)
- **Listones ventilados** — interior / trasdosado (clave `petiribi`)
- **Metal negro** — barra perchero y herrajes (clave `metal`)

## Texturas
Carpintería piso a techo. Interior ventilado para secado, barra a 1.80 m.

## Componentes
- 2 hojas 0.75 m
- barra perchero
- ventilación inferior y superior

## Notas
Profundidad 0.625 m. Largo de frente 1.50 m.

## Generar render

```bash
cd espacios/lavadero
python3 FURNITURE_PLACARD_SECADO.py
```

Salida: `renders/muebles/FURNITURE_PLACARD_SECADO.png`
