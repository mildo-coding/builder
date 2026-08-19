# Baño de Visitas

Carpeta de trabajo de Arqui para el espacio **Baño de Visitas** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta del espacio
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_VANITORY.md` + `FURNITURE_VANITORY.py` — Vanitory con madera
- `FURNITURE_ESPEJO_RETROILUMINADO.md` + `FURNITURE_ESPEJO_RETROILUMINADO.py` — Espejo retroiluminado
- `FURNITURE_DUCHERO.md` + `FURNITURE_DUCHERO.py` — Duchero moderno

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/bano_visitas`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
python3 FURNITURE_VANITORY.py
python3 FURNITURE_ESPEJO_RETROILUMINADO.py
python3 FURNITURE_DUCHERO.py
```

Los PNG se guardan en:
- `espacios/bano_visitas/planos/`
- `espacios/bano_visitas/renders/`
- `planos/bano_visitas_planta.png`
- `renders/bano_visitas/`

## Medidas de referencia
- Local: 1.80 × 1.45 m (2.6 m²)
- Alto: 2.50 m
