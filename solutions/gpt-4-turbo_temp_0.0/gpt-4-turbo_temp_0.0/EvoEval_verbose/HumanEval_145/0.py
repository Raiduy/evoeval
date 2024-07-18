def order_by_points(nums):
    """
    This function sorts a provided list of integers in ascending order based on the sum of their digits.
    It preserves the order of numbers with the same digit sum (stable sort).
    """
    return sorted(nums, key=sum_of_digits)