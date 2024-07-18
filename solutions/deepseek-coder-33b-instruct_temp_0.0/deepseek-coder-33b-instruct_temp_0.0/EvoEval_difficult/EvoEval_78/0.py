def hex_key_primes(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    prime_count = 0
    sum_primes = 0
    for digit in num:
        if digit in primes:
            prime_count += 1
            if digit.isdigit():
                sum_primes += int(digit)
            else:
                sum_primes += ord(digit) - 55
    if prime_count > len(num) - prime_count:
        return (prime_count, 'Dominant', sum_primes)
    else:
        return (prime_count, 'Non-dominant', sum_primes)