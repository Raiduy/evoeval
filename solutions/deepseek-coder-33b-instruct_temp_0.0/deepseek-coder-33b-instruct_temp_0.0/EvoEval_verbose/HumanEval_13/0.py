

def greatest_common_divisor(a: int, b: int) -> int:
    """
    This function, 'greatest_common_divisor', takes in two integers, 'a' and 'b', as input arguments and returns
    the greatest common divisor (GCD) of these two integers.

    The greatest common divisor of two numbers is the largest positive integer that divides each of the integers without a remainder.
    For example, the GCD of 8 and 12 is 4.

    Args:
    a (int): The first input integer.
    b (int): The second input integer.

    Returns:
    int: The greatest common divisor of integers 'a' and 'b'.
    
    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    This example returns 1 because 1 is the only positive integer that divides both 3 and 5 without a remainder.

    >>> greatest_common_divisor(25, 15)
    5
    This example returns 5 because 5 is the largest positive integer that divides both 25 and 15 without a remainder.  
    """
    while b != 0:
        (a, b) = (b, a % b)
    return a