
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the absolute values of other two, and all numbers are integers.
    Returns false in any other cases.
    """
    if all((isinstance(i, int) for i in [x, y, z])):
        return x == abs(y) + abs(z) or y == abs(x) + abs(z) or z == abs(x) + abs(y)
    else:
        return False