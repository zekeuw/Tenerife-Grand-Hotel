# TIPOS DE HABITACIONES: Presidencial (La mas grande, no tener mas de 5, tiene garaje), Luxury (Cara pero pej sin garaje, no mas de 20), Privacy (Con garaje con acceso directo a la habitacion, 50), Apartamento (Con cocina), Regular (Solo cama y sala de estar)
# TIPOS DE CAMAS: King (Exclusiva para Presidencial y Luxury), Matrimonio, individual, sofa-cama, cuna



from pymongo import MongoClient
import urllib.parse 


username = urllib.parse.quote_plus("admin")  # O el usuario que definiste
password = urllib.parse.quote_plus("admin") # O la contraseña que definiste
host = "localhost"
port = 27017

uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"

myclient = MongoClient(uri) # Cambiar puerto dependiendo docker

mydb = myclient["Tenerife_Grand_Hotel"]

rooms = mydb["rooms"]
users = mydb["users"]
bookings = mydb["bookings"]

room_data = {
    "Presidential":{
        "P123":{ # Numero de habitacion es el id 
            "guests" : 2,
            "bed": ["King"],
            "content": ["Wifi", "TV"],
            "price": 100,
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
                        "when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic "
                        "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing",
            "reviews":{
                "score": 5,
                "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's",
                "date":"10/10/1010"
            }
        } 
    },
    "Luxury":{
        "L123":{ # Numero de habitacion es el id 
            "guests" : 2,
            "bed": ["Matrimonio"],
            "content": ["Wifi", "TV"],
            "price": 100,
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
                        "when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic "
                        "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing",
            "reviews":{
                "score": 5,
                "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's",
                "date":"10/10/1010"
            }
        } 
    },
    "Privacy":{
        "P123":{ # Numero de habitacion es el id 
            "guests" : 2,
            "bed": ["King"], # Si tiene varias camas se añaden aqui
            "content": ["Wifi", "TV", "Garage"],
            "price": 100,
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
                        "when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic "
                        "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing",
            "reviews":{
                "score": 5,
                "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's",
                "date":"10/10/1010"
            }
        } 
    },
    "Apartamento":{
        "A123":{ # Numero de habitacion es el id 
            "guests" : 2,
            "bed": ["Individual"],
            "content": ["Wifi", "TV"],
            "price": 100,
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
                        "when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic "
                        "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing",
            "reviews":{
                "score": 5,
                "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's",
                "date":"10/10/1010"
            }
        } 
    },
    "Regular":{
        "A123":{ # Numero de habitacion es el id 
            "guests" : 2,
            "bed": ["Individual"],
            "content": ["Wifi", "TV"],
            "price": 100,
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
                        "when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic "
                        "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing",
            "reviews":{
                "score": 5,
                "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's",
                "date":"10/10/1010"
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
x = rooms.insert_one(room_data)
x = users.insert_one(users_data)
x = bookings.insert_one(bookings_data)