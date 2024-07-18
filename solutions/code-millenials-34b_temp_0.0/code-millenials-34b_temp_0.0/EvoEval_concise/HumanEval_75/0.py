
def is_multiply_prime(a):
    prime_factors = []
    for i in range(2, a + 1):
        while a % i == 0 and is_prime(i):
            prime_factors.append(i)
            a //= i
            if a == 1:
                break
    return len(prime_factors) == 3