def hex_key_primes(num):
    prime_digits = ['2', '3', '5', '7', 'B', 'D']
    prime_count = 0
    non_prime_count = 0
    prime_sum = 0
    for digit in num:
        if digit in prime_digits:
            prime_count += 1
            if digit == 'B':
                prime_sum += 11
            elif digit == 'D':
                prime_sum += 13
            else:
                prime_sum += int(digit, 16)
        else:
            non_prime_count += 1
    if prime_count > non_prime_count:
        return (prime_count, 'Dominant', prime_sum)
    else:
        return (prime_count, 'Non-dominant', prime_sum)