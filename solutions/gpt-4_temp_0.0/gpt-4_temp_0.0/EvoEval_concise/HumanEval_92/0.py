
def any_int(x, y, z):
    """
    Create a function that takes 3 integer numbers.
    Returns true if any number is the sum of the other two.
    Returns false otherwise or if any of the numbers is not an integer.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False

    """
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x + y == z or x + z == y or y + z == x:
            return True
        else:
            return False
    else:
        return False