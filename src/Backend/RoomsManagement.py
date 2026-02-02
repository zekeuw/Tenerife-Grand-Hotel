from .Connection import conectRoomCollection
from random import choice, randint

ROOMS_TYPES = ["Presidential", "Luxury", "Privacy", "Apartment", "Regular"]

def TakeRandomPhotoByRoomType(room_type):
    room_collection = conectRoomCollection()
    room = room_collection.find_one({"category": room_type}, {"category_images": 1})
    
    if room and "category_images" in room and room["category_images"]:
        images = room["category_images"]
        idx = randint(0, len(images) - 1)
        return images[idx]

def TakeRoomImage(room):
    room["main_image"] = choice(room["category_images"])
    room["id"] = room["_id"]
    return room

def TakeAllRooms() -> list[dict]:
    room_collection = conectRoomCollection()
    if room_collection is None: return []
    rooms = room_collection.find({})
    return [TakeRoomImage(room) for room in rooms]

def FilterRooms(filters: list[str]) -> list[dict]:
    room_collection = conectRoomCollection()
    if room_collection is None: return []

    type_filters = [f for f in filters if f in ROOMS_TYPES]
    price_filters = [f for f in filters if "€" in f]
    feature_filters = [f for f in filters if f not in type_filters and f not in price_filters]

    query = {}

    if type_filters:
        query["category"] = {"$in": type_filters}

    if feature_filters:
        and_conditions = []
        for feature in feature_filters:
            and_conditions.append({
                "$or": [
                    {"content": feature},
                    {"bed": feature}
                ]
            })
        if and_conditions:
            query["$and"] = and_conditions

    rooms_filtered = room_collection.find(query)
    
    results = []
    
    for room in rooms_filtered:
        price = room.get("price", 0)
        pass_price = True
        
        if price_filters:
            pass_price = False
            for pf in price_filters:
                clean_str = pf.replace("€", "").strip()
                try:
                    if "+" in clean_str: 
                        limit = int(clean_str.replace("+", ""))
                        if price >= limit: pass_price = True
                    elif "-" in clean_str: 
                        parts = clean_str.split("-")
                        if len(parts) == 2:
                            min_p, max_p = int(parts[0]), int(parts[1])
                            if min_p <= price <= max_p: pass_price = True
                except ValueError:
                    continue
                if pass_price: break 
        
        if pass_price:
            results.append(TakeRoomImage(room))

    return results

def TakeMostValuedRooms() -> dict:
    room_collection = conectRoomCollection()
    if room_collection is None: return None

    best_rooms = {}

    for room_type in ROOMS_TYPES:
        rooms = room_collection.find({"category": room_type})
        scored_rooms = []
        
        for room in rooms:
            reviews = room.get("reviews", [])
            avg_score = 0
            if reviews:
                avg_score = sum(r.get("mark", 0) for r in reviews) / len(reviews)
            
            room["avg_rating"] = round(avg_score, 2)
            scored_rooms.append(TakeRoomImage(room))
        
        scored_rooms.sort(key=lambda x: x["avg_rating"], reverse=True)
        if scored_rooms:
            best_rooms[room_type] = scored_rooms[:2]
        

    return best_rooms

