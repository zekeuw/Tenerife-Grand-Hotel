from pymongo import MongoClient
import urllib.parse 


username = urllib.parse.quote_plus("admin")  # O el usuario que definiste
password = urllib.parse.quote_plus("admin") # O la contraseña que definiste
host = "localhost"
port = 27017

uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"

myclient = MongoClient(uri) # Cambiar puerto dependiendo docker

mydb = myclient["Tenerife_Grand_Hotel"]

def contctRoomCollection():
    return mydb["rooms"]

def contctUsersCollection():
    return mydb["users"]

def contctBookingCollection():
    return mydb["bookings"]