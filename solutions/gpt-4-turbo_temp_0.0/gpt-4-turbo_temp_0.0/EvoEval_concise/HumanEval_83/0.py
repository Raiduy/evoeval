
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of n-digit positive integers that either begin or conclude with 1.
    """
    if n == 1:
        return 1
    else:
        start_or_end_with_1 = 2 * 10 ** (n - 1)
        both_start_and_end_with_1 = 10 ** (n - 2)
        return start_or_end_with_1 - both_start_and_end_with_1