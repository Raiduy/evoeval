def largest_prime_divisor(n: int, k: int) -> int:
    primes = []
    for i in range(2, n):
        if all((i % j != 0 for j in range(2, i))):
            primes.append(i)
    divisors = []
    for i in primes:
        if n % i == 0:
            divisors.append(i)
    divisors.sort(reverse=True)
    if k > len(divisors):
        return -1
    else:
        return divisors[k - 1]