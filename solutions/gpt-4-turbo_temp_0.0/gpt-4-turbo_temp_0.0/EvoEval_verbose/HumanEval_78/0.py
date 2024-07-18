
def hex_key(num):
    prime_hex_digits = '2357BD'
    count = 0
    for char in num:
        if char in prime_hex_digits:
            count += 1
    return count