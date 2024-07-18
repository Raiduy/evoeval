
def count_up_to(n):
    prime_numbers = []
    for i in range(n, 0, -1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers