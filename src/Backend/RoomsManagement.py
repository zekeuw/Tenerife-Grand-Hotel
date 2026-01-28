# This file will control the rooms updates
from .Connection import conectRoomCollection

ROOMS_TYPES = ["Presidential", "Luxury", "Privacy", "Apartment", "Regular"]

def TakeAllRooms() -> list[dict]:
    room_collection = conectRoomCollection()
    return list(room_collection.find())

def TakeMostValuedRooms()-> list[dict]:
    """This function will take the 2 best valued rooms and return them"""
    room_collection = conectRoomCollection()
    print("ROOM COLLECTION", room_collection)
    if room_collection is None: return None

    best_rooms = {}

    for room_type in ROOMS_TYPES:
        data = room_collection.find_one({}, {room_type: 1, "_id": 0})
        
        if not data or room_type not in data:
            continue
            
        type_content = data[room_type]
        
        reviews = type_content.get("reviews", {})
        
        scores_map = {}
        
        for review in reviews.values():
            r_id = review.get("id_room")
            mark = review.get("mark")
            
            if r_id and mark is not None:
                if r_id not in scores_map:
                    scores_map[r_id] = []
                scores_map[r_id].append(mark)
        
        def get_avg_score(room_id):
            marks = scores_map.get(room_id, [])
            return sum(marks) / len(marks) if marks else 0

        room_ids = [k for k in type_content.keys() if k not in ["reviews", "images"]]
        
        sorted_ids = sorted(room_ids, key=get_avg_score, reverse=True)
        
        top_2_ids = sorted_ids[:2]
        
        best_rooms[room_type] = []
        for rid in top_2_ids:
            room_data = type_content[rid]
            room_data["id"] = rid 
            room_data["avg_rating"] = get_avg_score(rid) 
            best_rooms[room_type].append(room_data)

    return best_rooms
        
def TakeRandomPhotoByRoomType(room_type):
    from random import randint
    room_collection = conectRoomCollection()
    return room_collection.find_one({}, {room_type: 1, "_id": 0})[room_type]["images"][randint(0,2)]
    

if __name__ == "__main__": TakeRandomPhotoByRoomType("Presidential")