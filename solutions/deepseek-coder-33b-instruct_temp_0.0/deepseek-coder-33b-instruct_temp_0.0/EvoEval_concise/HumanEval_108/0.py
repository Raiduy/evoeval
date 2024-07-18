
def count_nums(arr):
    """
    Define a function count_nums that takes an array of integers and returns the count of elements 
    with their sum of signed digits greater than 0. For negative numbers, the first digit is negative.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for num in arr:
        digit_sum = sum((int(digit) for digit in str(abs(num))))
        if num < 0:
            digit_sum = -digit_sum
        if digit_sum > 0:
            count += 1
    return count