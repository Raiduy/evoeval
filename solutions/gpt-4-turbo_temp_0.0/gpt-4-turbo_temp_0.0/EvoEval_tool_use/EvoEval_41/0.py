def valid_coordinate(coord: str):
    """
    Helper Function

    This function checks whether a given string is a valid (x, y) coordinate.
    A valid coordinate should have the form (x,y) where x and y are integers.

    Args:
        coord (str): The input string to check.

    Returns:
        bool: True if the string is a valid coordinate, False otherwise.
    """
    if coord[0] != '(' or coord[-1] != ')':
        return False

    values = coord[1:-1].split(',')
    if len(values) != 2:
        return False

    try:
        x, y = int(values[0]), int(values[1])
    except ValueError:
        return False

    return True


def convert_to_int(coord: str):
    """
    Helper Function

    This function converts a string of the form (x,y) into a tuple of integers (x, y).

    Args:
        coord (str): The input string to convert.

    Returns:
        tuple: A tuple of two integers representing the coordinates.
    """
    values = coord[1:-1].split(',')
    x, y = int(values[0]), int(values[1])
    return (x, y)
from typing import List


def find_path(start: str, end: str, obstacles: List[str]) -> int:
    if not (valid_coordinate(start) and valid_coordinate(end) and all((valid_coordinate(o) for o in obstacles))):
        return -1
    start_coord = convert_to_int(start)
    end_coord = convert_to_int(end)
    obstacle_coords = {convert_to_int(o) for o in obstacles}
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    queue = deque([(start_coord[0], start_coord[1], 0)])
    visited = set([start_coord])
    while queue:
        (x, y, steps) = queue.popleft()
        if (x, y) == end_coord:
            return steps
        for (dx, dy) in directions:
            (nx, ny) = (x + dx, y + dy)
            if (nx, ny) not in obstacle_coords and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
        if steps > 100:
            return -1
    return -1