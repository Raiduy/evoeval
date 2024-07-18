
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 4 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(90) == True
    90 = 2 * 3 * 3 * 5
    """
    factors = prime_factors(a)
    return len(factors) == 4