
def order_by_points(nums):
    """
    Sort a list of integers in ascending order by the sum of their digits. 
    In case of ties, maintain original order. 

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    points = [sum((int(digit) for digit in str(num))) for num in nums]
    sorted_nums = sorted(nums, key=lambda x: (sum((int(digit) for digit in str(x))), nums.index(x)))
    return sorted_nums