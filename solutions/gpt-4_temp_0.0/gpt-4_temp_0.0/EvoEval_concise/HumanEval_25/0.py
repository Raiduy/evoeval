from typing import List


def factorize(n: int) -> List[int]:
    """ Returns the list of prime factors of 'n', sorted from smallest to largest. 
    The frequency of each factor matches its occurrence in the factorization of 'n'.
    The product of all factors equals the input number.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors