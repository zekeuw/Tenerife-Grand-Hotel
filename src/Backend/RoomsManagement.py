# This file will control the rooms updates
from .Connection import conectRoomCollection

ROOMS_TYPES = ["Presidential", "Luxury", "Privacy", "Apartment", "Regular"]




def TakeAllRooms() -> list[dict]:
    room_collection = conectRoomCollection()
    return list(room_collection.find({}, {"_id": 0}))

def TakeMostValuedRooms()-> list[dict]:
    """This function will take the 2 best valued rooms and return them"""
    room_collection = conectRoomCollection()
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

def FilterRooms(filters: list[str]) -> list[dict]:
    all_data = TakeAllRooms()[0]
    filtered_results = []

    type_filters = [f for f in filters if f in ROOMS_TYPES]
    price_filters = [f for f in filters if "€" in f]
    feature_filters = [f for f in filters if f not in type_filters and f not in price_filters]

    for room_type, rooms_group in all_data.items():
        if room_type in ["images", "reviews"]: continue
        
        if type_filters and room_type not in type_filters:
            continue

        for room_id, room_info in rooms_group.items():
            if room_id in ["images", "reviews"]: continue
            
            room_flat = room_info.copy()
            room_flat["id"] = room_id
            room_flat["type"] = room_type

            if price_filters:
                price = room_flat.get("price", 0)
                price_match = False
                for pf in price_filters:
                    clean_str = pf.replace("€", "").strip()
                    
                    if "+" in clean_str: 
                        limit = int(clean_str.replace("+", ""))
                        if price >= limit: price_match = True
                    elif "-" in clean_str: 
                        min_p, max_p = map(int, clean_str.split("-"))
                        if min_p <= price <= max_p: price_match = True
                    
                    if price_match: break 
                
                if not price_match: continue 

            if feature_filters:
                room_features = room_flat.get("content", []) + room_flat.get("bed", [])
                
                if not all(f in room_features for f in feature_filters):
                    continue

            filtered_results.append(room_flat)

    return filtered_results

if __name__ == "__main__": print(FilterRooms(["King"]))