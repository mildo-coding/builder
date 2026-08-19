# Comedor Diario

Carpeta de trabajo de Arqui para el espacio **Comedor Diario** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta del espacio
- `generar_renders.py` — planta + axonométrica + fichas de todos los muebles
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_MESA_DESAYUNADOR.md` + `FURNITURE_MESA_DESAYUNADOR.py` — Mesa desayunador
- `FURNITURE_BANCOS.md` + `FURNITURE_BANCOS.py` — Sillas / bancos del nook
- `FURNITURE_BARRA.md` + `FURNITURE_BARRA.py` — Barra de conexión con cocina

## Cómo generar (solo a pedido del usuario)

Arqui no ejecuta estos comandos salvo que el usuario lo pida. El usuario elige cuándo hacer el render.

Desde esta carpeta (`espacios/comedor_diario`):

```bash
# Planta
python3 generar_plano.py

# Renders del espacio y de cada mueble
python3 generar_renders.py

# Atajo
python3 generar_todo.py

# Un mueble puntual
python3 FURNITURE_MESA_DESAYUNADOR.py
python3 FURNITURE_BANCOS.py
python3 FURNITURE_BARRA.py
```

Los PNG se guardan en:
- `espacios/comedor_diario/planos/`
- `espacios/comedor_diario/renders/`
- `planos/comedor_diario_planta.png`
- `renders/comedor_diario/`

## Medidas de referencia
- Local: 2.08 × 2.89 m (6.0 m²)
- Alto: 2.50 m
