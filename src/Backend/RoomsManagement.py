# This file will control the rooms updates
from .Connection import conectRoomCollection
from random import randint

ROOMS_TYPES = ["Presidential", "Luxury", "Privacy", "Apartment", "Regular"]




def TakeAllRooms() -> list[dict]:
    room_collection = conectRoomCollection()
    if room_collection is None: return []
    
    cursor = room_collection.find({})
    rooms = []
    for room in cursor:
        room['id'] = room['_id']
        rooms.append(room)
    return rooms

def TakeMostValuedRooms() -> dict:
    room_collection = conectRoomCollection()
    if room_collection is None: return None

    best_rooms = {}

    for room_type in ROOMS_TYPES:
        rooms_cursor = room_collection.find({"category": room_type})
        
        scored_rooms = []

        for room in rooms_cursor:
            reviews = room.get("reviews", [])
            
            if not reviews:
                avg_score = 0
            else:
                total_mark = sum(r.get("mark", 0) for r in reviews)
                avg_score = total_mark / len(reviews)
            
            room_data = room.copy()
            room_data["id"] = room["_id"]
            room_data["avg_rating"] = round(avg_score, 2)
            
            scored_rooms.append(room_data)

        scored_rooms.sort(key=lambda x: x["avg_rating"], reverse=True)
        
        if scored_rooms:
            best_rooms[room_type] = scored_rooms[:2]

    return best_rooms
        
def TakeRandomPhotoByRoomType(room_type):
    room_collection = conectRoomCollection()
    room = room_collection.find_one({"category": room_type}, {"category_images": 1})
    
    if room and "category_images" in room and room["category_images"]:
        images = room["category_images"]
        idx = randint(0, len(images) - 1)
        return images[idx]

def FilterRooms(filters: list[str]) -> list[dict]:
    room_collection = conectRoomCollection()
    if room_collection is None: return []

    type_filters = [f for f in filters if f in ROOMS_TYPES]
    price_filters = [f for f in filters if "€" in f]
    feature_filters = [f for f in filters if f not in type_filters and f not in price_filters]

    query = {}
    if type_filters:
        query["category"] = {"$in": type_filters}

    candidates = room_collection.find(query)
    
    filtered_results = []

    for room in candidates:
        room_flat = room.copy()
        room_flat["id"] = room["_id"]
        room_flat["type"] = room["category"] 
        
        if price_filters:
            price = room_flat.get("price", 0)
            price_match = False
            for pf in price_filters:
                clean_str = pf.replace("€", "").strip()
                
                try:
                    if "+" in clean_str: 
                        limit = int(clean_str.replace("+", ""))
                        if price >= limit: price_match = True
                    elif "-" in clean_str: 
                        parts = clean_str.split("-")
                        if len(parts) == 2:
                            min_p, max_p = int(parts[0]), int(parts[1])
                            if min_p <= price <= max_p: price_match = True
                except ValueError:
                    continue
                
                if price_match: break 
            
            if not price_match: continue 

        if feature_filters:
            room_features = room_flat.get("content", []) + room_flat.get("bed", [])
            room_features = [str(f) for f in room_features]
            
            if not all(f in room_features for f in feature_filters):
                continue

        filtered_results.append(room_flat)
if __name__ == "__main__": print(FilterRooms(["King"]))