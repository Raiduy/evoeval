
def prime_avg_range(n, m):
    """Compute the binary representation of the rounded average of prime numbers in a given range."""
    if n > m:
        return -1
    primes = [i for i in range(n, m + 1) if is_prime(i)]
    if not primes:
        return -1
    avg = round(sum(primes) / len(primes))
    return bin(avg)