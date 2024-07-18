def largest_prime_factor(n: int, m: int) -> int:
    """Return the largest or smallest prime factor of n based on the primality of m."""
    factors = prime_factors(n)
    if is_prime(m):
        return max(factors)
    else:
        return min(factors)