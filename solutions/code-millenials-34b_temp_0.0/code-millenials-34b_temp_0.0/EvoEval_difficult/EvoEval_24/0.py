def largest_prime_divisor(n: int, k: int) -> int:

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [i for i in range(2, n) if is_prime(i) and n % i == 0]
    primes.sort(reverse=True)
    if len(primes) < k:
        return -1
    else:
        return primes[k - 1]