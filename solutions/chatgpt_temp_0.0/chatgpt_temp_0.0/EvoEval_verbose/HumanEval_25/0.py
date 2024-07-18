from typing import List


def factorize(n: int) -> List[int]:
    """
    This function accepts an integer 'n' as input and returns a list of prime factors. The prime factors are the prime numbers that divide the given integer exactly.

    The output list should be ordered from smallest to largest prime number. If a prime number is a factor multiple times, it should appear that many times in the list. That is, the number of occurrences of a prime factor should correspond to the number of times it is used in the factorization process.

    The product of all factors in the returned list should be equal to the input number 'n'. This is to ensure the correctness of the factorization.

    Examples:
    >>> factorize(8)
    [2, 2, 2]
    In this case, 8 is factorized to three 2s. 2 is the smallest prime number, and the product of three 2s is equal to 8.

    >>> factorize(25)
    [5, 5]
    Here, 25 is factorized to two 5s. 5 is a prime number and the product of two 5s is equal to 25.

    >>> factorize(70)
    [2, 5, 7]
    For this case, 70 is factorized to 2, 5 and 7. All these are prime numbers, ordered from smallest to largest, and their product equals to 70.
    """
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors