
def hex_key(num):
    primes = [2, 3, 5, 7, 11, 13, 17]
    count = 0
    for digit in num:
        if digit in ['0', '1', '4', '6', '8', '9', 'A', 'C', 'E']:
            count += 1
        elif digit.isdigit():
            if int(digit) not in primes:
                count += 1
    return count