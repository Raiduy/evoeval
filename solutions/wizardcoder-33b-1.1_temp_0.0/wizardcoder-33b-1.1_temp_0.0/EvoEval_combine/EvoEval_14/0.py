
def prime_avg_range(n, m):
    if n > m:
        return -1
    primes = [i for i in range(n, m + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and i > 1]
    if not primes:
        return -1
    avg = round(sum(primes) / len(primes))
    return bin(avg)