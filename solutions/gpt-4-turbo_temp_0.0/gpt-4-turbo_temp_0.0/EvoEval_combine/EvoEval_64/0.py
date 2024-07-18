
def modp_prime_numbers(n: int, p: int) -> list:
    """Implement a function that takes two non-negative integers n and p, first calculate 2^n modulo p, 
    then return an array of the first calculated modulo result integers that are prime numbers and less than the calculated modulo result.
    If no prime numbers are found within the range, return an empty array."""
    mod_result = pow(2, n, p)
    primes = [i for i in range(2, mod_result) if is_prime(i)]
    return primes