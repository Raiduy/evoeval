
def order_by_points(nums):
    """
    Sort a list of integers in ascending order by the sum of their digits. 
    In case of ties, maintain original order. 

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    def digit_sum(num):
        return sum((int(d) for d in str(abs(num))))
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))