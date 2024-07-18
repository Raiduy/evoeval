def hex_key_primes(num):
    prime_hex = {'2': 2, '3': 3, '5': 5, '7': 7, 'B': 11, 'D': 13}
    prime_count = 0
    prime_sum = 0
    for char in num:
        if char in prime_hex:
            prime_count += 1
            prime_sum += prime_hex[char]
    non_prime_count = len(num) - prime_count
    dominance = 'Dominant' if prime_count > non_prime_count else 'Non-dominant'
    return (prime_count, dominance, prime_sum)