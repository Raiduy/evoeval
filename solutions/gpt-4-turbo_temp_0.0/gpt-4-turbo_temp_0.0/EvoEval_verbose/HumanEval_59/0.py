

def largest_prime_factor(n: int) -> int:
    """
    This function computes and returns the largest prime factor of a given integer. 

    A prime factor is a factor that is a prime number. Prime numbers are numbers that have exactly two distinct positive divisors: 1 and the number itself. The largest prime factor is therefore the highest prime number that can divide the input number, 'n', without leaving a remainder.

    The function assumes that the input number 'n' is greater than 1 and is not a prime number itself. This assumption is made because 1 is not a prime number and a prime number's largest prime factor would be the number itself.

    Parameters:
    n (int): an integer greater than 1 and is not a prime number, which we want to find the largest prime factor for

    Returns:
    int: The largest prime factor of the input number 'n'
    """
    while n % 2 == 0:
        largest_prime = 2
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n = n // i
    if n > 2:
        largest_prime = n
    return largest_prime