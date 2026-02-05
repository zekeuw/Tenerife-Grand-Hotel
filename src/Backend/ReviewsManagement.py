import pymongo

from src.Backend.Utils.Exceptions import NotFoundError
from src.Backend.Connection import conectRoomCollection

def createReview(title: str, roomId:str, review:str,mark:int, userId:str, bookingStart:str):
    '''Creates a review :P'''
    rooms = conectRoomCollection()
    
    if not (1 <= mark <= 5):
        raise ValueError("La puntuación debe estar entre 1 y 5.")
        
    if not review:
        raise ValueError("El comentario no puede estar vacío.")


    new_review = {
        "title": title,
        "id_Client": userId,
        "id_room": roomId,  
        "mark": int(mark),
        "description": review,
        "bookingStartDate": bookingStart
    }

    result = rooms.update_one(
        {"_id": roomId},
        {"$push": {"reviews": new_review}}
    )

    if result.matched_count == 0:
        raise NotFoundError(f"No se encontró la habitación con ID: {roomId}")

def returnReview(userId:str, roomId:str, bookingStart:str):
    '''Returns a review based on the user, the room, and the start date'''
    rooms = conectRoomCollection()
    filter = {"_id": roomId}

    args = {
        "_id": 0, 
        "reviews": {
            "$elemMatch": {
                "id_Client": userId,
                "bookingStartDate": bookingStart
            }
        }
    }

    data = rooms.find_one(filter, args)

    if data and "reviews" in data and len(data["reviews"]) > 0:
        return data["reviews"][0]