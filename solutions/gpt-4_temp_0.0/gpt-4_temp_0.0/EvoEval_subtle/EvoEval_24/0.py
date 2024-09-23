
def smallest_divisor(n: int) -> int:
    """ For a given number n, find the smallest number that divides n evenly, larger than 1
    >>> smallest_divisor(15)
    3
    """
    if n <= 1:
        return None
    for i in range(2, n + 1):
        if n % i == 0:
            return i
    return None