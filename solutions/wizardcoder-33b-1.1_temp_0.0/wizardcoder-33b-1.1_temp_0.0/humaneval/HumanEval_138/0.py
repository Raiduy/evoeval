
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    if n < 16:
        return False
    if n % 2 == 0:
        return True
    else:
        return False
