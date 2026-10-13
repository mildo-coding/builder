# Lavadero

Carpeta de trabajo de Arqui para el espacio **Lavadero** (Beruti 3336, piso 23).

## Contenido
- `LAYOUT.md` — medidas del local, adyacencias y componentes
- `generar_plano.py` — planta + alzados
- `generar_renders.py` — vistas + axonométrica + fichas
- `generar_todo.py` — atajo al generador completo
- `FURNITURE_PLACARD_SECADO.md` + `FURNITURE_PLACARD_SECADO.py` — Placard de secado
- `FURNITURE_ESCOBERO.md` + `FURNITURE_ESCOBERO.py` — Escobero
- `FURNITURE_BANITORI.md` + `FURNITURE_BANITORI.py` — Mueble banitori
- `FURNITURE_PILETON.md` + `FURNITURE_PILETON.py` — Pileta de lavar
- `FURNITURE_LAVARROPAS.md` + `FURNITURE_LAVARROPAS.py` — Lavarropas frontal
- `FURNITURE_MESADA_PLANCHAR.md` + `FURNITURE_MESADA_PLANCHAR.py` — Mesada de planchado
- `FURNITURE_ALACENA.md` + `FURNITURE_ALACENA.py` — Alacena limpieza y baño
- `FURNITURE_MUEBLE_DIVISOR.md` + `FURNITURE_MUEBLE_DIVISOR.py` — Mueble divisor lavadero–cocina
- `FURNITURE_CAFE_BAJO.md` + `FURNITURE_CAFE_BAJO.py` — Coffee station — bajo
- `FURNITURE_CAFE_MESADA.md` + `FURNITURE_CAFE_MESADA.py` — Coffee station — mesada
- `FURNITURE_CAFE_ALACENA.md` + `FURNITURE_CAFE_ALACENA.py` — Coffee station — alacena

## Cómo generar (solo a pedido del usuario)

```bash
python3 generar_plano.py
python3 generar_renders.py
python3 generar_todo.py

# Un mueble
python3 FURNITURE_PLACARD_SECADO.py
python3 FURNITURE_ESCOBERO.py
python3 FURNITURE_BANITORI.py
python3 FURNITURE_PILETON.py
python3 FURNITURE_LAVARROPAS.py
python3 FURNITURE_MESADA_PLANCHAR.py
python3 FURNITURE_ALACENA.py
python3 FURNITURE_MUEBLE_DIVISOR.py
python3 FURNITURE_CAFE_BAJO.py
python3 FURNITURE_CAFE_MESADA.py
python3 FURNITURE_CAFE_ALACENA.py
```

## Medidas de referencia
- Norte 2.08 m útiles / 2.20 tot. · Sur 2.65 m útiles / 2.80 tot. · Oeste 2.80 m útiles / 3.00 tot.
- Alto: 2.80 m
- Vanos: puerta de servicio 0.80 m (sur) · paso a cocina 1.60 m (este)
