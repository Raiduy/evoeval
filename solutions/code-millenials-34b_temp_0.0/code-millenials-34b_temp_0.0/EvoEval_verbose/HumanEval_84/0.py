
def solve(N):
    str_N = str(N)
    sum_of_digits = sum((int(digit) for digit in str_N))
    return bin(sum_of_digits)[2:]