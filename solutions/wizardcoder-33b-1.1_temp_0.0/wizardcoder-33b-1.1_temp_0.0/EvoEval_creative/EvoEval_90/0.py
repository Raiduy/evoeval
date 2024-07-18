def magical_multiply(s1, s2):
    digits1 = list(map(int, s1))
    digits2 = list(map(int, s2))
    total_sum = 0
    for digit1 in digits1:
        for digit2 in digits2:
            total_sum += digit1 + digit2
    return total_sum