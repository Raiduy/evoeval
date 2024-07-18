
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    # Convert the integer to a string
    N_str = str(N)

    # Initialize a variable to hold the sum of digits
    sum_digits = 0

    # Iterate over each digit in the string
    for digit in N_str:
        # Convert the digit back to an integer and add it to the sum
        sum_digits += int(digit)

    # Convert the sum to binary and return it as a string
    return bin(sum_digits)[2:]
