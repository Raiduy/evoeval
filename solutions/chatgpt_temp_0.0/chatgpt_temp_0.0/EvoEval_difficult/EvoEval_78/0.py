def hex_key_primes(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    prime_count = 0
    prime_sum = 0
    non_prime_count = 0
    for digit in num:
        if digit in primes:
            prime_count += 1
            prime_sum += int(digit, 16)
        else:
            non_prime_count += 1
    if prime_count > non_prime_count:
        return (prime_count, 'Dominant', prime_sum)
    else:
        return (prime_count, 'Non-dominant', prime_sum)