

def largest_prime_factor(n: int) -> int:
    """
    This function computes and returns the largest prime factor of a given integer. 

    A prime factor is a factor that is a prime number. Prime numbers are numbers that have exactly two distinct positive divisors: 1 and the number itself. The largest prime factor is therefore the highest prime number that can divide the input number, 'n', without leaving a remainder.

    The function assumes that the input number 'n' is greater than 1 and is not a prime number itself. This assumption is made because 1 is not a prime number and a prime number's largest prime factor would be the number itself.

    Parameters:
    n (int): an integer greater than 1 and is not a prime number, which we want to find the largest prime factor for

    Returns:
    int: The largest prime factor of the input number 'n'

    Examples:
    >>> largest_prime_factor(13195)
    29
    This means that the largest prime number that can divide 13195 without leaving a remainder is 29.

    >>> largest_prime_factor(2048)
    2
    This means that the largest prime number that can divide 2048 without leaving a remainder is 2.
    """
    largest_prime = 2
    while n % 2 == 0:
        n = n // 2
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            largest_prime = factor
            n = n // factor
        else:
            factor += 2
    if n > 1:
        largest_prime = n
    return largest_prime