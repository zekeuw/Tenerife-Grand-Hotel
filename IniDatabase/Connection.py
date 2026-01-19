
from pymongo import MongoClient
import urllib.parse  # Importante para limpiar la contraseña

# --- 1. DATOS DE CONEXIÓN ---
# Estos deben coincidir con los que usaste al crear el contenedor Docker
username = urllib.parse.quote_plus("admin")  # O el usuario que definiste
password = urllib.parse.quote_plus("admin") # O la contraseña que definiste
host = "localhost"
port = 27017

# --- 2. CREAR LA URI CON AUTENTICACIÓN ---
# Generalmente la autenticación se guarda en la base de datos "admin"
uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"

myclient = MongoClient(uri) # Cambiar puerto dependiendo docker

mydb = myclient["Tenerife_Grand_Hotel"]



rooms = mydb["rooms"]
users = mydb["users"]
bookings = mydb["bookings"]
reviews = mydb["reviews"]

tablas = {"habitaciones": rooms, "usuarios": users, "reservas": bookings, "reseñas": reviews}

room_data = {
    "ID_room": "P123", # Numero de habitacion es el id 
    "guests" : 2,
    "bed": "King",
    "type": "Presidential",
    "content": ["Wifi", "TV"],
    "price": 100,
    "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
                   "when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic "
                   "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing"
}

users_data = {
    "username": "prueba",
    "password": "123456as",
    "name": "Alberto",
    "surname": "Rodriguez Afonso",
    "phone": "695288521",
    "birth": "10/10/2010"
}

bookings_data = {
    "ID_room": "654"

}

x = rooms.insert_one(room_data)
x = users.insert_one(users_data)
x = bookings.insert_one(bookings_data)