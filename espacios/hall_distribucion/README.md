# Hall de Distribución

Carpeta de trabajo de Arqui para el espacio **Hall de Distribución** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta del espacio
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_CONSOLA.md` + `FURNITURE_CONSOLA.py` — Consola de recibo
- `FURNITURE_PANELADO_HALL.md` + `FURNITURE_PANELADO_HALL.py` — Panelado de hall

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/hall_distribucion`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
python3 FURNITURE_CONSOLA.py
python3 FURNITURE_PANELADO_HALL.py
```

Los PNG se guardan en:
- `espacios/hall_distribucion/planos/`
- `espacios/hall_distribucion/renders/`
- `planos/hall_distribucion_planta.png`
- `renders/hall_distribucion/`

## Medidas de referencia
- Local: 1.38 × 2.30 m (3.2 m²)
- Alto: 2.50 m
