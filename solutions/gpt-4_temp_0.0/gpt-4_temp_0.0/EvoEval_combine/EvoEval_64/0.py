
def modp_prime_numbers(n: int, p: int):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    mod_result = pow(2, n, p)
    primes = [i for i in range(2, mod_result) if is_prime(i)]
    return primes