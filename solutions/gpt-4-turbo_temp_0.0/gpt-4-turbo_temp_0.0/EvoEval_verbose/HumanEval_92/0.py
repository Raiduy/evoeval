
def any_int(x, y, z):
    """
    This function checks if one of the numbers equals the sum of the other two and if all numbers are integers.
    """
    if not all((isinstance(i, int) for i in [x, y, z])):
        return False
    return x == y + z or y == x + z or z == x + y