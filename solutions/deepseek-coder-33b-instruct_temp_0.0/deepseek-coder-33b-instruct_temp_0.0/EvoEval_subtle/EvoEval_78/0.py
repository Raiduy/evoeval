
def hex_key(num):
    non_prime_hex = ['0', '1', '4', '6', '8', '9', 'A', 'C', 'E']
    count = 0
    for digit in num:
        if digit in non_prime_hex:
            count += 1
    return count