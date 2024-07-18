

def least_common_multiple(a: int, b: int) -> int:
    """ Return the least common multiple of two integers a and b
    >>> least_common_multiple(3, 5)
    15
    >>> least_common_multiple(25, 15)
    75
    """

    def gcd(a: int, b: int) -> int:
        """ Return the greatest common divisor of two integers a and b """
        while b:
            (a, b) = (b, a % b)
        return a
    return a * b // gcd(a, b)