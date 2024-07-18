
def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Ensure the number is positive for easy iteration through digits
    num = abs(num)
    
    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0
    
    # Iterate through each digit in the number
    while num > 0:
        digit = num % 10  # Get the last digit
        if digit % 2 == 0:  # Check if the digit is even
            even_count += 1
        else:  # The digit is odd
            odd_count += 1
        num = num // 10  # Remove the last digit and continue
    
    return (even_count, odd_count)
