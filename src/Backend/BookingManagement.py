# Here is the logic of bookings
from src.Backend.Connection import conectBookingCollection
from src.Backend.RoomsManagement import conectRoomCollection
from src.Backend.Utils.Exceptions import NotFoundError

from datetime import datetime
import json

# booking dict example :
'''    {
        "RoomId": "P654",
        "IniDate":"2026-10-10",
        "FinDate":"2026-10-10",
        "UserName":"Pepito" 
    }'''

def DateAvailable(id_hab:str, StartDate:str, EndDate:str, ignore_id=False) -> bool:
    '''Checks if the date is available for the booking on those two new dates'''

    bookings = conectBookingCollection()

    query = {
        "RoomId": id_hab,
        "IniDate": {"$lte": EndDate},
        "FinDate": {"$gte": StartDate}
    }
    # surprisingly this works with strings, because alphabetical order and whatever
    # if the starting date of the existing booking is before the end date of the new one while its end date is after the new one's start it means they are overlaping (big brain move here)
    # btw now it checks for equal dates too, meaning that a booking can not start the same day another one ends (let's give room service some time aight?)

    if ignore_id: #for updating bookings we don't want the actual query we are updating to count for checking the date, so we add that the id of the booking is not the same as the one we are updating
        query["_id"] = {"$ne": ignore_id}

    data = bookings.find_one(query) #just searching for one is enough

    if data:
        return False
    return True

def createBooking(id_hab: str, StartDate:str, EndDate:str, UserName:str):
    '''Creates a booking, raising exceptions in cases theres someting wrong'''

    bookings = conectBookingCollection()
    rooms = conectRoomCollection()

    data = rooms.find_one({"_id": id_hab})

    if not data:
        raise NotFoundError("Habitacion no existente")
    
    try:
        datetime.strptime(StartDate, "%Y-%m-%d")
        datetime.strptime(EndDate, "%Y-%m-%d")
    except:
        raise ValueError("Fecha introducida no válida")
    
    if EndDate <= StartDate:
        raise ValueError("La fecha de de check-in no puede ser posterior o igual a la fecha de check-out")

    if DateAvailable(id_hab, StartDate, EndDate):
        booking = {"RoomId": id_hab, "IniDate": StartDate, "FinDate": EndDate, "UserName": UserName}
        bookings.insert_one(booking)
    else:
        raise ValueError("La habitacion ya está ocupada en las fechas introducidas")

def UpdateBooking(id_hab: str, StartDate:str, NewStart: str, NewEnd:str):
    '''Using a room's id and the start date to get the booking, it updates the booking'''
    # btw naturally you cannot change the user or the room, if they want to change the room then delete the entire booking and make a new one (since they could have diferent prices and all)

    bookings = conectBookingCollection()
    
    data = bookings.find_one({"RoomId": id_hab, "IniDate": StartDate})

    changes = {}


    if NewStart != None:
        changes["IniDate"] = NewStart
    else:
        NewStart = data["IniDate"]

    if NewEnd != None:
        changes["FinDate"] = NewEnd
    else:
        NewEnd = data["FinDate"]

    try:
        datetime.strptime(NewStart, "%Y-%m-%d")
        datetime.strptime(NewEnd, "%Y-%m-%d")
    except:
        raise ValueError("Fecha introducida no válida")
    
    if NewEnd <= NewStart:
        raise ValueError("La fecha de de check-in no puede ser posterior o igual a la fecha de check-out")

    if changes == {}:
        raise ValueError("Haga al menos un cambio")
    
    if DateAvailable(id_hab, NewStart, NewEnd, data["_id"]): #this is why we changed the newdates before, also we pass the id so that it doesnt check for the booking we are updating
        update = { '$set' : changes }
        bookings.update_one({"RoomId": id_hab, "IniDate": StartDate}, update)
    else:
        raise ValueError("La habitacion ya está ocupada en las fechas introducidas")

    
    
def DeleteBookings(id_hab:str, StartDate:str):
    '''Searches a booking from its room id and its starting dates and deletes it'''

    bookings = conectBookingCollection()

    data = bookings.find_one({"RoomId": id_hab, "IniDate": StartDate})

    if data:
        bookings.delete_one({"RoomId": id_hab, "IniDate": StartDate})
    
    else:
        raise NotFoundError("Reserva no encontrada") #this shouldn't happen but just in case...
    

def GetBookingsOfUser(userName:str) -> list:
    '''Returns all the bookings of a user, searching by the username'''

    bookings = conectBookingCollection()

    data = bookings.find({"UserName": userName})

    if not data:
        raise NotFoundError("No hay ninguna reserva")
    
    data = list(data)
    
    return data


def GetAvailableRooms(StartDate:str, EndDate:str):
    '''First searches for not available rooms and then searches for any room that is not (not) available'''

    bookings = conectBookingCollection()
    rooms = conectRoomCollection()

    query = {
        "IniDate": {"$lte": EndDate},
        "FinDate": {"$gte": StartDate}
    }

    data = bookings.find(query) #now searching for one is not enough :D

    data = list(data)
    ids = []
    for elemento in data:
        ids.append(elemento["RoomId"])

    query = {
        "_id" : {"$nin": ids}
    }

    data = rooms.find(query)

    return list(data)

def BookingSampleData():
    '''Crea un puñao de bookings para la base de datos'''
    with open("./src/Backend/SampleData/Bookings.json", "r") as f:
        BOOKINGS = json.load(f)

        for booking in BOOKINGS:

            try:
                createBooking(booking["RoomId"], booking["IniDate"], booking["FinDate"], booking["UserName"])

            except Exception as e:
                print(f"No se pudo insertar {booking}: {e}") #esta funcion es de debug asiq da un poco igual poner un print aqui


    