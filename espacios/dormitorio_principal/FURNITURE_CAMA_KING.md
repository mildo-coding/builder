# Cama King Size

Ficha de carpintería / equipamiento para **Dormitorio Principal**.

## Identificación
- **Archivo:** `FURNITURE_CAMA_KING`
- **Espacio:** Dormitorio Principal (`dormitorio_principal`)
- **Tipo:** cama

## Medidas
- **Frente:** 2.000 m
- **Profundidad:** 2.000 m
- **Alto:** 0.450 m
- **Huella en planta (w × d):** 2.000 × 2.000 m

## Ubicación
- **Descripción:** Eje del dormitorio, cabecera contra el respaldo de madera (muro sur).
- **Origen (x, y):** (0.62, 1.40) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Lino** — cabecera tapizada bajo el panel (clave `lino`)
- **Roble** — base (clave `roble`)

## Texturas
Base tapizada, colchón 200×200, ropa de cama tono arena.

## Componentes
- colchón King 200×200
- base 45 cm

## Generar render

```bash
cd espacios/dormitorio_principal
python3 FURNITURE_CAMA_KING.py
```

Salida: `renders/muebles/FURNITURE_CAMA_KING.png`
