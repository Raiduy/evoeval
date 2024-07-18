
def hex_key(num):
    non_prime_hex = ['0', '1', '4', '6', '8', '9', 'A', 'C', 'E']
    count = sum((1 for digit in num if digit in non_prime_hex))
    return count