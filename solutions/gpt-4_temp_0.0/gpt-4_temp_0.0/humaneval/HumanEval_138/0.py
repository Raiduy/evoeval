
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # The smallest possible sum of 4 positive even numbers is 2+2+2+2=8
    # So, if n is less than 8, it cannot be written as the sum of 4 positive even numbers
    if n < 8:
        return False
    # If n is greater than or equal to 8, we check if it is divisible by 2
    # If it is, then it can be written as the sum of 4 positive even numbers
    # If it is not, then it cannot be written as the sum of 4 positive even numbers
    else:
        return n % 2 == 0
