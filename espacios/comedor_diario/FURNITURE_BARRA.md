# Barra de conexión con cocina

Ficha de carpintería / equipamiento para **Comedor Diario**.

## Identificación
- **Archivo:** `FURNITURE_BARRA`
- **Espacio:** Comedor Diario (`comedor_diario`)
- **Tipo:** mesada

## Medidas
- **Frente:** 1.600 m
- **Profundidad:** 0.400 m
- **Alto:** 1.100 m
- **Huella en planta (w × d):** 1.600 × 0.400 m

## Ubicación
- **Descripción:** Umbral hacia la cocina, pasaplatos / apoyo de 40 cm de fondo.
- **Origen (x, y):** (0.24, 0.00) m desde el rincón SO del local
- **Frente hacia:** S

## Materiales
- **Roble** — tablero 40 mm (clave `roble`)
- **Perfilería negra** — cerramiento opcional de vidrio (clave `metal`)

## Texturas
Barra de madera a 1.10 m. Opcional: paños de vidrio con perfil negro.

## Componentes
- pasaplatos
- 2 banquetas altas opcionales

## Generar render

```bash
cd espacios/comedor_diario
python3 FURNITURE_BARRA.py
```

Salida: `renders/muebles/FURNITURE_BARRA.png`
