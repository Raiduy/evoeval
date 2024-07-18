def hex_key_primes(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    prime_count = 0
    prime_sum = 0
    for digit in num:
        if digit in primes:
            prime_count += 1
            if digit == '2':
                prime_sum += 2
            elif digit == '3':
                prime_sum += 3
            elif digit == '5':
                prime_sum += 5
            elif digit == '7':
                prime_sum += 7
            elif digit == 'B':
                prime_sum += 11
            elif digit == 'D':
                prime_sum += 13
    if prime_count > len(num) - prime_count:
        return (prime_count, 'Dominant', prime_sum)
    else:
        return (prime_count, 'Non-dominant', prime_sum)