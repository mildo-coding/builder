# Vanitory flotante

Ficha de carpintería / equipamiento para **Baño Principal (en suite)**.

## Identificación
- **Archivo:** `FURNITURE_VANITORY`
- **Espacio:** Baño Principal (en suite) (`bano_principal`)
- **Tipo:** vanitory

## Medidas
- **Frente:** 1.000 m
- **Profundidad:** 0.450 m
- **Alto:** 0.400 m
- **Huella en planta (w × d):** 1.000 × 0.450 m

## Ubicación
- **Descripción:** Muro sur, volado a 0.20 m del piso, sobre revestimiento de gran formato.
- **Origen (x, y):** (0.70, 0.00) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Roble tratado contra humedad** — cajón flotante (clave `roble`)
- **Loza / Silestone** — encimera y bacha (clave `silestone`)
- **Grifería negra embutida** — monocomando mural (clave `negro`)

## Texturas
Cajón único con frente integrado, bacha de apoyo, grifería mural negra.

## Componentes
- volado 20 cm
- cajón soft-close
- LED bajo mueble

## Generar render

```bash
cd espacios/bano_principal
python3 FURNITURE_VANITORY.py
```

Salida: `renders/muebles/FURNITURE_VANITORY.png`
