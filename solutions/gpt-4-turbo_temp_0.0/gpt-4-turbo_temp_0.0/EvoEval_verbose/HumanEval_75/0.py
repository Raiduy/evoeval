
def is_multiply_prime(a):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if a < 2:
        return False
    prime_factors = []
    while a % 2 == 0:
        prime_factors.append(2)
        a = a // 2
    for i in range(3, int(a ** 0.5) + 1, 2):
        while a % i == 0:
            if is_prime(i):
                prime_factors.append(i)
            a = a // i
    if a > 2:
        prime_factors.append(a)
    return len(prime_factors) == 3