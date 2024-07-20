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
    target_parts = target.split(',')
    target_x = int(target_parts[0])
    target_y = int(target_parts[1])
    closest_point = ''
    closest_distance = float('inf')
    for point in points:
        if not is_valid_coordinate(point):
            return 'Invalid input'
        point_parts = point.split(',')
        point_x = int(point_parts[0])
        point_y = int(point_parts[1])
        distance = math.sqrt((point_x - target_x) ** 2 + (point_y - target_y) ** 2)
        if distance < closest_distance or (distance == closest_distance and point_x < int(closest_point.split(',')[0])):
            closest_distance = distance
            closest_point = point
    return closest_point if closest_point else ''