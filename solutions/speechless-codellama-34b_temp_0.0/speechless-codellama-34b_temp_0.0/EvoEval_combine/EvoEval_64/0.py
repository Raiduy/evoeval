
def modp_prime_numbers(n: int, p: int):
    modulo_result = pow(2, n, p)
    prime_numbers = []
    if modulo_result < 2:
        return prime_numbers
    if modulo_result == 2:
        return [2]
    if modulo_result == 3:
        return [3]
    if modulo_result == 5:
        return [5]
    if modulo_result == 7:
        return [7]
    if modulo_result % 2 == 0:
        return prime_numbers
    if modulo_result % 3 == 0:
        return prime_numbers
    if modulo_result % 5 == 0:
        return prime_numbers
    if modulo_result % 7 == 0:
        return prime_numbers
    if modulo_result > 7:
        for i in range(3, int(modulo_result ** 0.5) + 1, 2):
            if modulo_result % i == 0:
                break