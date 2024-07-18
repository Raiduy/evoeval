

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start checking from n-1 down to 1
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1  # This line is technically unreachable for n > 1, as 1 will always divide n