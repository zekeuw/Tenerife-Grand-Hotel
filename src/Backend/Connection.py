from pymongo import MongoClient
import urllib.parse 


username = urllib.parse.quote_plus("admin") 
password = urllib.parse.quote_plus("admin")
host = "127.0.0.1"
port = 27017

uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"

myclient = MongoClient(uri) # Cambiar puerto dependiendo docker

mydb = myclient["Tenerife_Grand_Hotel"]

def conectRoomCollection():
    return mydb["rooms"]

def conectUsersCollection():
    return mydb["users"]

def conectBookingCollection():
    return mydb["bookings"]