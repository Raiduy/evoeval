
def solve(N):
    sum_of_digits = sum((int(digit) for digit in str(N)))
    return hex(sum_of_digits)[2:].upper()