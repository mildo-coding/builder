# Oficina / Estudio

Carpeta de trabajo de Arqui para el espacio **Oficina / Estudio** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta del espacio
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_ESCRITORIO.md` + `FURNITURE_ESCRITORIO.py` — Escritorio corrido
- `FURNITURE_BIBLIOTECA.md` + `FURNITURE_BIBLIOTECA.py` — Biblioteca a medida
- `FURNITURE_SILLA_ESCRITORIO.md` + `FURNITURE_SILLA_ESCRITORIO.py` — Silla de trabajo

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/oficina`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
python3 FURNITURE_ESCRITORIO.py
python3 FURNITURE_BIBLIOTECA.py
python3 FURNITURE_SILLA_ESCRITORIO.py
```

Los PNG se guardan en:
- `espacios/oficina/planos/`
- `espacios/oficina/renders/`
- `planos/oficina_planta.png`
- `renders/oficina/`

## Medidas de referencia
- Local: 3.10 × 1.70 m (5.3 m²)
- Alto: 2.50 m
