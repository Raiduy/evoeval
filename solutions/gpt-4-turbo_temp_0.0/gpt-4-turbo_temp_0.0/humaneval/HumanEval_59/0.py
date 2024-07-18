

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Step 1: Remove factors of 2
    while n % 2 == 0:
        max_prime = 2
        n //= 2
    
    # Step 2 and 3: Check for odd factors
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            max_prime = divisor
            n //= divisor
        divisor += 2
    
    # Step 4: Check if n is a prime number greater than 2
    if n > 2:
        max_prime = n
    
    return max_prime
