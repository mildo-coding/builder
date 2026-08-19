# Vestidor / placard

Ficha de carpintería / equipamiento para **Dormitorio Principal**.

## Identificación
- **Archivo:** `FURNITURE_PLACARD_VESTIDOR`
- **Espacio:** Dormitorio Principal (`dormitorio_principal`)
- **Tipo:** placard

## Medidas
- **Frente:** 2.400 m
- **Profundidad:** 0.600 m
- **Alto:** 2.500 m
- **Huella en planta (w × d):** 3.230 × 0.600 m

## Ubicación
- **Descripción:** Tramo norte/circulación del dormitorio, frente continuo piso a techo.
- **Origen (x, y):** (0.00, 3.80) m desde el rincón SO del local
- **Frente hacia:** S

## Materiales
- **Roble** — frentes (clave `roble`)
- **Grafito** — interior (clave `grafito`)

## Texturas
Puertas piso a techo, interior con barra, cajonera y zapatero.

## Componentes
- barra doble
- cajonera central
- LED interior

## Generar render

```bash
cd espacios/dormitorio_principal
python3 FURNITURE_PLACARD_VESTIDOR.py
```

Salida: `renders/muebles/FURNITURE_PLACARD_VESTIDOR.png`
