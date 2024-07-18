
def is_equal_to_sum_even(n):
    """Check if the input number n can be expressed as the sum of exactly 4 positive even numbers.
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    count = 0
    for i in range(2, n, 2):
        for j in range(2, n, 2):
            for k in range(2, n, 2):
                for l in range(2, n, 2):
                    if i + j + k + l == n:
                        count += 1
    return count > 0