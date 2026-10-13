# Espacios — Beruti 3336

Carpetas de trabajo de **Arqui** (arquitecto de la refacción). Hay un directorio por local del programa de necesidades.

## Espacios

| Carpeta | Local | Superficie |
| --- | --- | --- |
| `living_comedor` | Living Comedor | 44.0 m² |
| `balcon` | Balcón / Terraza | 11.0 m² |
| `dormitorio_principal` | Dormitorio Principal | 16.3 m² |
| `dormitorio_2` | Dormitorio 2 | 15.0 m² |
| `oficina` | Oficina / Estudio | 5.3 m² |
| `cocina` | Cocina Principal | 7.4 m² |
| `comedor_diario` | Comedor Diario | 6.0 m² |
| `lavadero` | Lavadero | 6.1 m² |
| `bano_servicio` | Baño de Servicio | 1.6 m² |
| `bano_principal` | Baño Principal | 2.8 m² |
| `bano_visitas` | Baño de Visitas | 2.6 m² |
| `hall_distribucion` | Hall de Distribución | 3.2 m² |

Cada carpeta incluye:
1. `README.md` — contenido y comandos
2. `LAYOUT.md` — medidas y componentes
3. `FURNITURE_X.md` — ficha del mueble X
4. `FURNITURE_X.py` — generador de renders del mueble X
5. `generar_plano.py` / `generar_renders.py` / `generar_todo.py`

## Cómo generar (solo a pedido del usuario)

Arqui **no** corre estos comandos salvo instrucción explícita. El usuario elige cuándo renderizar.

Desde la raíz del proyecto o desde `espacios/`:

```bash
python3 espacios/generar_todo.py
python3 espacios/generar_todo.py lavadero
```

Planta (vista superior) y alzados (vista de frente) de un espacio:

```bash
python3 espacios/generar_vistas.py lavadero
python3 espacios/lavadero/generar_plano.py
```

Un espacio:

```bash
python3 espacios/lavadero/generar_todo.py
```

Un mueble:

```bash
python3 espacios/lavadero/FURNITURE_PLACARD_SECADO.py
```

## Librería compartida

`espacios/_comun/` concentra paleta, catálogo y motores de planta / ficha / axonométrica. Los generadores de cada espacio lo importan.

## Salidas

- Por espacio: `espacios/<slug>/planos/` y `espacios/<slug>/renders/`
- Copia de proyecto: `./planos/<slug>_planta.png` y `./renders/<slug>/`
