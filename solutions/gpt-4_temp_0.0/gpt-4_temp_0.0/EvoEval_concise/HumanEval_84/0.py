
def solve(N):
    """
    Returns the sum of the digits in the binary representation of a positive integer N, as a binary string.

    Example:
        For N = 1000, binary sum of digits is 1, output: "1".
        For N = 150, binary sum of digits is 6, output: "110".
        For N = 147, binary sum of digits is 12, output: "1100".

    Variables:
        N : integer (0 ≤ N ≤ 10000)
    Output:
        string representing binary number
    """
    binary_N = bin(N)[2:]
    binary_sum = sum((int(digit) for digit in binary_N))
    return bin(binary_sum)[2:]