def is_prime_sum(lst, n):
    primes = []
    for num in lst:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if primes[i] + primes[j] == n:
                return True
    return False