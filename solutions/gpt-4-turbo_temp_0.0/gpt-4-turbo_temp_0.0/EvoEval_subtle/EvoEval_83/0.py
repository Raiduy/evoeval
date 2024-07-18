
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start with 1 or end with 2.
    """
    if n == 1:
        return 2
    else:
        starts_with_1 = 9 ** (n - 1)
        ends_with_2 = 10 ** (n - 1)
        starts_1_ends_2 = 9 ** (n - 2)
        total = starts_with_1 + ends_with_2 - starts_1_ends_2
        return total