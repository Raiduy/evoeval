
def prime_avg_range(n, m):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [i for i in range(n, m + 1) if is_prime(i)]
    if not primes:
        return -1
    avg = round(sum(primes) / len(primes))
    return bin(avg)