
def prime_avg_range(n, m):
    if n > m:
        return -1
    primes = []
    for i in range(n, m + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    if not primes:
        return -1
    avg = round(sum(primes) / len(primes))
    return bin(avg)