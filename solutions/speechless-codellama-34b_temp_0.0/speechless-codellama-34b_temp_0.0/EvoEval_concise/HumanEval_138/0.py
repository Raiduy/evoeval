
def is_equal_to_sum_even(n):
    """Check if the input number n can be expressed as the sum of exactly 4 positive even numbers.
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    even_count = 0
    even_sum = 0
    for i in range(2, n + 1):
        if i % 2 == 0:
            even_count += 1
            even_sum += i
            if even_count > 4:
                return False
            if even_sum == n:
                return True
    return False