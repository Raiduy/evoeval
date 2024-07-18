def hex_key_primes(num):
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    prime_count = sum((1 for digit in num if digit in prime_hex_digits))
    non_prime_count = len(num) - prime_count
    sum_primes = sum((int(digit, 16) for digit in num if digit in prime_hex_digits))
    status = 'Dominant' if prime_count > non_prime_count else 'Non-dominant'
    return (prime_count, status, sum_primes)