# Biblioteca a medida

Ficha de carpintería / equipamiento para **Oficina / Estudio**.

## Identificación
- **Archivo:** `FURNITURE_BIBLIOTECA`
- **Espacio:** Oficina / Estudio (`oficina`)
- **Tipo:** estanteria

## Medidas
- **Frente:** 3.100 m
- **Profundidad:** 0.320 m
- **Alto:** 2.500 m
- **Huella en planta (w × d):** 3.100 × 0.320 m

## Ubicación
- **Descripción:** Muro norte, piso a techo, todo el ancho del local.
- **Origen (x, y):** (0.00, 1.38) m desde el rincón SO del local
- **Frente hacia:** S

## Materiales
- **Roble** — estantes y costados (clave `roble`)
- **Listones acústicos** — trasdosado (clave `petiribi`)

## Texturas
Estantes regulables, módulo cerrado inferior, listonado acústico de fondo.

## Componentes
- estantes cada 32 cm
- módulo bajo con puertas

## Generar render

```bash
cd espacios/oficina
python3 FURNITURE_BIBLIOTECA.py
```

Salida: `renders/muebles/FURNITURE_BIBLIOTECA.png`
