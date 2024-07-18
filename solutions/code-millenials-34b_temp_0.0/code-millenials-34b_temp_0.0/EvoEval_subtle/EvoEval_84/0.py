
def solve(N):
    digit_sum = sum((int(digit) for digit in str(N)))
    return hex(digit_sum)[2:].upper()