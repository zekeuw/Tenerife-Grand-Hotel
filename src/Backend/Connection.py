from pymongo import MongoClient, errors
import urllib.parse 


username = urllib.parse.quote_plus("gaelverar_db_user") 
password = urllib.parse.quote_plus("NoQ1HNz0HcHAT6Z5")
host = "clustertest"
port = 27017

uri = "mongodb+srv://gaelverar_db_user:NoQ1HNz0HcHAT6Z5@clustertest.rhdsz6d.mongodb.net/?appName=ClusterTest"

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
    
