# Cama Queen

Ficha de carpintería / equipamiento para **Dormitorio 2**.

## Identificación
- **Archivo:** `FURNITURE_CAMA_QUEEN`
- **Espacio:** Dormitorio 2 (`dormitorio_2`)
- **Tipo:** cama

## Medidas
- **Frente:** 1.600 m
- **Profundidad:** 2.000 m
- **Alto:** 0.450 m
- **Huella en planta (w × d):** 1.600 × 2.000 m

## Ubicación
- **Descripción:** Eje del cuarto, cabecera contra muro sur.
- **Origen (x, y):** (1.03, 1.10) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Lino** — respaldo tapizado (clave `lino`)
- **Roble** — patas (clave `roble`)

## Texturas
Cama 160×200, respaldo tapizado bajo. Alternativa: dos camas de 0.90.

## Componentes
- colchón Queen
- opción 2×90 cm

## Generar render

```bash
cd espacios/dormitorio_2
python3 FURNITURE_CAMA_QUEEN.py
```

Salida: `renders/muebles/FURNITURE_CAMA_QUEEN.png`
