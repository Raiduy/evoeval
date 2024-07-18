
def hex_key(num):
    non_prime_digits = ['0', '1', '4', '6', '8', '9', 'A', 'C', 'E']
    non_prime_count = 0
    for char in num:
        if char in non_prime_digits:
            non_prime_count += 1
    return non_prime_count