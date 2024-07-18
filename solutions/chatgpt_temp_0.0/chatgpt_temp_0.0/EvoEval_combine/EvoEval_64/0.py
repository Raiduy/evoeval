
def modp_prime_numbers(n: int, p: int):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    modulo_result = pow(2, n, p)
    primes = [num for num in range(2, modulo_result) if is_prime(num)]
    return primes