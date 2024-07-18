
def solve(N):
    # Convert N to binary and remove the first two characters
    binary = bin(N)[2:]

    # Calculate the sum of digits in binary
    binary_sum = sum(int(digit) for digit in binary)

    # Return the binary sum as a binary string
    return bin(binary_sum)[2:]
