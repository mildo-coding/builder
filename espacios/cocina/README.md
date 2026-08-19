# Cocina Principal

Carpeta de trabajo de Arqui para el espacio **Cocina Principal** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta del espacio
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_BAJO_MESADA.md` + `FURNITURE_BAJO_MESADA.py` — Bajo mesada
- `FURNITURE_MESADA.md` + `FURNITURE_MESADA.py` — Mesada Silestone
- `FURNITURE_ALACENA.md` + `FURNITURE_ALACENA.py` — Alacenas superiores
- `FURNITURE_TORRE_HORNOS.md` + `FURNITURE_TORRE_HORNOS.py` — Torre de hornos

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/cocina`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
python3 FURNITURE_BAJO_MESADA.py
python3 FURNITURE_MESADA.py
python3 FURNITURE_ALACENA.py
python3 FURNITURE_TORRE_HORNOS.py
```

Los PNG se guardan en:
- `espacios/cocina/planos/`
- `espacios/cocina/renders/`
- `planos/cocina_planta.png`
- `renders/cocina/`

## Medidas de referencia
- Local: 2.00 × 3.69 m (7.4 m²)
- Alto: 2.50 m
