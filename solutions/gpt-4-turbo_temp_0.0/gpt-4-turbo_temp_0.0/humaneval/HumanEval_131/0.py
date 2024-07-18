
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Convert the number to a string to easily iterate through each digit
    str_n = str(n)
    # Initialize the product variable to 1 (since we are multiplying)
    product = 1
    # Variable to track if we have found any odd digits
    found_odd = False
    # Iterate through each character in the string representation of n
    for char in str_n:
        # Convert the character back to an integer
        digit = int(char)
        # Check if the digit is odd
        if digit % 2 != 0:
            # Multiply the product by the digit
            product *= digit
            # Mark that we have found an odd digit
            found_odd = True
    # If we found at least one odd digit, return the product
    if found_odd:
        return product
    # If all digits were even, return 0
    return 0
