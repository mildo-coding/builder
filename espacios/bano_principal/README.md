# Baño Principal (en suite)

Carpeta de trabajo de Arqui para el espacio **Baño Principal (en suite)** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta del espacio
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_VANITORY.md` + `FURNITURE_VANITORY.py` — Vanitory flotante
- `FURNITURE_MAMPARA.md` + `FURNITURE_MAMPARA.py` — Mampara de ducha
- `FURNITURE_INODORO.md` + `FURNITURE_INODORO.py` — Inodoro

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/bano_principal`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
python3 FURNITURE_VANITORY.py
python3 FURNITURE_MAMPARA.py
python3 FURNITURE_INODORO.py
```

Los PNG se guardan en:
- `espacios/bano_principal/planos/`
- `espacios/bano_principal/renders/`
- `planos/bano_principal_planta.png`
- `renders/bano_principal/`

## Medidas de referencia
- Local: 1.88 × 1.49 m (2.8 m²)
- Alto: 2.50 m
