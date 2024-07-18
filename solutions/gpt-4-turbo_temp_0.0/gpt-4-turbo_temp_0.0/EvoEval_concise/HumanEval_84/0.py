
def solve(N):
    binary_representation = bin(N)[2:]
    sum_of_digits = sum((int(digit) for digit in binary_representation))
    binary_sum = bin(sum_of_digits)[2:]
    return binary_sum