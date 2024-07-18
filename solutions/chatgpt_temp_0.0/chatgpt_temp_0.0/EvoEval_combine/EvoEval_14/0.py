
def prime_avg_range(n, m):
    if n > m:
        return -1
    primes = []
    for num in range(n, m + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    if len(primes) == 0:
        return -1
    avg = round(sum(primes) / len(primes))
    binary = bin(avg)
    return binary