
def solve(N):
    binary_N = bin(N)[2:]
    binary_sum = sum((int(digit) for digit in binary_N))
    return bin(binary_sum)[2:]