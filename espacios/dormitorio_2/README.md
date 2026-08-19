# Dormitorio 2

Carpeta de trabajo de Arqui para el espacio **Dormitorio 2** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta del espacio
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_CAMA_QUEEN.md` + `FURNITURE_CAMA_QUEEN.py` — Cama Queen
- `FURNITURE_MESA_NOCHE_2.md` + `FURNITURE_MESA_NOCHE_2.py` — Mesa de noche
- `FURNITURE_PLACARD.md` + `FURNITURE_PLACARD.py` — Placard de frente continuo

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/dormitorio_2`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
python3 FURNITURE_CAMA_QUEEN.py
python3 FURNITURE_MESA_NOCHE_2.py
python3 FURNITURE_PLACARD.py
```

Los PNG se guardan en:
- `espacios/dormitorio_2/planos/`
- `espacios/dormitorio_2/renders/`
- `planos/dormitorio_2_planta.png`
- `renders/dormitorio_2/`

## Medidas de referencia
- Local: 3.67 × 4.09 m (15.0 m²)
- Alto: 2.50 m
