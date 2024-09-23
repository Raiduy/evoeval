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
    if not validate_coordinates(coordinates1) or not validate_coordinates(coordinates2):
        return -1
    (lat1, lon1) = map(float, coordinates1.split(', '))
    (lat2, lon2) = map(float, coordinates2.split(', '))
    (lat1, lon1, lat2, lon2) = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c
    return round(distance)