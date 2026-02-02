from pymongo import MongoClient, errors

uri = "mongodb+srv://gaelverar_db_user:NoQ1HNz0HcHAT6Z5@clustertest.rhdsz6d.mongodb.net/?appName=ClusterTest"
HotelDB = None
def tryConnection(collection):
    global HotelDB
    if HotelDB is None:
        try:
            client = MongoClient(
                    uri, 
                    serverSelectionTimeoutMS=5000
                )
            HotelDB = client["Tenerife_Grand_Hotel"]
            ping = client.admin.command('ping')
        except (errors.ServerSelectionTimeoutError, errors.ConnectionFailure):
            return None
    return HotelDB[collection]

    

def conectRoomCollection():
    mydb = tryConnection("rooms")   
    return mydb if mydb is not None else None

def conectUsersCollection():
    mydb = tryConnection("users")   
    return mydb if mydb is not None else None
    

def conectBookingCollection():
    mydb = tryConnection("bookings")   
    return mydb if mydb is not None else None
    
