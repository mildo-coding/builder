# Lavadero

Carpeta de trabajo de Arqui para el espacio **Lavadero** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta detallada 1:20 (placard ajustado 1.50 × 0.625)
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_PLACARD_SECADO.md` + `FURNITURE_PLACARD_SECADO.py` — Placard de secado
- `FURNITURE_LAVARROPAS.md` + `FURNITURE_LAVARROPAS.py` — Lavarropas
- `FURNITURE_SECARROPAS.md` + `FURNITURE_SECARROPAS.py` — Secarropas
- `FURNITURE_PILETON.md` + `FURNITURE_PILETON.py` — Piletón de lavar
- `FURNITURE_MUEBLE_LIMPIEZA.md` + `FURNITURE_MUEBLE_LIMPIEZA.py` — Mueble de limpieza

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/lavadero`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
python3 FURNITURE_PLACARD_SECADO.py
python3 FURNITURE_LAVARROPAS.py
python3 FURNITURE_SECARROPAS.py
python3 FURNITURE_PILETON.py
python3 FURNITURE_MUEBLE_LIMPIEZA.py
```

Los PNG se guardan en:
- `espacios/lavadero/planos/` (incluye la lámina detallada `lavadero_planta.png`)
- `espacios/lavadero/renders/`
- `espacios/lavadero/renders/`
- `planos/lavadero_planta.png`
- `renders/lavadero/`

## Medidas de referencia
- Local: 2.00 × 2.81 m (5.6 m²)
- Alto: 2.50 m
