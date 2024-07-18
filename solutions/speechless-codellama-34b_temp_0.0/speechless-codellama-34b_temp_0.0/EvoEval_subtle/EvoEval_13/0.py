

def least_common_multiple(a: int, b: int) -> int:
    """ Return the least common multiple of two integers a and b """
    return abs(a * b) // gcd(a, b)