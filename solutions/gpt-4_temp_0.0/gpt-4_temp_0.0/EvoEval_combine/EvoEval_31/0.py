
from typing import List

def special_prime_factorial(n: int) -> int:
    """ 
    This function first factorizes the input 'n' into its prime factors and then calculates a special factorial.
    The 'special factorial' is defined as the product of factorials of all the prime factors of 'n'.
    The factors should be calculated number of times corresponding to how many times they appear in the factorization.
    The function should return the product of these factorials.
    
    For instance,
    >>> special_prime_factorial(8)
    8  # because 8 = 2*2*2; 2! * 2! * 2! = 2 * 2 * 2 = 8
    >>> special_prime_factorial(25)
    14400 # because 25 = 5*5; 5! * 5! = 120 * 120 = 14400
    >>> special_prime_factorial(70)
    1209600 # because 70 = 2 * 5 * 7; 2! * 5! * 7! = 2 * 120 * 5040 = 1209600
    """
    " \n    This function first factorizes the input 'n' into its prime factors and then calculates a special factorial.\n    The 'special factorial' is defined as the product of factorials of all the prime factors of 'n'.\n    The factors should be calculated number of times corresponding to how many times they appear in the factorization.\n    The function should return the product of these factorials.\n    "
    factors = prime_factors(n)
    result = 1
    for factor in factors:
        result *= math.factorial(factor)
    return result