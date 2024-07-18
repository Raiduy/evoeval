
from typing import List

def special_prime_factorial(n: int) -> int:
    """ 
    This function first factorizes the input 'n' into its prime factors and then calculates a special factorial.
    The 'special factorial' is defined as the product of factorials of all the prime factors of 'n'.
    The factors should be calculated number of times corresponding to how many times they appear in the factorization.
    The function should return the product of these factorials.
    
    For instance,
    >>> special_prime_factorial(8)
    8  # because 8 = 2*2*2; 2! * 2! * 2 = 2 * 2 * 2 = 8
    >>> special_prime_factorial(25)
    14400 # because 25 = 5*5; 5!-- 5!-- = 120 * 120 = 14400
    >>> special_prime_factorial(70)
    1209600 # because 70 = 2 * 5 * 7; 2!-- 5!-- 7!-- = 2 * 120 * 5040 = 1209600
    """

    def prime_factors(n):
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
    prime_factor_list = prime_factors(n)
    prime_factor_counts = {factor: prime_factor_list.count(factor) for factor in prime_factor_list}
    result = 1
    for (factor, count) in prime_factor_counts.items():
        result *= math.factorial(factor) ** count
    return result