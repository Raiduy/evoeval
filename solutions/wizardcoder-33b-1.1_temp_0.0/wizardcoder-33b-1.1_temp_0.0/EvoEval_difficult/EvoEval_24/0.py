def largest_prime_divisor(n: int, k: int) -> int:

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [i for i in range(2, n) if n % i == 0 and is_prime(i)]
    primes.sort(reverse=True)
    return primes[k - 1] if k <= len(primes) else -1