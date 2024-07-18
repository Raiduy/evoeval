def translate_direction(dir_string):
    """This function translates the direction string (N, S, E, W) into a tuple with respective x and y changes.
    """
    if dir_string == "N":
        return (0, 1)
    elif dir_string == "S":
        return (0, -1)
    elif dir_string == "E":
        return (1, 0)
    elif dir_string == "W":
        return (-1, 0)

def is_valid_direction(dir_string):
    """This function checks if the direction string is one of the valid directions (N, S, E, W).
    """
    return dir_string in ["N", "S", "E", "W"]
def final_position(start, steps):
    """This function takes in a start position as a tuple (x, y) on a 2D grid, and a list of steps where each step is a tuple (direction, distance), where direction is a string (N, S, E, W) and distance is a positive integer.
    
    The function should compute the final position after all steps are taken, and return this position as a tuple (x, y). 

    Note: The directions given correspond to North (N - up on the grid), South (S - down on the grid), East (E - right on the grid), West (W - left on the grid).
    
    You may assume that all inputs are valid and that the steps list is not empty.
    
    Examples:
    For start = (0, 0) and steps = [("N", 1), ("E", 2)], the output should be (2, 1).
    For start = (3, 3) and steps = [("S", 1), ("W", 3), ("N", 2)], the output should be (0, 4).
    For start = (-1, -1) and steps = [("E", 1)], the output should be (0, -1).
    """
    (x, y) = start
    for step in steps:
        (direction, distance) = step
        if not is_valid_direction(direction):
            raise ValueError('Invalid direction received.')
        (dx, dy) = translate_direction(direction)
        x += dx * distance
        y += dy * distance
    return (x, y)