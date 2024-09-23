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


def find_path(start: str, end: str, obstacles: List[str]):
    if not valid_coordinate(start) or not valid_coordinate(end) or (not all((valid_coordinate(obstacle) for obstacle in obstacles))):
        return -1
    start = convert_to_int(start)
    end = convert_to_int(end)
    obstacles = set(map(convert_to_int, obstacles))
    if start == end:
        return 0
    queue = deque([(start, 0)])
    visited = set([start])
    while queue:
        (current, steps) = queue.popleft()
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_coord = (current[0] + dx, current[1] + dy)
            if next_coord == end:
                return steps + 1
            if next_coord not in visited and next_coord not in obstacles and (0 <= next_coord[0] <= 100) and (0 <= next_coord[1] <= 100):
                queue.append((next_coord, steps + 1))
                visited.add(next_coord)
    return -1