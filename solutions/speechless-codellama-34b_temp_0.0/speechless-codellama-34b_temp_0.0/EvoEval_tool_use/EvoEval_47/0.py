def validate_coordinates(coordinates: str) -> bool:
    """
    Helper function to validate the coordinates format
    Takes a string representation of the coordinates as input
    The accepted format is two numbers separated by a comma and
    a space like: '23.5, -45.6'
    Returns True if the input string is in correct format, False otherwise

    >>> validate_coordinates('23.5, -45.6')
    True
    >>> validate_coordinates('23.5,-45.6')
    False
    >>> validate_coordinates('23.5 -45.6')
    False
    """
    parts = coordinates.split(', ')
    if len(parts) != 2:
        return False

    try:
        float(parts[0])
        float(parts[1])
    except ValueError:
        return False

    return True
def calculate_distance(coordinates1: str, coordinates2: str) -> float:
    """
    Write a function to calculate the distance between two points on Earth
    represented by their coordinates. The coordinates are represented as
    strings with the format 'latitude, longitude'. The latitude and longitude
    values are in decimal degrees. Use the Haversine formula to calculate the distance:
        a = sin²(ΔlatDifference/2) + cos(lat1)*cos(lt2)*sin²(ΔlonDifference/2) 
        c = 2*atan2(√a, √(1−a))
        distance= 6371 *c
    
    The result should be in kilometers. Round the result to the nearest integer.
    
    You can assume that the Earth is a perfect sphere with a radius of 6371 kilometers.
    
    The function should return -1 if any of the coordinate strings is in incorrect format.
    """
    if not validate_coordinates(coordinates1) or not validate_coordinates(coordinates2):
        return -1
    (lat1, lon1) = map(float, coordinates1.split(', '))
    (lat2, lon2) = map(float, coordinates2.split(', '))
    R = 6371
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return round(distance)