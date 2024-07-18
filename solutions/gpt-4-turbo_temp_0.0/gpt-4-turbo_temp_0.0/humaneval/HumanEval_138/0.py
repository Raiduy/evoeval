
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if n is less than 8 or odd
    if n < 8 or n % 2 != 0:
        return False
    # Since the smallest even number is 2, and we need exactly 4 numbers,
    # we check if n - 6 (the smallest sum of three even numbers) is still even.
    # This is because if n - 6 is even, then n can be expressed as the sum of 2 + 2 + 2 + (n-6),
    # where (n-6) is also an even number.
    # This condition is actually redundant for the purpose of this specific function,
    # as any n >= 8 and even will satisfy the condition to be written as a sum of 4 even numbers.
    # However, it illustrates the thought process for a more general case.
    return True
