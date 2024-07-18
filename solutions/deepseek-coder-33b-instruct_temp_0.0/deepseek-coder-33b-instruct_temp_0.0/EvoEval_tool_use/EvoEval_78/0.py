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
    (x, y) = start
    for (direction, distance) in steps:
        (dx, dy) = translate_direction(direction)
        x += dx * distance
        y += dy * distance
    return (x, y)