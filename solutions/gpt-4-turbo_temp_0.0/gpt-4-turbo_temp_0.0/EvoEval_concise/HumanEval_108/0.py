
def count_nums(arr):
    """
    Define a function count_nums that takes an array of integers and returns the count of elements 
    with their sum of signed digits greater than 0. For negative numbers, the first digit is negative.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def sum_of_signed_digits(num):
        num_str = str(num)
        sum_digits = 0
        if num_str[0] == '-':
            sum_digits -= int(num_str[1])
            for digit in num_str[2:]:
                sum_digits += int(digit)
        else:
            for digit in num_str:
                sum_digits += int(digit)
        return sum_digits
    count = 0
    for num in arr:
        if sum_of_signed_digits(num) > 0:
            count += 1
    return count