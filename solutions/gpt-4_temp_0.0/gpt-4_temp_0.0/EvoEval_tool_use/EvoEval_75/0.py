def calculate_distance(point_a, point_b):
    """
    This helper function will calculate the Euclidean distance between two points.
    Each point is represented as a tuple of two values (x, y).
    """
    from math import sqrt
    distance = sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)
    return distance
def find_nearest_bus_stop(user_coordinate, bus_stops):
    """
    Write a function that returns the id of the nearest bus stop to the user's location.

    The user's location and the bus stops locations are two-dimensional (x, y). 
    The bus stops data is stored in a list of tuple: bus stop id, x coordinate, y coordinate (e.g., 123,5,6).

    The function should return the id of the bus stop that is closest to the user.

    Example:
    find_nearest_bus_stop((3, 4), [(123, 4, 5), (321, 3, 3)]) -> 321

    Assumption: The user's location and the bus stops locations are all in the range of 0-100 (inclusive), and the bus stop id is always an integer.
    """
    nearest_bus_stop = None
    min_distance = float('inf')
    for bus_stop in bus_stops:
        bus_stop_coordinate = (bus_stop[1], bus_stop[2])
        distance = calculate_distance(user_coordinate, bus_stop_coordinate)
        if distance < min_distance:
            min_distance = distance
            nearest_bus_stop = bus_stop[0]
    return nearest_bus_stop