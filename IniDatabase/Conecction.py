# TIPOS DE HABITACIONES: Presidencial (La mas grande, no tener mas de 5, tiene garaje), Luxury (Cara pero pej sin garaje, no mas de 20), Privacy (Con garaje con acceso directo a la habitacion, 50), Apartamento (Con cocina), Regular (Solo cama y sala de estar)
# TIPOS DE CAMAS: King (Exclusiva para Presidencial y Luxury), Matrimonio, individual, sofa-cama, cuna



from pymongo import MongoClient
import urllib.parse 


username = urllib.parse.quote_plus("admin")  # O el usuario que definiste
password = urllib.parse.quote_plus("admin") # O la contraseña que definiste
host = "127.0.0.1"
port = 27017

uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"

myclient = MongoClient(uri) # Cambiar puerto dependiendo docker

mydb = myclient["Tenerife_Grand_Hotel"]

rooms = mydb["rooms"]


room_data = {
    "Presidential": {
        "PR_1": {
            "guests": 4,
            "bed": ["King", "King"],
            "content": ["Wifi", "TV'", "Garaje", "Jacuzzi", "Minibar Premium"],
            "price": 1200,
            "description": "La joya de la corona. Suite presidencial de 150m2 con doble cama King Size y acceso exclusivo. Decoración imperial y vistas panorámicas de 360 grados."
        },
        "PR_2": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV", "Garaje", "Sauna", "Terraza"],
            "price": 950,
            "description": "Exclusividad y confort absoluto. Incluye mayordomo 24h y acceso directo desde el garaje privado a la habitación. Acabados en mármol y oro."
        },
        "PR_3": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV", "Garaje", "Piscina Privada", "Barra libre"],
            "price": 1500,
            "description": "La Suite Real. Piscina climatizada dentro de la habitación, techo retráctil y garaje blindado. El máximo lujo disponible."
        },
        "PR_4": {
            "guests": 4,
            "bed": ["King", "King"],
            "content": ["Wifi", "TV", "Garaje", "Sala de Cine", "Piano"],
            "price": 1350,
            "description": "Suite para dignatarios. Cuenta con un piano de cola, sala de proyección insonorizada y dos dormitorios principales."
        },
        "PR_5": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV", "Garaje", "Helipuerto acceso", "Mayordomo"],
            "price": 2500,
            "description": "La cúspide del hotel. Acceso directo al helipuerto, cristales blindados y bodega privada con colección centenaria. Solo para VIPs."
        },
        "images": ["/media/img/Rooms/Presidential/Presidential1.jpg","/media/img/Rooms/Presidential/Presidential2.jpg","/media/img/Rooms/Presidential/Presidential3.jpg"]
        ,"reviews": {
            "rev_1": {
                "id_Client": "user_45",
                "id_room": "PR_1",
                "mark": 5,
                "description": "Inolvidable. Despertar con esa vista panorámica de 360 grados es algo que hay que vivir una vez en la vida."
            },
            "rev_2": {
                "id_Client": "user_12",
                "id_room": "PR_3",
                "mark": 5,
                "description": "La piscina dentro de la habitación es una locura. El techo retráctil funcionó perfecto para ver las estrellas desde el agua."
            },
            "rev_3": {
                "id_Client": "user_89",
                "id_room": "PR_5",
                "mark": 4,
                "description": "El servicio de mayordomo fue excelente, aunque el acceso al helipuerto tuvo un pequeño retraso por viento. La bodega es espectacular."
            },
            "rev_4": {
                "id_Client": "user_33",
                "id_room": "PR_2",
                "mark": 5,
                "description": "Privacidad absoluta. Subir del garaje directo a la habitación sin cruzarme con nadie era justo lo que necesitaba."
            },
            "rev_5": {
                "id_Client": "user_67",
                "id_room": "PR_4",
                "mark": 5,
                "description": "La sala de cine tiene una acústica de estudio profesional. Disfrutamos mucho del piano de cola."
            },
            "rev_6": {
                "id_Client": "user_21",
                "id_room": "PR_1",
                "mark": 5,
                "description": "La cama King doble es inmensa. Todo el mobiliario respira lujo imperial."
            },
            "rev_7": {
                "id_Client": "user_09",
                "id_room": "PR_3",
                "mark": 3,
                "description": "Mucho lujo, pero el sistema del techo tardó un poco en cerrarse cuando empezó a llover. Por este precio esperaba perfección."
            },
            "rev_8": {
                "id_Client": "user_99",
                "id_room": "PR_2",
                "mark": 5,
                "description": "La sauna privada es maravillosa después de un día de reuniones. Acabados de mármol impecables."
            },
            "rev_9": {
                "id_Client": "user_55",
                "id_room": "PR_4",
                "mark": 4,
                "description": "Ideal para viajes diplomáticos. Espacio de sobra para reuniones privadas en los salones."
            },
            "rev_10": {
                "id_Client": "user_77",
                "id_room": "PR_5",
                "mark": 5,
                "description": "Sin palabras. Los cristales blindados dan una sensación de seguridad total. La mejor experiencia VIP que he tenido."
            }
        }    
    },
    "Luxury": {
        "LX_1": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV", "Vistas al Mar", "Cafetera Nespresso"],
            "price": 450,
            "description": "Lujo moderno sin complicaciones. Amplia cama King Size con sábanas de seda egipcia. Situada en la planta más alta, pero sin plaza de garaje asignada."
        },
        "LX_2": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV", "Domótica", "Baño de diseño"],
            "price": 420,
            "description": "Habitación inteligente controlada por voz. Ideal para parejas que buscan una experiencia tecnológica de alto standing."
        },
        "LX_3": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV", "Jacuzzi", "Minibar Premium"],
            "price": 440,
            "description": "Experiencia de relax total. Incluye un jacuzzi hidromasaje integrado en la habitación y un minibar con selección de licores premium incluidos."
        },
        "LX_4": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Terraza Privada", "Hamaca"],
            "price": 400,
            "description": "Lujo al aire libre. Disfruta de una terraza exclusiva de 20m2 con hamacas y zona chill-out. Ideal para ver el atardecer con total privacidad."
        },
        "LX_5": {
            "guests": 3,
            "bed": ["Matrimonio", "Sofa-cama"],
            "content": ["Wifi", "TV", "Balcón amplio"],
            "price": 380,
            "description": "Espacio de lujo con acabados en madera noble. Perfecta iluminación natural y servicio de habitaciones gourmet disponible."
        },
        "LX_6": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV 55'", "Vistas Panorámicas", "Ducha de lluvia"],
            "price": 410,
            "description": "Despierta con la mejor vista de la ciudad. Ducha efecto lluvia y amenities de alta gama. Sin garaje."
        },
        "LX_7": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV 60'", "Smart Home", "Cava de vinos"],
            "price": 460,
            "description": "Habitación tecnológica con pequeña selección de vinos premium incluida. Iluminación ajustable por app."
        },
        "LX_8": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Jacuzzi en terraza"],
            "price": 390,
            "description": "Romance puro. Jacuzzi situado en la terraza privada (planta alta). Privacidad visual total."
        },
        "LX_9": {
            "guests": 3,
            "bed": ["King", "Sofa-cama"],
            "content": ["Wifi", "TV", "Desayuno en cama"],
            "price": 430,
            "description": "Espaciosa suite junior. Zona de lectura y servicio de desayuno premium incluido en la tarifa."
        },
        "LX_10": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV", "Arte original"],
            "price": 400,
            "description": "Decorada por artistas locales. Una experiencia visual única con mobiliario de diseño."
        },
        "LX_11": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Acceso Spa"],
            "price": 375,
            "description": "Incluye acceso directo al Spa del hotel (ascensor exclusivo). Ambiente relajante con aromaterapia."
        },
        "LX_12": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV 65'", "Consola videojuegos"],
            "price": 425,
            "description": "Gamers Luxury. Pantalla gigante, consola de última generación y sillones ergonómicos."
        },
        "LX_13": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV", "Chimenea eléctrica"],
            "price": 440,
            "description": "Acogedora y sofisticada. Chimenea moderna frente a la cama King Size para noches de invierno."
        },
        "LX_14": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV", "Gimnasio privado", "Suelo radiante"],
            "price": 480,
            "description": "Wellness Suite. Incluye cinta de correr, pesas y esterilla de yoga dentro de la habitación. Baño con sauna de vapor."
        },
        "LX_15": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Telescopio", "Techo de cristal"],
            "price": 450,
            "description": "Stargazing Room. Situada en la última planta con una sección de techo acristalado y un telescopio profesional."
        },
        "LX_16": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV", "Biblioteca", "Sillón lectura"],
            "price": 410,
            "description": "Para intelectuales. Paredes forradas de libros clásicos, silencio absoluto y cafetera de grano recién molido."
        },
        "LX_17": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV", "Sistema de sonido Bose"],
            "price": 440,
            "description": "Cinema Suite. Pantalla gigante y acústica de estudio. Incluye suscripciones a todas las plataformas de streaming."
        },
        "LX_18": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Decoración Zen", "Tatami"],
            "price": 390,
            "description": "Estilo japonés moderno. Cama baja tipo tatami, jardín zen en miniatura y té matcha de bienvenida."
        },
        "LX_19": {
            "guests": 2,
            "bed": ["King"],
            "content": ["Wifi", "TV", "Oficina ejecutiva", "Impresora"],
            "price": 420,
            "description": "Business Luxury. Escritorio de roble, silla Herman Miller e impresora láser. Ideal para CEOs en viaje de negocios."
        },
        "LX_20": {
            "guests": 3,
            "bed": ["King", "Sofa-cama"],
            "content": ["Wifi", "TV", "Terraza chill-out"],
            "price": 460,
            "description": "Terraza privada de 30m2 con sofás de exterior y música ambiental. Perfecta para tomar una copa al atardecer."
        },
        "images": ["/media/img/Rooms/Luxury/Luxury1.jpg","/media/img/Rooms/Luxury/Luxury2.jpg","/media/img/Rooms/Luxury/Luxury3.jpg"],
        "reviews": {
            "rev_1": {
                "id_Client": "user_101",
                "id_room": "LX_3",
                "mark": 5,
                "description": "El jacuzzi en la habitación estaba impecable y el minibar muy completo. Perfecto para una escapada romántica."
            },
            "rev_2": {
                "id_Client": "user_202",
                "id_room": "LX_12",
                "mark": 5,
                "description": "El paraíso de un gamer. La pantalla gigante y la consola de última generación hicieron que no quisiera salir de la habitación."
            },
            "rev_3": {
                "id_Client": "user_303",
                "id_room": "LX_6",
                "mark": 4,
                "description": "La ducha efecto lluvia es muy relajante, aunque eché de menos tener plaza de garaje incluida en esta tarifa."
            },
            "rev_4": {
                "id_Client": "user_404",
                "id_room": "LX_2",
                "mark": 3,
                "description": "La domótica es genial cuando funciona, pero a veces Alexa no entendía bien las órdenes para apagar las luces."
            },
            "rev_5": {
                "id_Client": "user_505",
                "id_room": "LX_15",
                "mark": 5,
                "description": "Ver las estrellas con el telescopio desde la cama fue mágico. El techo de cristal estaba limpísimo."
            },
            "rev_6": {
                "id_Client": "user_606",
                "id_room": "LX_4",
                "mark": 5,
                "description": "La terraza privada es enorme. Desayunar en la hamaca con esas vistas no tiene precio."
            },
            "rev_7": {
                "id_Client": "user_707",
                "id_room": "LX_19",
                "mark": 5,
                "description": "Pude trabajar perfectamente gracias a la silla ergonómica y la impresora. WiFi muy rápido y estable."
            },
            "rev_8": {
                "id_Client": "user_808",
                "id_room": "LX_14",
                "mark": 4,
                "description": "Tener gimnasio en la propia habitación es un lujo, aunque la cinta de correr hace un poco de ruido al correr rápido."
            },
            "rev_9": {
                "id_Client": "user_909",
                "id_room": "LX_1",
                "mark": 5,
                "description": "Las sábanas de seda egipcia son otro nivel de confort. Se nota la calidad en cada detalle."
            },
            "rev_10": {
                "id_Client": "user_110",
                "id_room": "LX_18",
                "mark": 5,
                "description": "Me encantó el estilo japonés. El tatami es sorprendentemente cómodo y el jardín zen relaja muchísimo."
            }
        }
    },
    "Privacy": {
        "PV1": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo", "Insonorización"],
            "price": 180,
            "description": "Diseñada para la discreción total. Aparca tu coche y sube directamente a tu habitación sin pasar por recepción. Muros totalmente insonorizados."
        },
        "PV2": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo", "Check-in automático"],
            "price": 190,
            "description": "Entrada autónoma y privacidad garantizada. Habitación acogedora con iluminación tenue y acceso inmediato desde el box privado."
        },
        "PV3": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo"],
            "price": 175,
            "description": "Confort y privacidad. El garaje conecta mediante una escalera privada. Ideal para estancias cortas y discretas."
        },
        "PV4": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo", "Servicio de habitaciones torno"],
            "price": 160,
            "description": "Servicio de habitaciones a través de torno para máxima privacidad. Nadie entra, nadie sale."
        },
        "PV5": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo", "Espejos techo"],
            "price": 170,
            "description": "Decoración atrevida con espejos y luces led. El coche queda guardado justo debajo de la habitación."
        },
        "PV6": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo", "Sillón tantra"],
            "price": 180,
            "description": "Habitación temática para parejas. Acceso discreto garantizado las 24 horas."
        },
        "PV_7": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo"],
            "price": 155,
            "description": "Estilo motel americano renovado. Funcional, limpia y con persiana automática en el garaje."
        },
        "PV_8": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo", "Minibar gratuito"],
            "price": 190,
            "description": "Pack bienvenida incluido. Aparca y relájate sin pasar por recepción."
        },
        "PV_9": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo"],
            "price": 150,
            "description": "La opción más rápida para paradas técnicas. Check-in y apertura de garaje vía móvil."
        },
        "PV_10": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo", "Bañera redonda"],
            "price": 195,
            "description": "Pequeño lujo privado. Bañera integrada en la habitación y persianas de seguridad total."
        },
        "PV_11": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo"],
            "price": 165,
            "description": "Habitación interior ultra silenciosa. El garaje cuenta con cargador para coche eléctrico."
        },
        "PV_12": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo", "Cargador Coche Eléctrico"],
            "price": 185,
            "description": "Eco-Privacy. Tu plaza de garaje privada incluye cargador rápido para vehículos eléctricos gratuito."
        },
        "PV_13": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo", "Luces LED RGB"],
            "price": 165,
            "description": "Ambiente personalizable. Controla el color de la iluminación de toda la habitación desde el móvil."
        },
        "PV_14": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo", "Pago en efectivo anónimo"],
            "price": 175,
            "description": "La máxima discreción. Sistema de gestión que permite entrada y salida sin registro digital visible."
        },
        "PV_15": {
            "guests": 2,
            "bed": ["Matrimonio"], 
            "content": ["Wifi", "TV", "Garaje acceso directo", "Jacuzzi"],
            "price": 210,
            "description": "Suite Privacy Premium. Jacuzzi para dos personas y cama redonda. Acceso directo desde el vehículo."
        },
        "PV_16": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo"],
            "price": 155,
            "description": "Estándar Privacy. Habitación funcional en planta baja, sin ventanas al exterior (solo tragaluz) para total intimidad."
        },
        "PV_17": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo", "Pasaplatos"],
            "price": 170,
            "description": "Servicio de comida sin contacto. Pide la cena y recíbela a través de un compartimento seguro en la puerta."
        },
        "PV_18": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo"],
            "price": 160,
            "description": "Minimalista y oscura. Cortinas Blackout totales para dormir de día sin que entre un rayo de luz."
        },
        "PV_19": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Garaje acceso directo", "Barra de baile"],
            "price": 180,
            "description": "Habitación lúdica. Espaciosa y con espejo de pared completa. Garaje amplio para SUVs."
        },
        "images": ["/media/img/Rooms/Privacy/Privacy1.jpg","/media/img/Rooms/Privacy/Privacy2.jpg","/media/img/Rooms/Privacy/Privacy3.jpg"]
        ,"reviews": {
            "rev_1": {
                "id_Client": "user_11",
                "id_room": "PV1",
                "mark": 5,
                "description": "Discreción total garantizada. La insonorización es perfecta, no se oye nada del exterior."
            },
            "rev_2": {
                "id_Client": "user_22",
                "id_room": "PV_12",
                "mark": 5,
                "description": "Pude cargar el coche eléctrico en mi propia plaza privada mientras descansaba. Muy práctico y moderno."
            },
            "rev_3": {
                "id_Client": "user_33",
                "id_room": "PV4",
                "mark": 4,
                "description": "El torno para el servicio de habitaciones es un gran invento, aunque la comida llegó un poco tibia."
            },
            "rev_4": {
                "id_Client": "user_44",
                "id_room": "PV_17",
                "mark": 5,
                "description": "El sistema de pasaplatos es genial, cero contacto con el personal. Limpieza de 10."
            },
            "rev_5": {
                "id_Client": "user_55",
                "id_room": "PV6",
                "mark": 5,
                "description": "Una habitación muy divertida para parejas. El sillón tantra y la iluminación crean un ambiente único."
            },
            "rev_6": {
                "id_Client": "user_66",
                "id_room": "PV_14",
                "mark": 5,
                "description": "El proceso de pago anónimo y entrada autónoma funcionó a la perfección. Nadie te molesta."
            },
            "rev_7": {
                "id_Client": "user_77",
                "id_room": "PV_10",
                "mark": 4,
                "description": "La bañera redonda es relajante, pero tardó bastante en llenarse. Por lo demás, privacidad excelente."
            },
            "rev_8": {
                "id_Client": "user_88",
                "id_room": "PV_13",
                "mark": 5,
                "description": "Controlar las luces LED desde el móvil le da un toque muy chulo. Puedes cambiar el ambiente en un segundo."
            },
            "rev_9": {
                "id_Client": "user_99",
                "id_room": "PV3",
                "mark": 3,
                "description": "Cumple su función para una estancia corta, pero la escalera desde el garaje es un poco estrecha."
            },
            "rev_10": {
                "id_Client": "user_00",
                "id_room": "PV_18",
                "mark": 5,
                "description": "Las cortinas blackout funcionan de maravilla. Dormí a mediodía como si fuera medianoche. Oscuridad total."
            }
        }
    },
    "Apartment": {
        "AP_1": {
            "guests": 5,
            "bed": ["Matrimonio", "Individual", "Sofa-cama"],
            "content": ["Wifi", "TV", "Cocina", "Lavadora", "Nevera grande"],
            "price": 250,
            "description": "Siéntete como en casa. Apartamento completo con cocina americana, ideal para familias. Espacio amplio para niños y mascotas."
        },
        "AP_2": {
            "guests": 3,
            "bed": ["Matrimonio", "Cuna"],
            "content": ["Wifi", "TV", "Cocina", "Microondas"],
            "price": 200,
            "description": "Apartamento funcional perfecto para parejas con un bebé. Incluye cuna gratuita y zona de preparación de alimentos."
        },
        "AP_3": {
            "guests": 4,
            "bed": ["Matrimonio", "Sofa-cama"],
            "content": ["Wifi", "TV", "Cocina", "Lavavajillas"],
            "price": 230,
            "description": "Ideal estancias largas. Cocina con todos los electrodomésticos y zona de comedor separada."
        },
        "AP_4": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Cocina", "Vistas ciudad"],
            "price": 210,
            "description": "Studio loft. Espacio diáfano con cocina integrada y grandes ventanales."
        },
        "AP_5": {
            "guests": 6,
            "bed": ["Matrimonio", "Individual", "Individual", "Sofa-cama"],
            "content": ["Wifi", "TV", "Cocina", "Dos baños"],
            "price": 320,
            "description": "El apartamento familiar definitivo. Dos baños completos para evitar colas por la mañana."
        },
        "AP_6": {
            "guests": 3,
            "bed": ["Individual", "Individual", "Sofa-cama"],
            "content": ["Wifi", "TV", "Cocina"],
            "price": 190,
            "description": "Apartamento para grupo de amigos. Económico, con nevera y fogones para cocinar algo rápido."
        },
        "AP_7": {
            "guests": 4,
            "bed": ["Matrimonio", "Cuna", "Sofa-cama"],
            "content": ["Wifi", "TV", "Cocina", "Trona"],
            "price": 240,
            "description": "Baby Friendly. Incluye cuna, trona y calienta biberones en la cocina."
        },
        "AP_8": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Cocina", "Horno"],
            "price": 260,
            "description": "Para los amantes de la cocina. Horno profesional y utensilios de chef incluidos."
        },
        "AP_9": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Cocina", "Vistas mar"],
            "price": 280,
            "description": "Apartamento de diseño. Cocina en isla central perfecta para cocinar mirando al mar."
        },
        "AP_10": {
            "guests": 4,
            "bed": ["Individual", "Individual", "Sofa-cama", "Sofa-cama"],
            "content": ["Wifi", "TV", "Cocina", "Consola juegos"],
            "price": 220,
            "description": "Apartamento 'Student'. Económico para grupos de amigos, muchas camas separadas y cocina resistente."
        },
        "AP_11": {
            "guests": 3,
            "bed": ["Matrimonio", "Individual"],
            "content": ["Wifi", "TV", "Cocina", "Adaptado silla ruedas"],
            "price": 240,
            "description": "Accesible. Baño y cocina adaptados para movilidad reducida, puertas anchas y sin escalones."
        },
        "AP_12": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Cocina", "Balcón"],
            "price": 200,
            "description": "Pequeño y coqueto. Kitchenette básica (fuego y nevera) para desayunos. Balcón a la calle principal."
        },
        "AP_13": {
            "guests": 5,
            "bed": ["Matrimonio", "Matrimonio", "Sofa-cama"],
            "content": ["Wifi", "TV", "Cocina", "Dos plantas"],
            "price": 350,
            "description": "Duplex. Zona de día abajo con cocina y salón, zona de noche arriba con dormitorios."
        },
        "AP_14": {
            "guests": 2,
            "bed": ["Sofa-cama"],
            "content": ["Wifi", "TV", "Cocina"],
            "price": 180,
            "description": "Micro-apartamento inteligente. Todo es plegable para maximizar el espacio durante el día."
        },
        "AP_15": {
            "guests": 4,
            "bed": ["Matrimonio", "Cuna", "Cuna"],
            "content": ["Wifi", "TV", "Cocina", "Parque juegos"],
            "price": 260,
            "description": "Especial Gemelos. Espacio amplio con dos cunas y protectores en todos los enchufes y esquinas."
        },
        "images": ["/media/img/Rooms/Apartments/Apartment1.jpg","/media/img/Rooms/Apartments/Apartment2.jpg","/media/img/Rooms/Apartments/Apartment2.jpg"]
        ,"reviews": {
            "rev_1": {
                "id_Client": "user_123",
                "id_room": "AP_1",
                "mark": 5,
                "description": "Ideal para familias numerosas. La nevera grande nos salvó la vida y los niños tenían espacio de sobra."
            },
            "rev_2": {
                "id_Client": "user_234",
                "id_room": "AP_8",
                "mark": 5,
                "description": "La cocina está equipadísima, el horno es profesional. Hicimos una cena estupenda sin echar nada en falta."
            },
            "rev_3": {
                "id_Client": "user_345",
                "id_room": "AP_15",
                "mark": 5,
                "description": "Perfecto para ir con bebés. Las cunas estaban preparadas y los protectores en los enchufes nos dieron mucha tranquilidad."
            },
            "rev_4": {
                "id_Client": "user_456",
                "id_room": "AP_5",
                "mark": 4,
                "description": "Tener dos baños fue clave siendo 6 personas. El sofá cama es aceptable, pero mejor para niños que para adultos."
            },
            "rev_5": {
                "id_Client": "user_567",
                "id_room": "AP_11",
                "mark": 5,
                "description": "Totalmente accesible. Mi madre va en silla de ruedas y pudo moverse por el baño y la cocina sin problemas."
            },
            "rev_6": {
                "id_Client": "user_678",
                "id_room": "AP_3",
                "mark": 5,
                "description": "El lavavajillas es un puntazo para estancias largas. Te sientes como en tu propia casa."
            },
            "rev_7": {
                "id_Client": "user_789",
                "id_room": "AP_9",
                "mark": 5,
                "description": "Cocinar en la isla mirando al mar es una experiencia increíble. Diseño muy moderno y luminoso."
            },
            "rev_8": {
                "id_Client": "user_890",
                "id_room": "AP_13",
                "mark": 4,
                "description": "El dúplex es precioso y separa bien la zona de dormir, aunque las escaleras pueden cansar si subes y bajas mucho."
            },
            "rev_9": {
                "id_Client": "user_901",
                "id_room": "AP_6",
                "mark": 3,
                "description": "Económico para compartir entre amigos, pero la cocina es algo justa si todos queremos cocinar a la vez."
            },
            "rev_10": {
                "id_Client": "user_012",
                "id_room": "AP_14",
                "mark": 5,
                "description": "Sorprendente cómo se aprovecha el espacio. Todo plegable y funcional. Muy ingenioso para una persona o pareja."
            }
        }
    },
    "Regular": {
        "RG_1": {
            "guests": 1,
            "bed": ["Individual"],
            "content": ["Wifi", "TV", "Escritorio"],
            "price": 60,
            "description": "Habitación estándar para viajeros de negocios. Funcional, limpia y cómoda. Solo cama y pequeña sala de estar."
        },
        "RG_2": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Aire Acondicionado"],
            "price": 85,
            "description": "Nuestra opción más económica para parejas. Todo lo necesario para descansar después de un día de turismo."
        },
        "RG_3": {
            "guests": 2,
            "bed": ["Individual", "Individual"],
            "content": ["Wifi", "TV"],
            "price": 80,
            "description": "Doble twin clásica. Dos camas separadas, ideal para amigos o compañeros de trabajo. Sencillez y buen precio."
        },
        "RG_4": {
            "guests": 1,
            "bed": ["Individual"],
            "content": ["Wifi", "TV", "Ventilador"],
            "price": 50,
            "description": "La opción low-cost. Pequeña, interior pero limpia. Solo cama y baño."
        },
        "RG_5": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Armario"],
            "price": 75,
            "description": "Estándar matrimonial. Sin lujos, perfecta para dormir y seguir viajando."
        },
        "RG_6": {
            "guests": 2,
            "bed": ["Individual", "Individual"],
            "content": ["Wifi", "TV", "Mesa trabajo"],
            "price": 70,
            "description": "Doble económica. Camas separadas y una mesa pequeña para trabajar con el portátil."
        },
        "RG_7": {
            "guests": 1,
            "bed": ["Individual"],
            "content": ["Wifi", "Radio"],
            "price": 45,
            "description": "Habitación individual minimalista. Perfecta para mochileros. No tiene TV, solo radio."
        },
        "RG_8": {
            "guests": 2,
            "bed": ["Sofa-cama"],
            "content": ["Wifi", "TV", "Sala de estar"],
            "price": 65,
            "description": "Convertible. Durante el día es una sala de estar, de noche despliegas el sofá-cama."
        },
        "RG_9": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Vistas patio"],
            "price": 80,
            "description": "Tranquilidad absoluta. Da a un patio interior lleno de plantas. Silenciosa y fresca."
        },
        "RG_10": {
            "guests": 1,
            "bed": ["Individual"],
            "content": ["Wifi", "TV", "Caja fuerte"],
            "price": 55,
            "description": "Individual Plus. Un poco más grande que la estándar, con espacio para dejar maletas grandes."
        },
        "RG_11": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Baño compartido"], # Opción muy barata
            "price": 40,
            "description": "Low Cost Extreme. Habitación privada con lavabo, pero el baño completo es compartido en el pasillo."
        },
        "RG_12": {
            "guests": 2,
            "bed": ["Individual", "Individual"],
            "content": ["Wifi", "TV"],
            "price": 65,
            "description": "Twin interior. Sin vistas, perfecta para dormir y ahorrar presupuesto."
        },
        "RG_13": {
            "guests": 1,
            "bed": ["Sofa-cama"],
            "content": ["Wifi", "Escritorio"],
            "price": 45,
            "description": "Estudio de trabajo. Básicamente una oficina donde puedes dormir si se hace tarde."
        },
        "RG_14": {
            "guests": 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV", "Ventana techo"],
            "price": 75,
            "description": "Ático abuhardillado. Techos bajos y ventana tipo velux. Muy acogedora aunque pequeña."
        },
        "RG_15": {
            "guests": 2,
            "bed": ["Individual", "Individual"],
            "content": ["Wifi", "TV"],
            "price": 68,
            "description": "Doble estándar cerca del ascensor. Precio reducido por posible ruido leve."
        },
        "RG_16": {
            "guests": 1,
            "bed": ["Individual"],
            "content": ["Wifi", "TV"],
            "price": 50,
            "description": "Individual básica. Cuenta con una pequeña nevera vacía para que guardes tus bebidas."
        },
        "images": ["/media/img/Rooms/Regular/Regular1.jpg","/media/img/Rooms/Regular/Regular2.jpg","/media/img/Rooms/Regular/Regular2.jpg"],
        "reviews": {
            "rev_1": {
                "id_Client": "user_150",
                "id_room": "RG_1",
                "mark": 4,
                "description": "Cumple perfectamente para un viaje de negocios. Limpia, funcional y el escritorio sirve para trabajar un rato."
            },
            "rev_2": {
                "id_Client": "user_250",
                "id_room": "RG_11",
                "mark": 2,
                "description": "El precio es imbatible, pero tener que salir al pasillo para usar el baño compartido es bastante incómodo por la noche."
            },
            "rev_3": {
                "id_Client": "user_350",
                "id_room": "RG_9",
                "mark": 5,
                "description": "Al dar al patio interior es súper silenciosa. No se oye ni un coche. Descanso garantizado."
            },
            "rev_4": {
                "id_Client": "user_450",
                "id_room": "RG_14",
                "mark": 4,
                "description": "Muy acogedora con el techo abuhardillado, aunque cuidado con la cabeza si eres muy alto."
            },
            "rev_5": {
                "id_Client": "user_550",
                "id_room": "RG_4",
                "mark": 3,
                "description": "Es pequeña y sin aire acondicionado (solo ventilador), pero por este precio no se puede pedir más. Estaba limpia."
            },
            "rev_6": {
                "id_Client": "user_650",
                "id_room": "RG_7",
                "mark": 4,
                "description": "No tiene TV, pero me vino bien para desconectar. La radio le da un toque vintage simpático."
            },
            "rev_7": {
                "id_Client": "user_750",
                "id_room": "RG_13",
                "mark": 5,
                "description": "Básicamente una oficina donde dormir. El escritorio es amplio y cómodo. Genial si vienes solo a trabajar."
            },
            "rev_8": {
                "id_Client": "user_850",
                "id_room": "RG_8",
                "mark": 4,
                "description": "Durante el día tienes un salón bastante majo. El sofá-cama es más cómodo de lo que esperaba."
            },
            "rev_9": {
                "id_Client": "user_950",
                "id_room": "RG_2",
                "mark": 5,
                "description": "La mejor opción calidad-precio para parejas. Tiene aire acondicionado y baño privado, no necesitamos más."
            },
            "rev_10": {
                "id_Client": "user_050",
                "id_room": "RG_16",
                "mark": 4,
                "description": "La neverita vacía es un detalle útil para guardar agua y yogures. Habitación sencilla pero correcta."
            }
        }
    }
    
}

users_data = {
    "user_1": {
        "username": "luis01",
        "password": "passLuis01",
        "name": "Luis",
        "surname": "Benitez",
        "phone": "604343958",
        "birth": "1982-12-06"
    },
    "user2": {
        "username": "luis02",
        "password": "passLuis02",
        "name": "Luis",
        "surname": "Diaz",
        "phone": "682773620",
        "birth": "1997-04-22"
    },
    "user3": {
        "username": "javier03",
        "password": "passJavier03",
        "name": "Javier",
        "surname": "Alvarez",
        "phone": "672603876",
        "birth": "1978-11-12"
    },
    "user4": {
        "username": "sofia04",
        "password": "passSofia04",
        "name": "Sofia",
        "surname": "Torres",
        "phone": "671186270",
        "birth": "1997-02-15"
    },
    "user5": {
        "username": "beatriz05",
        "password": "passBeatriz05",
        "name": "Beatriz",
        "surname": "Perez",
        "phone": "681811867",
        "birth": "1986-11-15"
    },
    "user6": {
        "username": "pedro06",
        "password": "passPedro06",
        "name": "Pedro",
        "surname": "Sanchez",
        "phone": "669634582",
        "birth": "1970-09-24"
    },
    "user7": {
        "username": "raquel07",
        "password": "passRaquel07",
        "name": "Raquel",
        "surname": "Lopez",
        "phone": "659987992",
        "birth": "1971-10-16"
    },
    "user8": {
        "username": "luis08",
        "password": "passLuis08",
        "name": "Luis",
        "surname": "Vazquez",
        "phone": "667155989",
        "birth": "1993-09-07"
    },
    "user9": {
        "username": "marta09",
        "password": "passMarta09",
        "name": "Marta",
        "surname": "Hernandez",
        "phone": "612882132",
        "birth": "1983-10-07"
    },
    "user10": {
        "username": "antonio10",
        "password": "passAntonio10",
        "name": "Antonio",
        "surname": "Romero",
        "phone": "666819601",
        "birth": "1970-04-24"
    },
    "user11": {
        "username": "antonio11",
        "password": "passAntonio11",
        "name": "Antonio",
        "surname": "Navarro",
        "phone": "675352282",
        "birth": "2000-06-11"
    },
    "user12": {
        "username": "francisco12",
        "password": "passFrancisco12",
        "name": "Francisco",
        "surname": "Rodriguez",
        "phone": "660458764",
        "birth": "1974-01-14"
    },
    "user13": {
        "username": "patricia13",
        "password": "passPatricia13",
        "name": "Patricia",
        "surname": "Fernandez",
        "phone": "698961378",
        "birth": "1970-03-30"
    },
    "user14": {
        "username": "david14",
        "password": "passDavid14",
        "name": "David",
        "surname": "Benitez",
        "phone": "628224984",
        "birth": "2005-12-16"
    },
    "user15": {
        "username": "lucia15",
        "password": "passLucia15",
        "name": "Lucia",
        "surname": "Perez",
        "phone": "627034271",
        "birth": "1992-10-13"
    },
    "user16": {
        "username": "antonio16",
        "password": "passAntonio16",
        "name": "Antonio",
        "surname": "Ramirez",
        "phone": "669715521",
        "birth": "1983-09-18"
    },
    "user17": {
        "username": "francisco17",
        "password": "passFrancisco17",
        "name": "Francisco",
        "surname": "Rodriguez",
        "phone": "678359243",
        "birth": "1993-01-25"
    },
    "user18": {
        "username": "antonio18",
        "password": "passAntonio18",
        "name": "Antonio",
        "surname": "Gomez",
        "phone": "685640027",
        "birth": "1974-12-27"
    },
    "user19": {
        "username": "manuel19",
        "password": "passManuel19",
        "name": "Manuel",
        "surname": "Navarro",
        "phone": "683587618",
        "birth": "1988-03-26"
    },
    "user20": {
        "username": "beatriz20",
        "password": "passBeatriz20",
        "name": "Beatriz",
        "surname": "Gomez",
        "phone": "693579070",
        "birth": "1982-11-15"
    },
    "user21": {
        "username": "juan21",
        "password": "passJuan21",
        "name": "Juan",
        "surname": "Martinez",
        "phone": "647893622",
        "birth": "1985-01-30"
    },
    "user22": {
        "username": "isabel22",
        "password": "passIsabel22",
        "name": "Isabel",
        "surname": "Navarro",
        "phone": "673254336",
        "birth": "1982-06-26"
    },
    "user23": {
        "username": "carlos23",
        "password": "passCarlos23",
        "name": "Carlos",
        "surname": "Muñoz",
        "phone": "690832202",
        "birth": "1975-06-17"
    },
    "user24": {
        "username": "carla24",
        "password": "passCarla24",
        "name": "Carla",
        "surname": "Alonso",
        "phone": "697204655",
        "birth": "2002-01-03"
    },
    "user25": {
        "username": "marta25",
        "password": "passMarta25",
        "name": "Marta",
        "surname": "Flores",
        "phone": "613123895",
        "birth": "1985-06-26"
    },
    "user26": {
        "username": "patricia26",
        "password": "passPatricia26",
        "name": "Patricia",
        "surname": "Benitez",
        "phone": "685589901",
        "birth": "2005-08-30"
    },
    "user27": {
        "username": "juan27",
        "password": "passJuan27",
        "name": "Juan",
        "surname": "Castillo",
        "phone": "664732851",
        "birth": "1992-03-22"
    },
    "user28": {
        "username": "sofia28",
        "password": "passSofia28",
        "name": "Sofia",
        "surname": "Perez",
        "phone": "676050113",
        "birth": "1999-04-11"
    },
    "user29": {
        "username": "isabel29",
        "password": "passIsabel29",
        "name": "Isabel",
        "surname": "Flores",
        "phone": "608927148",
        "birth": "2003-03-09"
    },
    "user30": {
        "username": "miguel30",
        "password": "passMiguel30",
        "name": "Miguel",
        "surname": "Torres",
        "phone": "647740718",
        "birth": "1982-12-21"
    },
    "user31": {
        "username": "ana31",
        "password": "passAna31",
        "name": "Ana",
        "surname": "Fernandez",
        "phone": "698838783",
        "birth": "1996-12-10"
    },
    "user32": {
        "username": "maria32",
        "password": "passMaria32",
        "name": "Maria",
        "surname": "Benitez",
        "phone": "618387763",
        "birth": "1999-09-06"
    },
    "user33": {
        "username": "patricia33",
        "password": "passPatricia33",
        "name": "Patricia",
        "surname": "Navarro",
        "phone": "697616617",
        "birth": "1991-10-27"
    },
    "user34": {
        "username": "laura34",
        "password": "passLaura34",
        "name": "Laura",
        "surname": "Hernandez",
        "phone": "601915812",
        "birth": "1980-01-20"
    },
    "user35": {
        "username": "jose35",
        "password": "passJose35",
        "name": "Jose",
        "surname": "Rodriguez",
        "phone": "646342039",
        "birth": "1989-01-01"
    },
    "user36": {
        "username": "raquel36",
        "password": "passRaquel36",
        "name": "Raquel",
        "surname": "Romero",
        "phone": "631532150",
        "birth": "1995-06-22"
    },
    "user37": {
        "username": "carmen37",
        "password": "passCarmen37",
        "name": "Carmen",
        "surname": "Diaz",
        "phone": "681186868",
        "birth": "1990-09-12"
    },
    "user38": {
        "username": "raquel38",
        "password": "passRaquel38",
        "name": "Raquel",
        "surname": "Diaz",
        "phone": "623307381",
        "birth": "1987-02-12"
    },
    "user39": {
        "username": "sofia39",
        "password": "passSofia39",
        "name": "Sofia",
        "surname": "Lopez",
        "phone": "628355294",
        "birth": "2003-02-13"
    },
    "user40": {
        "username": "luis40",
        "password": "passLuis40",
        "name": "Luis",
        "surname": "Alonso",
        "phone": "685155586",
        "birth": "1988-10-31"
    },
    "user41": {
        "username": "carla41",
        "password": "passCarla41",
        "name": "Carla",
        "surname": "Diaz",
        "phone": "602365048",
        "birth": "1978-01-27"
    },
    "user42": {
        "username": "manuel42",
        "password": "passManuel42",
        "name": "Manuel",
        "surname": "Romero",
        "phone": "640132793",
        "birth": "1973-02-12"
    },
    "user43": {
        "username": "laura43",
        "password": "passLaura43",
        "name": "Laura",
        "surname": "Castillo",
        "phone": "630885599",
        "birth": "1996-04-15"
    },
    "user44": {
        "username": "lucia44",
        "password": "passLucia44",
        "name": "Lucia",
        "surname": "Gomez",
        "phone": "600901570",
        "birth": "1998-10-17"
    },
    "user45": {
        "username": "maria45",
        "password": "passMaria45",
        "name": "Maria",
        "surname": "Lopez",
        "phone": "625676664",
        "birth": "1983-10-18"
    },
    "user46": {
        "username": "carla46",
        "password": "passCarla46",
        "name": "Carla",
        "surname": "Fernandez",
        "phone": "643209010",
        "birth": "1989-12-24"
    },
    "user47": {
        "username": "marta47",
        "password": "passMarta47",
        "name": "Marta",
        "surname": "Sanchez",
        "phone": "693862117",
        "birth": "1987-12-30"
    },
    "user48": {
        "username": "elena48",
        "password": "passElena48",
        "name": "Elena",
        "surname": "Alonso",
        "phone": "695561647",
        "birth": "1999-01-07"
    },
    "user49": {
        "username": "alejandro49",
        "password": "passAlejandro49",
        "name": "Alejandro",
        "surname": "Gutierrez",
        "phone": "668046933",
        "birth": "1992-09-25"
    },
    "user50": {
        "username": "paula50",
        "password": "passPaula50",
        "name": "Paula",
        "surname": "Ruiz",
        "phone": "610647468",
        "birth": "1996-07-28"
    },
    "user51": {
        "username": "paula51",
        "password": "passPaula51",
        "name": "Paula",
        "surname": "Sanchez",
        "phone": "684488680",
        "birth": "1975-04-23"
    },
    "user52": {
        "username": "carlos52",
        "password": "passCarlos52",
        "name": "Carlos",
        "surname": "Torres",
        "phone": "640025291",
        "birth": "1993-10-14"
    },
    "user53": {
        "username": "manuel53",
        "password": "passManuel53",
        "name": "Manuel",
        "surname": "Sanchez",
        "phone": "699430318",
        "birth": "1976-07-21"
    },
    "user54": {
        "username": "jose54",
        "password": "passJose54",
        "name": "Jose",
        "surname": "Fernandez",
        "phone": "650407569",
        "birth": "1980-09-03"
    },
    "user55": {
        "username": "miguel55",
        "password": "passMiguel55",
        "name": "Miguel",
        "surname": "Martinez",
        "phone": "639750985",
        "birth": "1988-10-18"
    },
    "user56": {
        "username": "lucia56",
        "password": "passLucia56",
        "name": "Lucia",
        "surname": "Sanchez",
        "phone": "654736584",
        "birth": "2002-09-12"
    },
    "user57": {
        "username": "juan57",
        "password": "passJuan57",
        "name": "Juan",
        "surname": "Gil",
        "phone": "601851886",
        "birth": "1971-12-09"
    },
    "user58": {
        "username": "ana58",
        "password": "passAna58",
        "name": "Ana",
        "surname": "Garcia",
        "phone": "661857916",
        "birth": "1985-06-21"
    },
    "user59": {
        "username": "paula59",
        "password": "passPaula59",
        "name": "Paula",
        "surname": "Ramirez",
        "phone": "633030991",
        "birth": "2000-04-15"
    },
    "user60": {
        "username": "maria60",
        "password": "passMaria60",
        "name": "Maria",
        "surname": "Benitez",
        "phone": "639340989",
        "birth": "1981-11-21"
    },
    "user61": {
        "username": "carla61",
        "password": "passCarla61",
        "name": "Carla",
        "surname": "Martinez",
        "phone": "657093043",
        "birth": "1970-03-02"
    },
    "user62": {
        "username": "laura62",
        "password": "passLaura62",
        "name": "Laura",
        "surname": "Muñoz",
        "phone": "630555351",
        "birth": "1971-05-18"
    },
    "user63": {
        "username": "alejandro63",
        "password": "passAlejandro63",
        "name": "Alejandro",
        "surname": "Benitez",
        "phone": "604676804",
        "birth": "1995-09-26"
    },
    "user64": {
        "username": "carla64",
        "password": "passCarla64",
        "name": "Carla",
        "surname": "Flores",
        "phone": "675066763",
        "birth": "1996-07-10"
    },
    "user65": {
        "username": "luis65",
        "password": "passLuis65",
        "name": "Luis",
        "surname": "Diaz",
        "phone": "655438173",
        "birth": "1974-07-15"
    },
    "user66": {
        "username": "paula66",
        "password": "passPaula66",
        "name": "Paula",
        "surname": "Ruiz",
        "phone": "635018336",
        "birth": "1987-02-21"
    },
    "user67": {
        "username": "alejandro67",
        "password": "passAlejandro67",
        "name": "Alejandro",
        "surname": "Alonso",
        "phone": "629616083",
        "birth": "1982-12-13"
    },
    "user68": {
        "username": "elena68",
        "password": "passElena68",
        "name": "Elena",
        "surname": "Gomez",
        "phone": "602541133",
        "birth": "2002-06-19"
    },
    "user69": {
        "username": "carla69",
        "password": "passCarla69",
        "name": "Carla",
        "surname": "Alonso",
        "phone": "617542363",
        "birth": "2002-12-02"
    },
    "user70": {
        "username": "francisco70",
        "password": "passFrancisco70",
        "name": "Francisco",
        "surname": "Castillo",
        "phone": "631239085",
        "birth": "1983-10-31"
    },
    "user71": {
        "username": "paula71",
        "password": "passPaula71",
        "name": "Paula",
        "surname": "Garcia",
        "phone": "637942809",
        "birth": "1970-03-03"
    },
    "user72": {
        "username": "beatriz72",
        "password": "passBeatriz72",
        "name": "Beatriz",
        "surname": "Martinez",
        "phone": "625884625",
        "birth": "2002-01-16"
    },
    "user73": {
        "username": "paula73",
        "password": "passPaula73",
        "name": "Paula",
        "surname": "Torres",
        "phone": "636174815",
        "birth": "2004-06-08"
    },
    "user74": {
        "username": "raquel74",
        "password": "passRaquel74",
        "name": "Raquel",
        "surname": "Castillo",
        "phone": "635802459",
        "birth": "1979-07-27"
    },
    "user75": {
        "username": "antonio75",
        "password": "passAntonio75",
        "name": "Antonio",
        "surname": "Vazquez",
        "phone": "618396336",
        "birth": "1984-04-24"
    },
    "user76": {
        "username": "pablo76",
        "password": "passPablo76",
        "name": "Pablo",
        "surname": "Gutierrez",
        "phone": "645207307",
        "birth": "1971-06-17"
    },
    "user77": {
        "username": "luis77",
        "password": "passLuis77",
        "name": "Luis",
        "surname": "Flores",
        "phone": "608606909",
        "birth": "2002-05-19"
    },
    "user78": {
        "username": "elena78",
        "password": "passElena78",
        "name": "Elena",
        "surname": "Benitez",
        "phone": "644827366",
        "birth": "1978-09-28"
    },
    "user79": {
        "username": "pablo79",
        "password": "passPablo79",
        "name": "Pablo",
        "surname": "Alvarez",
        "phone": "616212778",
        "birth": "1970-04-28"
    },
    "user80": {
        "username": "maria80",
        "password": "passMaria80",
        "name": "Maria",
        "surname": "Torres",
        "phone": "619139147",
        "birth": "1995-09-10"
    },
    "user81": {
        "username": "carmen81",
        "password": "passCarmen81",
        "name": "Carmen",
        "surname": "Castillo",
        "phone": "601336313",
        "birth": "1981-05-04"
    },
    "user82": {
        "username": "carlos82",
        "password": "passCarlos82",
        "name": "Carlos",
        "surname": "Garcia",
        "phone": "609107621",
        "birth": "1982-02-28"
    },
    "user83": {
        "username": "maria83",
        "password": "passMaria83",
        "name": "Maria",
        "surname": "Castillo",
        "phone": "683211442",
        "birth": "1989-01-29"
    },
    "user84": {
        "username": "carla84",
        "password": "passCarla84",
        "name": "Carla",
        "surname": "Alvarez",
        "phone": "676994918",
        "birth": "1987-10-15"
    },
    "user85": {
        "username": "lucia85",
        "password": "passLucia85",
        "name": "Lucia",
        "surname": "Castillo",
        "phone": "628274569",
        "birth": "1974-12-26"
    },
    "user86": {
        "username": "maria86",
        "password": "passMaria86",
        "name": "Maria",
        "surname": "Navarro",
        "phone": "606916456",
        "birth": "2002-05-14"
    },
    "user87": {
        "username": "beatriz87",
        "password": "passBeatriz87",
        "name": "Beatriz",
        "surname": "Sanchez",
        "phone": "616159292",
        "birth": "2003-01-10"
    },
    "user88": {
        "username": "lucia88",
        "password": "passLucia88",
        "name": "Lucia",
        "surname": "Diaz",
        "phone": "656728559",
        "birth": "2003-02-28"
    },
    "user89": {
        "username": "manuel89",
        "password": "passManuel89",
        "name": "Manuel",
        "surname": "Benitez",
        "phone": "644138518",
        "birth": "1979-12-09"
    },
    "user90": {
        "username": "marta90",
        "password": "passMarta90",
        "name": "Marta",
        "surname": "Torres",
        "phone": "685165835",
        "birth": "1973-12-27"
    },
    "user91": {
        "username": "elena91",
        "password": "passElena91",
        "name": "Elena",
        "surname": "Perez",
        "phone": "653598271",
        "birth": "1977-11-04"
    },
    "user92": {
        "username": "laura92",
        "password": "passLaura92",
        "name": "Laura",
        "surname": "Gutierrez",
        "phone": "601993880",
        "birth": "2000-02-14"
    },
    "user93": {
        "username": "jose93",
        "password": "passJose93",
        "name": "Jose",
        "surname": "Torres",
        "phone": "696656237",
        "birth": "2004-06-10"
    },
    "user94": {
        "username": "carlos94",
        "password": "passCarlos94",
        "name": "Carlos",
        "surname": "Ramirez",
        "phone": "666478049",
        "birth": "1971-04-04"
    },
    "user95": {
        "username": "lucia95",
        "password": "passLucia95",
        "name": "Lucia",
        "surname": "Perez",
        "phone": "600449052",
        "birth": "1974-01-14"
    },
    "user96": {
        "username": "diego96",
        "password": "passDiego96",
        "name": "Diego",
        "surname": "Ramirez",
        "phone": "680642186",
        "birth": "1985-06-08"
    },
    "user97": {
        "username": "isabel97",
        "password": "passIsabel97",
        "name": "Isabel",
        "surname": "Hernandez",
        "phone": "673452015",
        "birth": "1999-05-08"
    },
    "user98": {
        "username": "carla98",
        "password": "passCarla98",
        "name": "Carla",
        "surname": "Gomez",
        "phone": "670698794",
        "birth": "1984-02-04"
    },
    "user99": {
        "username": "elena99",
        "password": "passElena99",
        "name": "Elena",
        "surname": "Perez",
        "phone": "630582412",
        "birth": "1988-10-02"
    },
    "user100": {
        "username": "luis100",
        "password": "passLuis100",
        "name": "Luis",
        "surname": "Lopez",
        "phone": "673954583",
        "birth": "2000-09-12"
    }
}


bookings_data = {
    "P654":{
        "IniDate":"10/10/2026",
        "FinDate":"10/10/2026",
        "UserId":"123" 
    }

}

result = rooms.insert_one(room_data)
print(result)