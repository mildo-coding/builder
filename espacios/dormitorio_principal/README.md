# Dormitorio Principal

Carpeta de trabajo de Arqui para el espacio **Dormitorio Principal** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta del espacio
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_CAMA_KING.md` + `FURNITURE_CAMA_KING.py` — Cama King Size
- `FURNITURE_RESPALDO_MADERA.md` + `FURNITURE_RESPALDO_MADERA.py` — Respaldo panelado
- `FURNITURE_MESAS_NOCHE.md` + `FURNITURE_MESAS_NOCHE.py` — Mesas de noche flotantes
- `FURNITURE_PLACARD_VESTIDOR.md` + `FURNITURE_PLACARD_VESTIDOR.py` — Vestidor / placard

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/dormitorio_principal`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
python3 FURNITURE_CAMA_KING.py
python3 FURNITURE_RESPALDO_MADERA.py
python3 FURNITURE_MESAS_NOCHE.py
python3 FURNITURE_PLACARD_VESTIDOR.py
```

Los PNG se guardan en:
- `espacios/dormitorio_principal/planos/`
- `espacios/dormitorio_principal/renders/`
- `planos/dormitorio_principal_planta.png`
- `renders/dormitorio_principal/`

## Medidas de referencia
- Local: 3.23 × 5.05 m (16.3 m²)
- Alto: 2.50 m
