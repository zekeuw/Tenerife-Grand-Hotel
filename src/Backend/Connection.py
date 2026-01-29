from pymongo import MongoClient, errors
import urllib.parse 


username = urllib.parse.quote_plus("admin") 
password = urllib.parse.quote_plus("admin")
host = "127.0.0.1"
port = 27017

uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"

def tryConnection(collection):
    try:
        client = MongoClient(
                uri, 
                serverSelectionTimeoutMS=5000
            )
        mydb = client["Tenerife_Grand_Hotel"]
        ping = client.admin.command('ping')
        return mydb[collection]
    except (errors.ServerSelectionTimeoutError, errors.ConnectionFailure):
        return None

def conectRoomCollection():
    mydb = tryConnection("rooms")   
    return mydb if mydb is not None else None

def conectUsersCollection():
    mydb = tryConnection("users")   
    return mydb if mydb is not None else None
    

def conectBookingCollection():
    mydb = tryConnection("bookings")   
    return mydb if mydb is not None else None
    