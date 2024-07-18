
def fizz_buzz(n: int):
    """Return the number of times the digit 8 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    0
    >>> fizz_buzz(79)
    1
    """
    count = 0
    for i in range(n):
        if (i % 11 == 0 or i % 13 == 0) and '8' in str(i):
            count += 1
    return count