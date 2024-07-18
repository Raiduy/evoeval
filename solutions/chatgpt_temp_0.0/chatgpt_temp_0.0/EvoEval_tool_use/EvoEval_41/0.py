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
    """
    Imagine a robot positioned at a specific coordinate on a grid. The robot can only move
    in four directions: up, down, left, right. The robot is trying to reach an end coordinate
    while avoiding various obstacles. Each coordinate on the grid is represented as a string
    in the form (x,y).

    This function should output the shortest path for the robot to take from the start to the
    end coordinate while avoiding the obstacles. Each move from one coordinate to an adjacent
    coordinate counts as one step.

    Args:
        start (str): The start coordinate in the form (x,y).
        end (str): The end coordinate in the form (x,y).
        obstacles (List[str]): A list of obstacles, each represented as a string in the form
        (x,y).

    Returns:
        int: The shortest path length, or -1 if inputs are invalid or there is no path to the
        end coordinate without hitting an obstacle or the shortest path is longer than 100 steps.
    """
    if not valid_coordinate(start) or not valid_coordinate(end):
        return -1
    start_coord = convert_to_int(start)
    end_coord = convert_to_int(end)
    if start_coord == end_coord:
        return 0
    if start in obstacles or end in obstacles:
        return -1
    for obstacle in obstacles:
        if not valid_coordinate(obstacle):
            return -1
    if len(obstacles) > 100:
        return -1
    return -1