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
    that is closest to the target point.
    """
    if not is_valid_coordinate(target) or not all((is_valid_coordinate(point) for point in points)):
        return 'Invalid input'
    (target_x, target_y) = map(int, target.split(','))
    closest = None
    min_distance = float('inf')
    for point in points:
        (x, y) = map(int, point.split(','))
        distance = sqrt((x - target_x) ** 2 + (y - target_y) ** 2)
        if distance < min_distance:
            closest = point
            min_distance = distance
        elif distance == min_distance:
            if int(point.split(',')[0]) < int(closest.split(',')[0]):
                closest = point
    return closest if closest is not None else ''