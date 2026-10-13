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
    z0: float = 0.0,
    en_planta: bool = True,
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
        "z0": z0,
        "frente_hacia": frente_hacia,
        "ubicacion": ubicacion,
        "materiales": materiales,
        "texturas": texturas,
        "componentes": componentes,
        "notas": notas,
        "en_planta": en_planta,
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
        "alzado_principal": "S",
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
                z0=0.86,
            ),
            "ALACENA": _m(
                "ALACENA", "Alacenas superiores", "placard",
                3.69, 0.35, 0.70, 0.00, 0.00, 0.35, 3.69, "E",
                "Sobre mesada, arranque a 1.50 m, hasta 2.20 m. LED bajo alacena.",
                [_mat("Roble", "frentes", "roble"),
                 _mat("LED 3000K", "tira bajo mueble", "blanco")],
                "Puertas verticales, interior blanco, campana integrada en un tramo.",
                ["luz de trabajo", "campana encastrada"],
                z0=1.50,
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
        "ancho": 2.65,
        "ancho_norte": 2.08,
        "ancho_sur": 2.65,
        "ancho_norte_total": 2.20,
        "ancho_sur_total": 2.80,
        "largo_oeste": 2.80,
        "largo_oeste_total": 3.00,
        "y_escalon": 0.52,
        "largo": 2.80,
        "alto": 2.80,
        "superficie": 6.12,
        "descripcion": (
            "Local no rectangular: norte 2.08 m útiles (2.20 tot.), sur 2.65 m útiles "
            "(2.80 tot.), oeste 2.80 m útiles (3.00 tot.). Oeste: placard de secado + "
            "escobero. Norte: banitori, pileta, mesada de planchar y lavarropas. Este: "
            "abertura 1.60 m + mueble divisor 1.20 m. Sur: coffee station."
        ),
        "adjacencias": {
            "N": "Baño de servicio",
            "S": "Puerta de servicio / circulación",
            "E": "Cocina",
        },
        "puertas": [
            {"nombre": "Puerta de servicio", "muro": "S", "ancho": 0.80, "offset": 0.625, "alto": 2.10},
            {"nombre": "Paso a cocina", "muro": "E", "ancho": 1.60, "offset": 0.00, "alto": 2.80},
        ],
        "criterio": (
            "Sur más largo que norte (+0.57 m al este): coffee station junto a la puerta. "
            "Oeste: placard 1.50 + escobero 0.30 + paso + banitori/pileta en NW. "
            "Este sin muro de obra: abertura 1.60 m y mueble divisor 1.20 × 0.60 × 2.80 "
            "(cestos al lavadero, columna de cocción a cocina, baulera arriba)."
        ),
        "alzado_principal": "N",
        "muros_omitidos": ["E"],
        "muebles": {
            "PLACARD_SECADO": _m(
                "PLACARD_SECADO", "Placard de secado", "placard",
                1.50, 0.625, 2.80, 0.00, 0.00, 0.625, 1.50, "E",
                "Muro oeste, desde la puerta de servicio hacia el norte. Piso a techo.",
                [_mat("Roble / petiribí", "frente piso a techo, dos hojas de 0.75 m", "roble"),
                 _mat("Listones ventilados", "interior / trasdosado", "petiribi"),
                 _mat("Metal negro", "barra perchero y herrajes", "metal")],
                "Carpintería piso a techo. Interior ventilado para secado, barra a 1.80 m.",
                ["2 hojas 0.75 m", "barra perchero", "ventilación inferior y superior"],
                "Profundidad 0.625 m. Largo de frente 1.50 m.",
            ),
            "ESCOBERO": _m(
                "ESCOBERO", "Escobero", "placard",
                0.30, 0.625, 2.80, 0.00, 1.50, 0.625, 0.30, "E",
                "Muro oeste, inmediato al norte del placard de secado. Piso a techo.",
                [_mat("Roble", "frente", "roble"),
                 _mat("Grafito", "interior", "grafito")],
                "Módulo estrecho para escobas y trapeadores. Al norte queda un paso libre "
                "hasta el banitori / pileta del rincón NW.",
                ["piso a techo 2.80 m", "frente 30 cm", "fondo 62.5 cm"],
            ),
            "BANITORI": _m(
                "BANITORI", "Mueble banitori", "placard",
                0.51, 0.60, 0.85, 0.00, 2.20, 0.51, 0.60, "S",
                "Rincón NW, muro norte. Bajo de apoyo hasta 0.85 m (misma cota que la pileta).",
                [_mat("Roble", "frentes", "roble"),
                 _mat("Grafito", "interior", "grafito")],
                "Mueble bajo junto a la pileta. Visible en alzado norte y oeste.",
                ["alto 0.85 m", "fondo 60 cm", "frente 51 cm"],
            ),
            "PILETON": _m(
                "PILETON", "Pileta de lavar", "pileta",
                0.405, 0.50, 0.35, 0.00, 2.00, 0.50, 0.405, "E",
                "Muro oeste, rincón NW. Cuba de 0.50 m a 0.85 m de altura. Visible también "
                "desde el alzado norte.",
                [_mat("Acero inoxidable", "cuba", "metal"),
                 _mat("Grifería negra", "pico alto", "negro")],
                "Entre el escobero y el banitori queda un paso; la pileta cuelga / apoya "
                "en el tramo norte del oeste. Cota superior 0.85 m = mesada de planchar.",
                ["cuba 40×35×25", "cota superior 0.85 m"],
                z0=0.50,
            ),
            "LAVARROPAS": _m(
                "LAVARROPAS", "Lavarropas frontal", "appliance",
                0.60, 0.60, 0.85, 0.51, 2.20, 0.60, 0.60, "S",
                "Muro norte, bajo la mesada de planchar, al este del banitori.",
                [_mat("Acero blanco / grafito", "carcasa", "grafito"),
                 _mat("Vidrio", "visor", "vidrio")],
                "Equipo 60×60×85 cm. Carga frontal hacia el local.",
                ["carga frontal", "bajo mesada"],
            ),
            "MESADA_PLANCHAR": _m(
                "MESADA_PLANCHAR", "Mesada de planchado", "mesada",
                1.48, 0.60, 0.02, 0.51, 2.20, 1.48, 0.60, "S",
                "Muro norte. Tablero 1.48 × 0.60 m a la misma altura que el tope de pileta (0.85 m).",
                [_mat("Silestone / compacto blanco cálido", "tablero 20 mm", "silestone"),
                 _mat("Opcional paño de planchar", "protección térmica móvil", "lino")],
                "Cubre lavarropas y sigue hacia el este. Cota superior 0.85 m.",
                ["espesor 2 cm", "cota 0.85 m", "largo 1.48 m", "fondo 60 cm"],
                z0=0.85,
            ),
            "ALACENA": _m(
                "ALACENA", "Alacena limpieza y baño", "placard",
                2.08, 0.35, 1.10, 0.00, 2.45, 2.08, 0.35, "S",
                "Muro norte, todo el ancho útil (2.08 m). De 1.70 m a techo. Fondo 35 cm.",
                [_mat("Roble", "frentes", "roble"),
                 _mat("Grafito", "interior y estantes", "grafito"),
                 _mat("LED 3000K", "tira bajo alacena", "blanco")],
                "Productos de limpieza y baño. LED bajo mueble.",
                ["arranque 1.70 m", "alto 1.10 m", "fondo 35 cm", "ancho 2.08 m"],
                z0=1.70,
            ),
            "MUEBLE_DIVISOR": _m(
                "MUEBLE_DIVISOR", "Mueble divisor lavadero–cocina", "placard",
                1.20, 0.60, 2.80, 1.48, 1.60, 0.60, 1.20, "O",
                "Cierre este del tramo norte (sin muro de obra). 1.20 × 0.60 × 2.80 m. "
                "Inferior al lavadero (cestos), medio a cocina (columna de cocción), "
                "superior baulera.",
                [_mat("MDF laqueado grafito", "frente cocina", "grafito"),
                 _mat("Melamina roble", "frente lavadero e interiores", "roble")],
                "Tres bandas: 0–0.70 cestos al lavadero; 0.70–1.90 columna horno/micro "
                "a cocina + alacena ciega al lavadero; 1.90–2.80 baulera push-to-open.",
                ["cestos extraíbles 0–0.70", "columna cocción a cocina", "baulera 1.90–2.80"],
            ),
            "CAFE_BAJO": _m(
                "CAFE_BAJO", "Coffee station — bajo", "placard",
                1.225, 0.50, 0.88, 1.425, 0.00, 1.225, 0.50, "N",
                "Muro sur, al este de la puerta de servicio. Frente al local (norte).",
                [_mat("Roble", "frentes de cajones y puerta", "roble"),
                 _mat("Grafito", "interior", "grafito")],
                "Minibar 45 cm + cajones/puerta 77.5 cm. La hoja de la puerta se estaciona "
                "contra el costado oeste del mueble.",
                ["minibar 45 cm", "2 cajones", "zócalo 8 cm"],
            ),
            "CAFE_MESADA": _m(
                "CAFE_MESADA", "Coffee station — mesada", "mesada",
                1.225, 0.52, 0.02, 1.425, 0.00, 1.225, 0.52, "N",
                "Muro sur. Tablero a 0.90 m sobre el coffee station.",
                [_mat("Silestone / compacto blanco cálido", "tablero 20 mm", "silestone")],
                "Espresso + molinillo y pava. Sin toma de agua.",
                ["espesor 2 cm", "cota 90 cm", "largo 1.225 m"],
                z0=0.88,
            ),
            "CAFE_ALACENA": _m(
                "CAFE_ALACENA", "Coffee station — alacena", "placard",
                1.225, 0.32, 1.25, 1.425, 0.00, 1.225, 0.32, "N",
                "Muro sur, de 1.55 m a techo. Tazas, café y vajilla de desayuno.",
                [_mat("Roble", "frentes", "roble"),
                 _mat("Grafito", "interior", "grafito"),
                 _mat("LED 3000K", "tira bajo alacena", "blanco")],
                "Hueco 65 cm para la máquina. Dos puertas.",
                ["arranque 1.55 m", "alto 1.25 m", "fondo 32 cm"],
                z0=1.55,
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
                z0=1.00,
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
