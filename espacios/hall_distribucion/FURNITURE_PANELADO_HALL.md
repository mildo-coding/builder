# Panelado de hall

Ficha de carpintería / equipamiento para **Hall de Distribución**.

## Identificación
- **Archivo:** `FURNITURE_PANELADO_HALL`
- **Espacio:** Hall de Distribución (`hall_distribucion`)
- **Tipo:** panel

## Medidas
- **Frente:** 2.300 m
- **Profundidad:** 0.030 m
- **Alto:** 1.200 m
- **Huella en planta (w × d):** 0.030 × 2.300 m

## Ubicación
- **Descripción:** Muro oeste o este, zócalo-panel de 1.20 m que unifica la transición.
- **Origen (x, y):** (0.00, 0.00) m desde el rincón SO del local
- **Frente hacia:** E

## Materiales
- **Roble** — listones (clave `roble`)
- **LED 2700K** — garganta de cielorraso (clave `blanco`)

## Texturas
Listonado horizontal de 1.20 m, continuo, con encuentro a puertas.

## Componentes
- zócalo integrado
- luz de cornisamento

## Generar render

```bash
cd espacios/hall_distribucion
python3 FURNITURE_PANELADO_HALL.py
```

Salida: `renders/muebles/FURNITURE_PANELADO_HALL.png`
