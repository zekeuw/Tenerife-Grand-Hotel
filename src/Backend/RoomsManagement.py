# This file will control the rooms updates
from Connection import conectRoomCollection

def TakeAllRooms() -> list[dict]:
    room_collection = conectRoomCollection()
    return list(room_collection.find())

def TakeMostValuedRooms():
    room_collection = conectRoomCollection()
    

if __name__ == "__main__": TakeAllRooms()