
def hex_key(num):
    """Function to count non-prime hexadecimal digits."""
    non_prime_hex_digits = {'0', '1', '4', '6', '8', '9', 'A', 'C', 'E'}
    non_prime_count = 0
    for digit in num:
        if digit in non_prime_hex_digits:
            non_prime_count += 1
    return non_prime_count