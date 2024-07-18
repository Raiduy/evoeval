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
    Returns the id of the nearest bus stop to the user's location.
    """
    distances = []
    for bus_stop in bus_stops:
        distance = calculate_distance(user_coordinate, (bus_stop[1], bus_stop[2]))
        distances.append((bus_stop[0], distance))
    distances.sort(key=lambda x: x[1])
    return distances[0][0]