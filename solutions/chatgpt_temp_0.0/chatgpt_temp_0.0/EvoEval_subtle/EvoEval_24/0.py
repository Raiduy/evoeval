
def smallest_divisor(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor(15)
    3
    """
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    return divisor