def is_valid_coordinate(coord: str) -> bool:
    """
    Helper function to determine if a given string is a valid coordinate.
    A valid coordinate is defined as a string of the format 'x,y' where
    x and y are both integers. If the coordinate is valid, the function
    should return True, else False.
    >>> is_valid_coordinate('1,2')
    True
    >>> is_valid_coordinate('1.2,3.4')
    False
    >>> is_valid_coordinate('10,20')
    True
    >>> is_valid_coordinate('X,Y')
    False
    """
    parts = coord.split(',')
    if len(parts) != 2:
        return False
    try:
        x = int(parts[0])
        y = int(parts[1])
    except ValueError:
        return False
    return True
def closest_point(points: list[str], target: str) -> str:
    if not is_valid_coordinate(target):
        return 'Invalid input'
    min_distance = math.inf
    closest_point = ''
    for point in points:
        if not is_valid_coordinate(point):
            return 'Invalid input'
        (x1, y1) = map(int, point.split(','))
        (x2, y2) = map(int, target.split(','))
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_point = point
        elif distance == min_distance and x1 < int(closest_point.split(',')[0]):
            closest_point = point
    return closest_point