# Baño de Servicio

Carpeta de trabajo de Arqui para el espacio **Baño de Servicio** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta del espacio
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_INODORO.md` + `FURNITURE_INODORO.py` — Inodoro compacto
- `FURNITURE_LAVATORIO.md` + `FURNITURE_LAVATORIO.py` — Lavatorio compacto

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/bano_servicio`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
python3 FURNITURE_INODORO.py
python3 FURNITURE_LAVATORIO.py
```

Los PNG se guardan en:
- `espacios/bano_servicio/planos/`
- `espacios/bano_servicio/renders/`
- `planos/bano_servicio_planta.png`
- `renders/bano_servicio/`

## Medidas de referencia
- Local: 1.30 × 1.20 m (1.6 m²)
- Alto: 2.50 m
