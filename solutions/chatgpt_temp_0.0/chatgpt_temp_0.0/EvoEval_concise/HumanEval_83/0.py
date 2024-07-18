
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of n-digit positive integers that either begin or conclude with 1.
    """
    count = 0
    if n == 1:
        count = 1
    elif n > 1:
        count = 9 * 10 ** (n - 2) + starts_one_ends(n - 1)
    return count