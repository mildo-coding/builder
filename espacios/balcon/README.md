# Balcón / Terraza

Carpeta de trabajo de Arqui para el espacio **Balcón / Terraza** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta del espacio
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_DECK.md` + `FURNITURE_DECK.py` — Deck / solado exterior
- `FURNITURE_LOUNGE_EXTERIOR.md` + `FURNITURE_LOUNGE_EXTERIOR.py` — Lounge exterior
- `FURNITURE_MESA_BAJA.md` + `FURNITURE_MESA_BAJA.py` — Mesa baja exterior
- `FURNITURE_MACETEROS.md` + `FURNITURE_MACETEROS.py` — Maceteros y vegetación

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/balcon`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
python3 FURNITURE_DECK.py
python3 FURNITURE_LOUNGE_EXTERIOR.py
python3 FURNITURE_MESA_BAJA.py
python3 FURNITURE_MACETEROS.py
```

Los PNG se guardan en:
- `espacios/balcon/planos/`
- `espacios/balcon/renders/`
- `planos/balcon_planta.png`
- `renders/balcon/`

## Medidas de referencia
- Local: 5.50 × 2.01 m (11.0 m²)
- Alto: 2.50 m
