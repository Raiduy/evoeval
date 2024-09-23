def hex_key_primes(num):
    hex_primes = {'2': 2, '3': 3, '5': 5, '7': 7, 'B': 11, 'D': 13}
    count = 0
    total = 0
    for digit in num:
        if digit in hex_primes:
            count += 1
            total += hex_primes[digit]
    if count > len(num) / 2:
        return (count, 'Dominant', total)
    else:
        return (count, 'Non-dominant', total)