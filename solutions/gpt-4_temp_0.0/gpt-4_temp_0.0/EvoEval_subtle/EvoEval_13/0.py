

def least_common_multiple(a: int, b: int) -> int:
    """ Return the least common multiple of two integers a and b
    >>> least_common_multiple(3, 5)
    15
    >>> least_common_multiple(25, 15)
    75
    """

    def gcd(a, b):
        while b != 0:
            (a, b) = (b, a % b)
        return a
    return abs(a * b) // gcd(a, b)