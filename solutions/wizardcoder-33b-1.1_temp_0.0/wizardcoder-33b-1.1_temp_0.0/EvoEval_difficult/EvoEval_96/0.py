def prime_sequences(n, m):
    if n == 0 or m == 0:
        return []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [i for i in range(n) if is_prime(i)]
    if len(primes) < m:
        return []
    return [primes[i:i + m] for i in range(len(primes) - m + 1)]