
def is_equal_to_sum_even(n):
    """Check if the input number n can be expressed as the sum of exactly 4 positive even numbers."""
    if n < 16:
        return False
    if n % 2 != 0:
        return False
    return True