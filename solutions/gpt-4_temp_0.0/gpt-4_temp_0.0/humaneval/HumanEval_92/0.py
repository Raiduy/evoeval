
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    # Check if all inputs are integers
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        # Check if one number is the sum of the other two
        if x == y + z or y == x + z or z == x + y:
            return True
    return False
