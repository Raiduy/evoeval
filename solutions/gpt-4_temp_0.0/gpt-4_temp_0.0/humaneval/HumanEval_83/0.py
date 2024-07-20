
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    else:
        # For n-digit numbers, there are 10^(n-1) numbers that start with a particular digit
        # and 10^(n-1) numbers that end with a particular digit.
        # Since we are counting numbers that start or end with 1, we need to subtract the overlap
        # (numbers that start and end with 1) to avoid double counting.
        return 2 * 10**(n-1) - 10**(n-2)
