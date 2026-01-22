# TIPOS DE HABITACIONES: Presidencial (La mas grande, no tener mas de 5, tiene garaje), Luxury (Cara pero pej sin garaje, no mas de 20), Privacy (Con garaje con acceso directo a la habitacion, 50), Apartamento (Con cocina), Regular (Solo cama y sala de estar)
# TIPOS DE CAMAS: King (Exclusiva para Presidencial y Luxury), Matrimonio, individual, sofa-cama, cuna



from pymongo import MongoClient
import urllib.parse 


username = urllib.parse.quote_plus("admin")  # O el usuario que definiste
password = urllib.parse.quote_plus("admin") # O la contraseña que definiste
host = "10.102.8.228"
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
        "images": ["/media/img/Presidential/Presidential1.jpg","/media/img/Presidential/Presidential2.jpg","/media/img/Presidential/Presidential3.jpg"]
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
        "images": ["/media/img/Luxury/Luxury1.jpg","/media/img/Luxury/Luxury2.jpg","/media/img/Luxury/Luxury3.jpg"]
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
        "images": ["/media/img/Privacy/Privacy1.jpg","/media/img/Privacy/Privacy2.jpg","/media/img/Apartamento/Privacy3.jpg"]
    },
    "Apartamento": {
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
        "images": ["/media/img/Apartamento/Apartamento1.jpg","/media/img/Apartamento/Apartamento2.jpg","/media/img/Apartamento/Apartamento2.jpg"]
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
        "images": ["/media/img/Regular/Regular1.jpg","/media/img/Regular/Regular2.jpg","/media/img/Regular/Regular2.jpg"],
        "reviews":{
            "0":{
                "user_id":1,
                "mark":5,
                "description":"esto es una prueba de una reseña",
                "room":"RG1"
            }
        }
    }
}


users_data = {
    "123":{ # ID Autoincremental
        "username": "prueba",
        "password": "123456as",
        "name": "Alberto",
        "surname": "Rodriguez Afonso",
        "phone": "695288521",
        "birth": "10/10/2010"
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