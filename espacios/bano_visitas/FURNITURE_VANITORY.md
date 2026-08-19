# Vanitory con madera

Ficha de carpintería / equipamiento para **Baño de Visitas**.

## Identificación
- **Archivo:** `FURNITURE_VANITORY`
- **Espacio:** Baño de Visitas (`bano_visitas`)
- **Tipo:** vanitory

## Medidas
- **Frente:** 0.900 m
- **Profundidad:** 0.450 m
- **Alto:** 0.400 m
- **Huella en planta (w × d):** 0.900 × 0.450 m

## Ubicación
- **Descripción:** Muro sur, flotante, alineado con el espejo retroiluminado.
- **Origen (x, y):** (0.70, 0.00) m desde el rincón SO del local
- **Frente hacia:** N

## Materiales
- **Roble tratado** — mueble (clave `roble`)
- **Silestone** — tapa (clave `silestone`)
- **Grifería negra** — monocomando (clave `negro`)

## Texturas
Vanitory de un cajón, bacha integrada, mismo lenguaje que la suite.

## Componentes
- cajón 90 cm
- sifón oculto

## Generar render

```bash
cd espacios/bano_visitas
python3 FURNITURE_VANITORY.py
```

Salida: `renders/muebles/FURNITURE_VANITORY.png`
