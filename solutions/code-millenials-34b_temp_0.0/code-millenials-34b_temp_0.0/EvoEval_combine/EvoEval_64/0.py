
def modp_prime_numbers(n: int, p: int):
    modulo_result = 2 ** n % p
    prime_numbers = [i for i in range(2, modulo_result) if is_prime(i)]
    return prime_numbers