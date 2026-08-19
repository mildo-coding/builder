# Living Comedor

Carpeta de trabajo de Arqui para el espacio **Living Comedor** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta del espacio
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_PANELADO_TV.md` + `FURNITURE_PANELADO_TV.py` — Panelado TV / audio
- `FURNITURE_SOFA.md` + `FURNITURE_SOFA.py` — Sofá de estar
- `FURNITURE_MESA_CENTRO.md` + `FURNITURE_MESA_CENTRO.py` — Mesa de centro
- `FURNITURE_MUEBLE_BAR.md` + `FURNITURE_MUEBLE_BAR.py` — Mueble bar / vajillero
- `FURNITURE_MESA_COMEDOR.md` + `FURNITURE_MESA_COMEDOR.py` — Mesa de comedor
- `FURNITURE_SILLAS_COMEDOR.md` + `FURNITURE_SILLAS_COMEDOR.py` — Juego de sillas de comedor

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/living_comedor`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
python3 FURNITURE_PANELADO_TV.py
python3 FURNITURE_SOFA.py
python3 FURNITURE_MESA_CENTRO.py
python3 FURNITURE_MUEBLE_BAR.py
python3 FURNITURE_MESA_COMEDOR.py
python3 FURNITURE_SILLAS_COMEDOR.py
```

Los PNG se guardan en:
- `espacios/living_comedor/planos/`
- `espacios/living_comedor/renders/`
- `planos/living_comedor_planta.png`
- `renders/living_comedor/`

## Medidas de referencia
- Local: 5.50 × 8.00 m (44.0 m²)
- Alto: 2.50 m
