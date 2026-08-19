# Duchero moderno

Ficha de carpintería / equipamiento para **Baño de Visitas**.

## Identificación
- **Archivo:** `FURNITURE_DUCHERO`
- **Espacio:** Baño de Visitas (`bano_visitas`)
- **Tipo:** ducha

## Medidas
- **Frente:** 0.800 m
- **Profundidad:** 0.800 m
- **Alto:** 2.100 m
- **Huella en planta (w × d):** 0.800 × 0.800 m

## Ubicación
- **Descripción:** Rincón este, plato a ras de piso, columna negra.
- **Origen (x, y):** (0.00, 0.65) m desde el rincón SO del local
- **Frente hacia:** E

## Materiales
- **Grifería negra embutida** — columna y flor (clave `negro`)
- **Porcelanato gran formato** — piso y muros (clave `porcelanato`)

## Texturas
Flor de 250 mm + duchador de mano, desagüe lineal.

## Componentes
- flor 25 cm
- desagüe lineal 70 cm

## Generar render

```bash
cd espacios/bano_visitas
python3 FURNITURE_DUCHERO.py
```

Salida: `renders/muebles/FURNITURE_DUCHERO.png`
