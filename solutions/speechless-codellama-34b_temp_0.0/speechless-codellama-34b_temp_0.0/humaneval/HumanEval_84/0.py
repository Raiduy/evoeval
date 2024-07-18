
def solve(N):
    # Convert the integer to binary and remove the '0b' prefix
    binary = bin(N)[2:]
    
    # Calculate the sum of the digits in binary
    digit_sum = sum(int(digit) for digit in binary)
    
    # Convert the digit sum to binary and return it as a string
    return bin(digit_sum)[2:]
