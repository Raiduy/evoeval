
def solve(N):
    # Convert the integer to binary and remove the '0b' prefix
    binary = bin(N)[2:]
    # Initialize the sum to 0
    total = 0
    # Iterate over each digit in the binary representation
    for digit in binary:
        # Add the digit to the total
        total += int(digit)
    # Convert the total back to binary and return it
    return bin(total)[2:]
