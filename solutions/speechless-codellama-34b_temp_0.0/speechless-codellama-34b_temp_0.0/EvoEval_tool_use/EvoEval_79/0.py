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
    """
    Given a list of points and a target point, return the point from the list
    that is closest to the target point. Distance is calculated using the
    Euclidean distance (i.e., sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)). 
    All points including target point should be a coordinate of integer values
    in string format like 'x,y'.
    If there are multiple points at the same closest distance, return one
    with the smallest first value. If the list of points is empty, return an empty string. If any
    points are not valid coordinates format, or the target is not a valid
    coordinate, return an error message: 'Invalid input'
    """
    if not is_valid_coordinate(target):
        return 'Invalid input'
    (target_x, target_y) = map(int, target.split(','))
    closest_point = ''
    closest_distance = float('inf')
    for point in points:
        if not is_valid_coordinate(point):
            return 'Invalid input'
        (x, y) = map(int, point.split(','))
        distance = math.sqrt((x - target_x) ** 2 + (y - target_y) ** 2)
        if distance < closest_distance:
            closest_distance = distance
            closest_point = point
        elif distance == closest_distance:
            closest_point = min(closest_point, point)
    return closest_point