
def is_equal_to_sum_even(n):
    """Check if the input number n can be expressed as the sum of exactly 4 positive even numbers.
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 10:
        return False
    elif n % 2 == 0:
        return True
    else:
        return False