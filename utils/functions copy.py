def captionToCount(caption):
    """
    get product count in: 
        🍟 Food title
        Nx
        N X N So'm = Total N so'm
    """
    try:
        count = int(caption.split('\n')[1].replace("x", ""))
        return count
    
    except:
        count = 1
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    # Radius of the earth in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Differences
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance
    distance = R * c
    return distance

def calc_delivered_time(dis, speed):
    # Vaqtni soatlar va minutlarga aylantiramiz
    vaqt_soat = dis / speed

    # Vaqtni soatlar va minutlarga aylantiramiz
    soat = int(vaqt_soat)
    minut = int((vaqt_soat - soat) * 60)

    return f"{soat} soat, {minut} minut" 

def create_google_maps_link(latitude, longitude, zoom=12):
    base_url = "https://www.google.com/maps/@"
    entry_param = "?entry=ttu"
    link = f"{base_url}{latitude},{longitude},{zoom}z{entry_param}"
    return link
