
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    
    # If the number is less than 10, it can't be written as the sum of 4 even numbers
    if n < 10:
        return False
    
    # If the number is even, subtract 2 to make it odd
    if n % 2 == 0:
        n -= 2
    
    # If the number is now odd, it can't be written as the sum of 4 even numbers
    if n % 2 != 0:
        return False
    
    # If the number is divisible by 4, it can be written as the sum of 4 even numbers
    if n % 4 == 0:
        return True
    
    # Otherwise, it can't be written as the sum of 4 even numbers
    return False
