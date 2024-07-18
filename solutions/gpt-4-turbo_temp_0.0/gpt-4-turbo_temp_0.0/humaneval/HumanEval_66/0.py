
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.
    """
    # Initialize sum to 0
    sum_of_uppercase_ascii = 0
    
    # Iterate through each character in the string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Add the ASCII value of the uppercase character to the sum
            sum_of_uppercase_ascii += ord(char)
    
    # Return the final sum
    return sum_of_uppercase_ascii
