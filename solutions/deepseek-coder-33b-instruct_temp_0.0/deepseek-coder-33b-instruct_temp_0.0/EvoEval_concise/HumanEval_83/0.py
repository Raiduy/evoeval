
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of n-digit positive integers that either begin or conclude with 1.
    """
    if n == 1:
        return 2
    else:
        return 2 + 9 * 10 ** (n - 2)