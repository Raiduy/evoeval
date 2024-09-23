
def starts_one_ends(n):
    """
    This function, given a user-provided positive integer 'n', calculates and returns the total count of n-digit positive integers where 1 appears either at the start or the end of the number.
    
    For instance, if the input is 2, the function will count all the two-digit numbers that either start or end with 1, like 10, 11, 21, 31, ..., 91, and 12, 13, ..., 19.
    
    It is important to note that this function only accepts positive integers. If a non-integer or non-positive integer is provided, the function may not behave as expected.
    
    Args:
    n : int
        A positive integer that represents the number of digits in the numbers to be counted.

    Returns:
    int
        The count of the numbers of n-digit positive integers that start or end with 1.

    Examples:
    The function can be called in the following way:
        starts_one_ends(2)
    This example call would return the count of two-digit numbers where 1 appears at the start or at the end.
    """
    if n == 1:
        return 1
    else:
        return 18 * 10 ** (n - 2) + 2