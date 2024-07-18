
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        # If n is 1, then there's only 1 number that starts and ends with 1, which is 1 itself.
        return 1
    
    # Counting numbers that start with 1
    starts_with_1 = 9 ** (n - 1)
    
    # Counting numbers that end with 1
    ends_with_1 = 9 * (10 ** (n - 2))
    
    # Adjusting for double counting
    double_counted = 10 ** (n - 2)
    
    # Total count
    total_count = starts_with_1 + ends_with_1 - double_counted
    
    return total_count
