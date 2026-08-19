# Respaldo panelado

Ficha de carpintería / equipamiento para **Dormitorio Principal**.

## Identificación
- **Archivo:** `FURNITURE_RESPALDO_MADERA`
- **Espacio:** Dormitorio Principal (`dormitorio_principal`)
- **Tipo:** panel

## Medidas
- **Frente:** 2.400 m
- **Profundidad:** 0.080 m
- **Alto:** 1.200 m
- **Huella en planta (w × d):** 2.400 × 0.080 m

## Ubicación
- **Descripción:** Muro de cabecera, integrando mesas de noche flotantes y LED.
- **Origen (x, y):** (0.42, 1.32) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Roble** — panelado (clave `roble`)
- **LED 2700K** — garganta superior (clave `blanco`)

## Texturas
Panelado horizontal de 1.20 m de alto, continuo detrás de la cama.

## Componentes
- LED indirecta
- encuentros con mesas flotantes

## Generar render

```bash
cd espacios/dormitorio_principal
python3 FURNITURE_RESPALDO_MADERA.py
```

Salida: `renders/muebles/FURNITURE_RESPALDO_MADERA.png`
