# Inodoro

Ficha de carpintería / equipamiento para **Baño Principal (en suite)**.

## Identificación
- **Archivo:** `FURNITURE_INODORO`
- **Espacio:** Baño Principal (en suite) (`bano_principal`)
- **Tipo:** sanitario

## Medidas
- **Frente:** 0.370 m
- **Profundidad:** 0.680 m
- **Alto:** 0.400 m
- **Huella en planta (w × d):** 0.370 × 0.680 m

## Ubicación
- **Descripción:** Muro norte, alineado con el vanitory en la circulación.
- **Origen (x, y):** (1.40, 0.70) m desde el rincón SO del local
- **Frente hacia:** S

## Materiales
- **Loza blanca** — cuerpo (clave `blanco`)
- **Tapa madera** — asiento (clave `roble`)

## Texturas
Línea suspendida o adosada de perfil compacto, depósito dual.

## Componentes
- depósito dual

## Generar render

```bash
cd espacios/bano_principal
python3 FURNITURE_INODORO.py
```

Salida: `renders/muebles/FURNITURE_INODORO.png`
