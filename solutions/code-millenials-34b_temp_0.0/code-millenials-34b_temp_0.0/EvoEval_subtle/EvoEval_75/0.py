
def is_multiply_prime(a):
    factors = []
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            factors.append(i)
            a //= i
            if len(factors) > 4:
                return False
    return len(factors) == 4