
def solve(N):
    binary = bin(N)[2:]
    digit_sum = sum((int(digit) for digit in binary))
    return bin(digit_sum)[2:]