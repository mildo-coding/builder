"""Catálogo de espacios y muebles — Beruti 3336.

Fuente de verdad para LAYOUT.md, fichas de mueble, plantas y renders.
Coordenadas de planta: origen en el rincón interior SO, +X este, +Y norte.
Medidas en metros.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

Spec = dict[str, Any]


def _m(
    id: str,
    nombre: str,
    tipo: str,
    frente: float,
    profundidad: float,
    alto: float,
    x: float,
    y: float,
    w: float,
    d: float,
    frente_hacia: str,
    ubicacion: str,
    materiales: list[dict[str, str]],
    texturas: str,
    componentes: list[str],
    notas: str = "",
) -> Spec:
    return {
        "id": id,
        "nombre": nombre,
        "tipo": tipo,
        "frente": frente,
        "profundidad": profundidad,
        "alto": alto,
        "x": x,
        "y": y,
        "w": w,
        "d": d,
        "frente_hacia": frente_hacia,
        "ubicacion": ubicacion,
        "materiales": materiales,
        "texturas": texturas,
        "componentes": componentes,
        "notas": notas,
    }


def _mat(nombre: str, uso: str, clave: str) -> dict[str, str]:
    return {"nombre": nombre, "uso": uso, "clave": clave}


ESPACIOS: dict[str, Spec] = {
    "living_comedor": {
        "nombre": "Living Comedor",
        "slug": "living_comedor",
        "grupo": "A. Área social y exterior",
        "ancho": 5.50,
        "largo": 8.00,
        "alto": 2.50,
        "superficie": 44.0,
        "descripcion": (
            "Corazón del departamento. Espacio amplio y flexible que sectoriza "
            "estar/TV y comedor principal para 8-10 personas. Conexión directa "
            "con el balcón, luz natural y vistas al Río de la Plata."
        ),
        "adjacencias": {
            "N": "Balcón / terraza",
            "S": "Hall y acceso",
            "E": "Dormitorios / núcleo húmedo",
            "O": "Cocina / comedor diario",
        },
        "puertas": [
            {"nombre": "Salida a balcón", "muro": "N", "ancho": 1.80, "offset": 1.80},
            {"nombre": "Acceso desde hall", "muro": "S", "ancho": 0.90, "offset": 2.20},
        ],
        "criterio": (
            "Panelado de madera en la pared de TV, mueble bar a medida con LED "
            "indirecta, comedor cerca de la salida al balcón."
        ),
        "muebles": {
            "PANELADO_TV": _m(
                "PANELADO_TV", "Panelado TV / audio", "panel",
                3.20, 0.04, 2.50, 1.15, 0.00, 3.20, 0.04, "N",
                "Pared sur del living, eje de la zona de estar, frente al sofá.",
                [_mat("Roble de Eslavonia", "listones piso a techo", "roble"),
                 _mat("LED 2700K", "garganta superior e inferior", "blanco")],
                "Listonado vertical de 40 mm con juntas de sombra. TV empotrada al eje.",
                ["TV 65\" empotrada", "pasacables oculto", "LED indirecta"],
            ),
            "SOFA": _m(
                "SOFA", "Sofá de estar", "sofa",
                2.80, 1.00, 0.85, 1.35, 2.40, 2.80, 1.00, "S",
                "Zona de estar, centrado frente al panelado de TV, a 2.40 m de la pared sur.",
                [_mat("Lino cálido", "tapizado", "lino"),
                 _mat("Roble", "patas y zócalo", "roble")],
                "Tapizado textil mate, cojines de pluma, patas de madera baja.",
                ["3 cuerpos", "cojines de respaldo", "patas 12 cm"],
            ),
            "MESA_CENTRO": _m(
                "MESA_CENTRO", "Mesa de centro", "mesa",
                1.20, 0.70, 0.38, 2.15, 1.45, 1.20, 0.70, "S",
                "Entre el sofá y el panelado, eje de la zona de estar.",
                [_mat("Roble", "estructura y fuste", "roble"),
                 _mat("Silestone", "tapa", "silestone")],
                "Tapa de piedra de 20 mm sobre base de madera maciza.",
                ["tapa 1.20 × 0.70", "base en U"],
            ),
            "MUEBLE_BAR": _m(
                "MUEBLE_BAR", "Mueble bar / vajillero", "placard",
                1.80, 0.45, 1.20, 0.00, 3.60, 0.45, 1.80, "E",
                "Muro oeste, entre estar y comedor, a medida contra pared.",
                [_mat("Petiribí", "frente y costados", "petiribi"),
                 _mat("LED 2700K", "estante vidrio iluminado", "blanco"),
                 _mat("Grafito", "interior", "grafito")],
                "Frentes lisos con tirador integrado. Estante superior vidrio + LED.",
                ["botellero", "vajilla", "iluminación indirecta"],
            ),
            "MESA_COMEDOR": _m(
                "MESA_COMEDOR", "Mesa de comedor", "mesa",
                2.40, 1.10, 0.75, 1.55, 5.70, 2.40, 1.10, "N",
                "Sector norte del local, próxima a la salida al balcón.",
                [_mat("Roble de Eslavonia", "tablero 40 mm", "roble"),
                 _mat("Metal negro", "base", "metal")],
                "Tablero de madera maciza, canto vivo, base metálica en T.",
                ["8 puestos habituales", "extensible a 10"],
            ),
            "SILLAS_COMEDOR": _m(
                "SILLAS_COMEDOR", "Juego de sillas de comedor", "silla",
                0.50, 0.55, 0.80, 1.40, 5.50, 2.70, 1.50, "N",
                "Alrededor de la mesa de comedor (8 unidades, dos cabeceras).",
                [_mat("Roble", "estructura", "roble"),
                 _mat("Lino", "asiento y respaldo", "lino")],
                "Silla de madera con tapizado desmontable. Perfil liviano.",
                ["8 sillas", "asiento 45 cm"],
            ),
        },
    },
    "balcon": {
        "nombre": "Balcón / Terraza",
        "slug": "balcon",
        "grupo": "A. Área social y exterior",
        "ancho": 5.50,
        "largo": 2.01,
        "alto": 2.50,
        "superficie": 11.0,
        "descripcion": (
            "Expansión del living hacia el norte. Lounge exterior, deck y "
            "vegetación para disfrutar la vista panorámica del piso 23."
        ),
        "adjacencias": {"S": "Living comedor", "N": "Vista al Río de la Plata"},
        "puertas": [{"nombre": "Desde living", "muro": "S", "ancho": 1.80, "offset": 1.80}],
        "criterio": "Deck simil madera, lounge bajo, mesa baja y vegetación perimetral.",
        "muebles": {
            "DECK": _m(
                "DECK", "Deck / solado exterior", "panel",
                5.50, 2.01, 0.02, 0.00, 0.00, 5.50, 2.01, "N",
                "Solado completo del balcón, nivelado con umbral del living.",
                [_mat("Porcelanato símil madera", "piso", "porcelanato")],
                "Pieza 20×120, veta corrida hacia la vista, junta mínima.",
                ["pendiente 1%", "zocalo oculto"],
            ),
            "LOUNGE_EXTERIOR": _m(
                "LOUNGE_EXTERIOR", "Lounge exterior", "sofa",
                1.80, 0.80, 0.70, 0.35, 0.90, 1.80, 0.80, "N",
                "Lado oeste del balcón, orientado a la vista norte.",
                [_mat("Tejido outdoor", "tapizado", "lino"),
                 _mat("Aluminio negro", "estructura", "metal")],
                "Tapizado impermeable tono arena, estructura liviana.",
                ["2 cuerpos", "cojín de respaldo"],
            ),
            "MESA_BAJA": _m(
                "MESA_BAJA", "Mesa baja exterior", "mesa",
                1.00, 0.60, 0.35, 2.40, 1.05, 1.00, 0.60, "N",
                "Frente al lounge, eje de la terraza.",
                [_mat("Teak / petiribí tratado", "tablero", "petiribi"),
                 _mat("Metal negro", "patas", "metal")],
                "Madera tratada para exterior, canto romo.",
                ["altura lounge 35 cm"],
            ),
            "MACETEROS": _m(
                "MACETEROS", "Maceteros y vegetación", "maceta",
                0.40, 1.80, 0.50, 4.90, 0.10, 0.40, 1.80, "O",
                "Línea este del balcón, contra baranda / muro divisorio.",
                [_mat("Fibra negra", "maceta", "grafito"),
                 _mat("Sustrato y especies de sol", "plantas", "petiribi")],
                "Composición de gramíneas y arbustos bajos de poco viento.",
                ["3 macetas 40×60", "riego por goteo"],
            ),
        },
    },
    "dormitorio_principal": {
        "nombre": "Dormitorio Principal",
        "slug": "dormitorio_principal",
        "grupo": "B. Área privada",
        "ancho": 3.23,
        "largo": 5.05,
        "alto": 2.50,
        "superficie": 16.3,
        "descripcion": (
            "Suite con cama King, respaldo de madera integrado, mesas de noche "
            "flotantes y vestidor/placard. Conecta en suite con el baño principal."
        ),
        "adjacencias": {"E": "Baño en suite", "O": "Hall / placard", "S": "Oficina"},
        "puertas": [
            {"nombre": "Acceso", "muro": "O", "ancho": 0.80, "offset": 0.20},
            {"nombre": "Baño en suite", "muro": "E", "ancho": 0.70, "offset": 0.20},
        ],
        "criterio": "Cama al eje, respaldo-panel de madera con LED, vestidor en el tramo de circulación.",
        "muebles": {
            "CAMA_KING": _m(
                "CAMA_KING", "Cama King Size", "cama",
                2.00, 2.00, 0.45, 0.62, 1.40, 2.00, 2.00, "N",
                "Eje del dormitorio, cabecera contra el respaldo de madera (muro sur).",
                [_mat("Lino", "cabecera tapizada bajo el panel", "lino"),
                 _mat("Roble", "base", "roble")],
                "Base tapizada, colchón 200×200, ropa de cama tono arena.",
                ["colchón King 200×200", "base 45 cm"],
            ),
            "RESPALDO_MADERA": _m(
                "RESPALDO_MADERA", "Respaldo panelado", "panel",
                2.40, 0.08, 1.20, 0.42, 1.32, 2.40, 0.08, "N",
                "Muro de cabecera, integrando mesas de noche flotantes y LED.",
                [_mat("Roble", "panelado", "roble"),
                 _mat("LED 2700K", "garganta superior", "blanco")],
                "Panelado horizontal de 1.20 m de alto, continuo detrás de la cama.",
                ["LED indirecta", "encuentros con mesas flotantes"],
            ),
            "MESAS_NOCHE": _m(
                "MESAS_NOCHE", "Mesas de noche flotantes", "mesa",
                0.50, 0.35, 0.12, 0.42, 1.40, 0.50, 0.35, "N",
                "A ambos lados de la cama, voladas del respaldo a 0.55 m del piso.",
                [_mat("Roble", "cajón volado", "roble"),
                 _mat("Metal negro", "herraje invisible", "metal")],
                "Par de cajones flotantes, canto fino, sin patas.",
                ["2 unidades 50×35×12 cm", "toma USB oculta"],
                "La ficha representa una unidad; se colocan en espejo a izquierda y derecha.",
            ),
            "PLACARD_VESTIDOR": _m(
                "PLACARD_VESTIDOR", "Vestidor / placard", "placard",
                2.40, 0.60, 2.50, 0.00, 3.80, 3.23, 0.60, "S",
                "Tramo norte/circulación del dormitorio, frente continuo piso a techo.",
                [_mat("Roble", "frentes", "roble"),
                 _mat("Grafito", "interior", "grafito")],
                "Puertas piso a techo, interior con barra, cajonera y zapatero.",
                ["barra doble", "cajonera central", "LED interior"],
            ),
        },
    },
    "dormitorio_2": {
        "nombre": "Dormitorio 2",
        "slug": "dormitorio_2",
        "grupo": "B. Área privada",
        "ancho": 3.67,
        "largo": 4.09,
        "alto": 2.50,
        "superficie": 15.0,
        "descripcion": (
            "Dormitorio secundario amplio. Huéspedes, hijos o uso multipropósito. "
            "Cama Queen (o dos individuales) y frente de placard."
        ),
        "adjacencias": {"S": "Baño de visitas", "O": "Hall"},
        "puertas": [{"nombre": "Acceso", "muro": "O", "ancho": 0.80, "offset": 0.30}],
        "criterio": "Cama Queen al eje, placard en el muro más largo. Previsión de dos camas individuales.",
        "muebles": {
            "CAMA_QUEEN": _m(
                "CAMA_QUEEN", "Cama Queen", "cama",
                1.60, 2.00, 0.45, 1.03, 1.10, 1.60, 2.00, "N",
                "Eje del cuarto, cabecera contra muro sur.",
                [_mat("Lino", "respaldo tapizado", "lino"),
                 _mat("Roble", "patas", "roble")],
                "Cama 160×200, respaldo tapizado bajo. Alternativa: dos camas de 0.90.",
                ["colchón Queen", "opción 2×90 cm"],
            ),
            "MESA_NOCHE_2": _m(
                "MESA_NOCHE_2", "Mesa de noche", "mesa",
                0.45, 0.35, 0.50, 0.45, 1.10, 0.45, 0.35, "N",
                "Lado oeste de la cama, contra muro sur.",
                [_mat("Roble", "cajón y tapa", "roble")],
                "Mesa baja con un cajón y estante abierto.",
                ["1 cajón", "estante abierto"],
            ),
            "PLACARD": _m(
                "PLACARD", "Placard de frente continuo", "placard",
                2.80, 0.60, 2.50, 0.40, 3.49, 2.80, 0.60, "S",
                "Muro norte, frente piso a techo de 2.80 m.",
                [_mat("Roble", "frentes", "roble"),
                 _mat("Grafito", "interior", "grafito")],
                "Tres hojas, interior mixto barra + estantes.",
                ["3 módulos de 0.93 m", "LED interior"],
            ),
        },
    },
    "oficina": {
        "nombre": "Oficina / Estudio",
        "slug": "oficina",
        "grupo": "B. Área privada",
        "ancho": 3.10,
        "largo": 1.70,
        "alto": 2.50,
        "superficie": 5.3,
        "descripcion": (
            "Home office y lectura. Ventanal con luz natural. Biblioteca a medida, "
            "escritorio corrido y aislamiento acústico."
        ),
        "adjacencias": {"N": "Dormitorio principal", "S": "Fachada / ventanal"},
        "puertas": [{"nombre": "Acceso", "muro": "O", "ancho": 0.70, "offset": 0.20}],
        "criterio": "Escritorio bajo la ventana, biblioteca en el muro largo opuesto o continuo.",
        "muebles": {
            "ESCRITORIO": _m(
                "ESCRITORIO", "Escritorio corrido", "mesa",
                2.40, 0.60, 0.75, 0.35, 0.05, 2.40, 0.60, "S",
                "Bajo el ventanal, corrido 2.40 m, fondo 60 cm.",
                [_mat("Roble", "tablero 30 mm", "roble"),
                 _mat("Grafito", "cajonera pedestal", "grafito")],
                "Tablero continuo, cajonera de 3 cajones en un extremo, cableado oculto.",
                ["puesto de trabajo", "pasacables", "toma en mesada"],
            ),
            "BIBLIOTECA": _m(
                "BIBLIOTECA", "Biblioteca a medida", "estanteria",
                3.10, 0.32, 2.50, 0.00, 1.38, 3.10, 0.32, "S",
                "Muro norte, piso a techo, todo el ancho del local.",
                [_mat("Roble", "estantes y costados", "roble"),
                 _mat("Listones acústicos", "trasdosado", "petiribi")],
                "Estantes regulables, módulo cerrado inferior, listonado acústico de fondo.",
                ["estantes cada 32 cm", "módulo bajo con puertas"],
            ),
            "SILLA_ESCRITORIO": _m(
                "SILLA_ESCRITORIO", "Silla de trabajo", "silla",
                0.65, 0.65, 1.10, 1.20, 0.70, 0.65, 0.65, "S",
                "Frente al escritorio, zona central del puesto.",
                [_mat("Lino", "tapizado", "lino"),
                 _mat("Metal negro", "base giratoria", "metal")],
                "Silla ergonómica de perfil bajo, tapizado cálido, base negra.",
                ["altura regulable", "ruedas blandas"],
            ),
        },
    },
    "cocina": {
        "nombre": "Cocina Principal",
        "slug": "cocina",
        "grupo": "C. Área de servicios y cocina",
        "ancho": 2.00,
        "largo": 3.69,
        "alto": 2.50,
        "superficie": 7.4,
        "descripcion": (
            "Cocina longitudinal eficiente (pasillo útil ~1.23 m). Mesadas de "
            "Silestone, bajo y sobre mesada en madera cálida y grafito, equipamiento integrado."
        ),
        "adjacencias": {
            "N": "Comedor diario",
            "S": "Lavadero / hall de servicio",
            "E": "Living",
        },
        "puertas": [
            {"nombre": "A comedor diario", "muro": "N", "ancho": 0.80, "offset": 0.20},
            {"nombre": "A lavadero", "muro": "S", "ancho": 0.80, "offset": 0.20},
        ],
        "criterio": "Línea de trabajo en un solo frente: fregadero, anafe, torre de hornos. Alacenas superiores.",
        "muebles": {
            "BAJO_MESADA": _m(
                "BAJO_MESADA", "Bajo mesada", "placard",
                3.69, 0.60, 0.90, 0.00, 0.00, 0.60, 3.69, "E",
                "Muro oeste, corrido en todo el largo de la cocina.",
                [_mat("Roble", "frentes cajones", "roble"),
                 _mat("Grafito", "módulos de puertas", "grafito")],
                "Cajones de 80 cm en zona de trabajo, puertas en torre y rincón.",
                ["cajones soft-close", "módulo reciclado", "zócalo 10 cm"],
            ),
            "MESADA": _m(
                "MESADA", "Mesada Silestone", "mesada",
                3.69, 0.62, 0.04, 0.00, 0.00, 0.62, 3.69, "E",
                "Sobre el bajo mesada, canto de 20 mm, saliente 2 cm.",
                [_mat("Silestone Calacatta / blanco cálido", "tapa", "silestone")],
                "Encimera continua con pileta bajo mesada y anafe a ras.",
                ["espesor 20 mm", "antepecho 8 cm"],
            ),
            "ALACENA": _m(
                "ALACENA", "Alacenas superiores", "placard",
                3.69, 0.35, 0.70, 0.00, 0.00, 0.35, 3.69, "E",
                "Sobre mesada, arranque a 1.50 m, hasta 2.20 m. LED bajo alacena.",
                [_mat("Roble", "frentes", "roble"),
                 _mat("LED 3000K", "tira bajo mueble", "blanco")],
                "Puertas verticales, interior blanco, campana integrada en un tramo.",
                ["luz de trabajo", "campana encastrada"],
            ),
            "TORRE_HORNOS": _m(
                "TORRE_HORNOS", "Torre de hornos", "appliance",
                0.60, 0.60, 2.20, 0.00, 3.09, 0.60, 0.60, "E",
                "Extremo norte de la línea, junto al comedor diario.",
                [_mat("Acero negro / grafito", "frentes de electrodomésticos", "grafito"),
                 _mat("Roble", "costados", "roble")],
                "Horno + microondas/vaporera en columna, cajón inferior.",
                ["horno 60 cm", "microondas 60 cm", "cajón 60 cm"],
            ),
        },
    },
    "comedor_diario": {
        "nombre": "Comedor Diario",
        "slug": "comedor_diario",
        "grupo": "C. Área de servicios y cocina",
        "ancho": 2.08,
        "largo": 2.89,
        "alto": 2.50,
        "superficie": 6.0,
        "descripcion": (
            "Breakfast nook para comidas rápidas. Semintegrado con la cocina "
            "mediante barra de madera o cerramiento de vidrio y perfilería negra."
        ),
        "adjacencias": {"S": "Cocina", "E": "Living", "N": "Fachada / luz"},
        "puertas": [{"nombre": "Desde cocina", "muro": "S", "ancho": 0.90, "offset": 0.20}],
        "criterio": "Mesa compacta para 4 y barra de conexión visual con la cocina.",
        "muebles": {
            "MESA_DESAYUNADOR": _m(
                "MESA_DESAYUNADOR", "Mesa desayunador", "mesa",
                1.20, 0.80, 0.75, 0.44, 1.20, 1.20, 0.80, "N",
                "Centro del local, junto al ventanal.",
                [_mat("Roble", "tablero", "roble"),
                 _mat("Metal negro", "patas", "metal")],
                "Mesa cuadrada-rectangular para 4, canto vivo.",
                ["4 puestos"],
            ),
            "BANCOS": _m(
                "BANCOS", "Sillas / bancos del nook", "silla",
                0.45, 0.45, 0.78, 0.30, 1.05, 1.50, 1.10, "N",
                "Alrededor de la mesa desayunador.",
                [_mat("Roble", "estructura", "roble"),
                 _mat("Lino", "asiento", "lino")],
                "Cuatro sillas livianas, mismo lenguaje que el comedor principal.",
                ["4 unidades"],
            ),
            "BARRA": _m(
                "BARRA", "Barra de conexión con cocina", "mesada",
                1.60, 0.40, 1.10, 0.24, 0.00, 1.60, 0.40, "S",
                "Umbral hacia la cocina, pasaplatos / apoyo de 40 cm de fondo.",
                [_mat("Roble", "tablero 40 mm", "roble"),
                 _mat("Perfilería negra", "cerramiento opcional de vidrio", "metal")],
                "Barra de madera a 1.10 m. Opcional: paños de vidrio con perfil negro.",
                ["pasaplatos", "2 banquetas altas opcionales"],
            ),
        },
    },
    "lavadero": {
        "nombre": "Lavadero",
        "slug": "lavadero",
        "grupo": "C. Área de servicios y cocina",
        "ancho": 2.00,
        "largo": 2.81,
        "ancho_total": 2.625,
        "alto": 2.50,
        "superficie": 5.62,
        "descripcion": (
            "Local técnico extraído del plano original. Placard de secado ajustado "
            "a 1.50 × 0.625 m, con puerta piso a techo y cierre de tabique sólido. "
            "Incluye lavarropas, secarropas, piletón y guardado de limpieza."
        ),
        "adjacencias": {
            "N": "Baño de servicio",
            "S": "Puerta de servicio / circulación",
            "E": "Cocina",
        },
        "puertas": [
            {"nombre": "Puerta de servicio", "muro": "S", "ancho": 0.80, "offset": 0.625},
            {"nombre": "A cocina", "muro": "E", "ancho": 0.80, "offset": 0.20},
        ],
        "criterio": (
            "El placard arranca contra el muro junto a la puerta de servicio y "
            "termina con tabique sólido de 10 cm. El tramo norte original se libera "
            "como piso útil (pileta y circulación)."
        ),
        "plano_custom": True,
        "muebles": {
            "PLACARD_SECADO": _m(
                "PLACARD_SECADO", "Placard de secado", "placard",
                1.50, 0.625, 2.50, 0.00, 0.00, 0.625, 1.50, "E",
                "Muro oeste. Empieza contra la pared junto a la puerta de servicio "
                "y termina con tabique sólido de 10 cm. Frente al interior del lavadero.",
                [_mat("Roble / petiribí", "frente piso a techo, dos hojas de 0.75 m", "roble"),
                 _mat("Listones ventilados", "interior / trasdosado", "petiribi"),
                 _mat("Metal negro", "barra perchero y herrajes", "metal")],
                "Carpintería piso a techo (H = 2.50 m). Veta vertical. Interior ventilado "
                "para secado de ropa, con barra a 1.80 m y reja inferior.",
                ["2 hojas 0.75 m", "barra perchero", "ventilación inferior y superior",
                 "tabique de cierre 0.10 m"],
                "Profundidad 0.625 m (interior ~0.60 m para perchas). Largo de frente 1.50 m.",
            ),
            "LAVARROPAS": _m(
                "LAVARROPAS", "Lavarropas", "appliance",
                0.60, 0.60, 0.85, 2.025, 0.90, 0.60, 0.60, "O",
                "Muro este, tramo sur-centro, junto a la puerta a cocina. Carga frontal.",
                [_mat("Acero blanco / grafito", "carcasa", "grafito"),
                 _mat("Vidrio", "visor", "vidrio")],
                "Equipo de 8–9 kg, 60×60 cm, encastrable bajo mesada técnica opcional.",
                ["carga frontal", "desagüe y toma de agua en muro este"],
            ),
            "SECARROPAS": _m(
                "SECARROPAS", "Secarropas", "appliance",
                0.60, 0.60, 0.85, 2.025, 0.90, 0.60, 0.60, "O",
                "Apilado sobre el lavarropas (kit de torre) en el mismo hueco de 60×60.",
                [_mat("Acero blanco / grafito", "carcasa", "grafito")],
                "Torre lavarropas + secarropas para liberar piso. Evacuación de humedad al muro.",
                ["kit de apilado", "altura total torre ~1.70 m"],
                "En planta ocupa la misma huella que el lavarropas.",
            ),
            "PILETON": _m(
                "PILETON", "Piletón de lavar", "pileta",
                0.50, 0.40, 0.90, 0.00, 2.20, 0.50, 0.40, "E",
                "Rincón noroeste, en el piso útil ganado al recortar el placard original.",
                [_mat("Acero inoxidable", "cuba", "metal"),
                 _mat("Roble tratado", "mueble bajo pileta", "roble"),
                 _mat("Grifería negra", "pico alto", "negro")],
                "Cuba profunda sobre mueble de 90 cm. Grifería negra de pico alto para palanganas.",
                ["cuba 40×35×25", "mueble con estante de limpieza"],
            ),
            "MUEBLE_LIMPIEZA": _m(
                "MUEBLE_LIMPIEZA", "Mueble de limpieza", "placard",
                0.40, 0.35, 2.00, 2.225, 1.70, 0.40, 0.35, "O",
                "Muro este, al norte de la torre de lavado, para productos y palo de piso.",
                [_mat("Grafito", "frentes", "grafito"),
                 _mat("Roble", "interior", "roble")],
                "Módulo alto y estrecho, puerta de 40 cm, interior con ganchos y bandejas.",
                ["guarda escoba", "bandejas de químicos"],
            ),
        },
    },
    "bano_servicio": {
        "nombre": "Baño de Servicio",
        "slug": "bano_servicio",
        "grupo": "C. Área de servicios y cocina",
        "ancho": 1.30,
        "largo": 1.20,
        "alto": 2.50,
        "superficie": 1.6,
        "descripcion": (
            "Baño auxiliar. Se reacondiciona como toilette secundario compacto "
            "(alternativa: guardado técnico)."
        ),
        "adjacencias": {"S": "Lavadero", "E": "Cocina / comedor diario"},
        "puertas": [{"nombre": "Acceso", "muro": "N", "ancho": 0.60, "offset": 0.35}],
        "criterio": "Inodoro + lavatorio compacto. Revestimiento gran formato. Grifería negra.",
        "muebles": {
            "INODORO": _m(
                "INODORO", "Inodoro compacto", "sanitario",
                0.37, 0.65, 0.40, 0.10, 0.10, 0.37, 0.65, "N",
                "Muro sur, fondo del toilette.",
                [_mat("Loza blanca", "cuerpo", "blanco"),
                 _mat("Tapa madera", "asiento", "roble")],
                "Inodoro de salida horizontal, depósito dual, tapa de madera.",
                ["depósito dual 3/6 L"],
            ),
            "LAVATORIO": _m(
                "LAVATORIO", "Lavatorio compacto", "pileta",
                0.45, 0.32, 0.85, 0.80, 0.75, 0.45, 0.32, "O",
                "Muro este, junto a la puerta, para no interferir la apertura.",
                [_mat("Loza blanca", "bacha", "blanco"),
                 _mat("Roble tratado", "ménsula", "roble"),
                 _mat("Grifería negra", "monocomando", "negro")],
                "Bacha de apoyo 45 cm sobre ménsula de madera.",
                ["sifón visto negro", "espejo 40×60"],
            ),
        },
    },
    "bano_principal": {
        "nombre": "Baño Principal (en suite)",
        "slug": "bano_principal",
        "grupo": "D. Núcleo de baños",
        "ancho": 1.88,
        "largo": 1.49,
        "alto": 2.50,
        "superficie": 2.8,
        "descripcion": (
            "Baño completo de la suite. Revestimientos de gran formato, vanitory "
            "flotante de madera, mampara de vidrio templado y grifería negra/embutida."
        ),
        "adjacencias": {"O": "Dormitorio principal"},
        "puertas": [{"nombre": "Desde suite", "muro": "O", "ancho": 0.70, "offset": 0.20}],
        "criterio": "Ducha al fondo con mampara, vanitory flotante sobre el muro largo, inodoro lineal.",
        "muebles": {
            "VANITORY": _m(
                "VANITORY", "Vanitory flotante", "vanitory",
                1.00, 0.45, 0.40, 0.70, 0.00, 1.00, 0.45, "N",
                "Muro sur, volado a 0.20 m del piso, sobre revestimiento de gran formato.",
                [_mat("Roble tratado contra humedad", "cajón flotante", "roble"),
                 _mat("Loza / Silestone", "encimera y bacha", "silestone"),
                 _mat("Grifería negra embutida", "monocomando mural", "negro")],
                "Cajón único con frente integrado, bacha de apoyo, grifería mural negra.",
                ["volado 20 cm", "cajón soft-close", "LED bajo mueble"],
            ),
            "MAMPARA": _m(
                "MAMPARA", "Mampara de ducha", "vidrio",
                0.90, 0.08, 2.00, 0.00, 0.80, 0.08, 0.90, "E",
                "Cierre de la ducha en el extremo este, vidrio templado 8 mm.",
                [_mat("Vidrio templado", "hoja fija + abatible", "vidrio"),
                 _mat("Perfil negro mate", "herrajes", "metal")],
                "Hoja fija + batiente, perfil mínimo negro, sin umbral alto.",
                ["vidrio 8 mm", "herraje negro"],
            ),
            "INODORO": _m(
                "INODORO", "Inodoro", "sanitario",
                0.37, 0.68, 0.40, 1.40, 0.70, 0.37, 0.68, "S",
                "Muro norte, alineado con el vanitory en la circulación.",
                [_mat("Loza blanca", "cuerpo", "blanco"),
                 _mat("Tapa madera", "asiento", "roble")],
                "Línea suspendida o adosada de perfil compacto, depósito dual.",
                ["depósito dual"],
            ),
        },
    },
    "bano_visitas": {
        "nombre": "Baño de Visitas",
        "slug": "bano_visitas",
        "grupo": "D. Núcleo de baños",
        "ancho": 1.80,
        "largo": 1.45,
        "alto": 2.50,
        "superficie": 2.6,
        "descripcion": (
            "Baño de apoyo del dormitorio 2 y visitas. Vanitory con madera, "
            "espejo retroiluminado y duchero moderno."
        ),
        "adjacencias": {"N": "Dormitorio 2", "O": "Hall"},
        "puertas": [{"nombre": "Acceso", "muro": "O", "ancho": 0.70, "offset": 0.20}],
        "criterio": "Misma familia material que el baño principal, escala ligeramente menor.",
        "muebles": {
            "VANITORY": _m(
                "VANITORY", "Vanitory con madera", "vanitory",
                0.90, 0.45, 0.40, 0.70, 0.00, 0.90, 0.45, "N",
                "Muro sur, flotante, alineado con el espejo retroiluminado.",
                [_mat("Roble tratado", "mueble", "roble"),
                 _mat("Silestone", "tapa", "silestone"),
                 _mat("Grifería negra", "monocomando", "negro")],
                "Vanitory de un cajón, bacha integrada, mismo lenguaje que la suite.",
                ["cajón 90 cm", "sifón oculto"],
            ),
            "ESPEJO_RETROILUMINADO": _m(
                "ESPEJO_RETROILUMINADO", "Espejo retroiluminado", "espejo",
                0.90, 0.04, 0.90, 0.70, 0.00, 0.90, 0.04, "N",
                "Sobre el vanitory, centrado, LED perimetral 3000K.",
                [_mat("Espejo 4 mm", "luna", "vidrio"),
                 _mat("LED 3000K", "halo perimetral", "blanco")],
                "Luna rectangular con halo LED difuso, sin marco visto.",
                ["90 × 90 cm", "IP44"],
            ),
            "DUCHERO": _m(
                "DUCHERO", "Duchero moderno", "ducha",
                0.80, 0.80, 2.10, 0.00, 0.65, 0.80, 0.80, "E",
                "Rincón este, plato a ras de piso, columna negra.",
                [_mat("Grifería negra embutida", "columna y flor", "negro"),
                 _mat("Porcelanato gran formato", "piso y muros", "porcelanato")],
                "Flor de 250 mm + duchador de mano, desagüe lineal.",
                ["flor 25 cm", "desagüe lineal 70 cm"],
            ),
        },
    },
    "hall_distribucion": {
        "nombre": "Hall de Distribución",
        "slug": "hall_distribucion",
        "grupo": "D. Núcleo de baños",
        "ancho": 1.38,
        "largo": 2.30,
        "alto": 2.50,
        "superficie": 3.2,
        "descripcion": (
            "Transición limpia entre la recepción social y el área privada "
            "de dormitorios y baños."
        ),
        "adjacencias": {
            "O": "Living",
            "E": "Dormitorios",
            "N": "Baños",
        },
        "puertas": [
            {"nombre": "Desde living", "muro": "O", "ancho": 0.90, "offset": 0.20},
            {"nombre": "A dormitorio principal", "muro": "E", "ancho": 0.80, "offset": 0.20},
        ],
        "criterio": "Paredes limpias, panelado bajo o consola de apoyo, luz indirecta en cielorraso.",
        "muebles": {
            "CONSOLA": _m(
                "CONSOLA", "Consola de recibo", "mesa",
                1.00, 0.32, 0.80, 0.19, 1.40, 1.00, 0.32, "S",
                "Muro largo, apoyo para llaves, bandeja y punto de luz.",
                [_mat("Roble", "tablero y fuste", "roble"),
                 _mat("Metal negro", "herraje", "metal")],
                "Consola liviana de 32 cm de fondo para no estrechar la circulación.",
                ["cajón único", "bandeja"],
            ),
            "PANELADO_HALL": _m(
                "PANELADO_HALL", "Panelado de hall", "panel",
                2.30, 0.03, 1.20, 0.00, 0.00, 0.03, 2.30, "E",
                "Muro oeste o este, zócalo-panel de 1.20 m que unifica la transición.",
                [_mat("Roble", "listones", "roble"),
                 _mat("LED 2700K", "garganta de cielorraso", "blanco")],
                "Listonado horizontal de 1.20 m, continuo, con encuentro a puertas.",
                ["zócalo integrado", "luz de cornisamento"],
            ),
        },
    },
}


ORDEN_ESPACIOS = [
    "living_comedor",
    "balcon",
    "dormitorio_principal",
    "dormitorio_2",
    "oficina",
    "cocina",
    "comedor_diario",
    "lavadero",
    "bano_servicio",
    "bano_principal",
    "bano_visitas",
    "hall_distribucion",
]


def espacio(slug: str) -> Spec:
    if slug not in ESPACIOS:
        raise KeyError(f"Espacio desconocido: {slug}")
    data = deepcopy(ESPACIOS[slug])
    data["slug"] = slug
    return data


def mueble(slug: str, mueble_id: str) -> Spec:
    esp = espacio(slug)
    spec = deepcopy(esp["muebles"][mueble_id])
    spec["espacio_slug"] = slug
    spec["espacio_nombre"] = esp["nombre"]
    return spec


def ids_muebles(slug: str) -> list[str]:
    return list(ESPACIOS[slug]["muebles"].keys())
