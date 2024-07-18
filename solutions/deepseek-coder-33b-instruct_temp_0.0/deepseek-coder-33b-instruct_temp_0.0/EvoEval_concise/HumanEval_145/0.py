
def order_by_points(nums):
    """
    Sort a list of integers in ascending order by the sum of their digits. 
    In case of ties, maintain original order. 

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    def sum_of_digits(n):
        return sum((int(digit) for digit in str(abs(n))))
    return sorted(nums, key=sum_of_digits)