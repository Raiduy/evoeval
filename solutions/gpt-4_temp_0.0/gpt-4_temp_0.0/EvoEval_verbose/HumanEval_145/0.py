def order_by_points(nums):
    """
    This function is designed to sort a provided list of integers in ascending order, but the order is determined not by the 
    integer values themselves, but by the sum of their digits. This provides an alternative sorting mechanism that might be
    useful in certain contexts. For instance, the number 11 (with a digit sum of 2) would come before the number 9 (with a digit 
    sum of 9), even though in standard numeric order, 9 would come before 11.

    If there are multiple numbers with the same sum of digits, the order of these numbers in the original list will be preserved 
    i.e., the function implements a stable sort. This means that if two numbers have the same sum of digits, the number that appeared 
    first in the original list will appear first in the sorted list.

    The function takes the following parameter:

    nums: A list of integers that will be sorted based on the sum of their digits.

    The function returns a list of integers sorted according to the criteria described above.

    Here are some examples to illustrate how the function works:

    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    In this case, the function returns the list [-1, -11, 1, -12, 11] 

    >>> order_by_points([]) == []
    In this case, the function returns a blank list, as the input list is empty.
    """

    def sum_of_digits(n):
        return sum((int(digit) for digit in str(abs(n))))
    return sorted(nums, key=sum_of_digits)