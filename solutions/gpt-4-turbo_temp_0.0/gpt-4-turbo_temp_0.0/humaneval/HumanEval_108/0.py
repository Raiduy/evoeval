
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def sum_of_digits(n):
        """
        This helper function takes an integer and returns the sum of its digits.
        If the number is negative, the first digit is considered negative.
        """
        if n < 0:
            return -int(str(n)[1]) + sum(int(digit) for digit in str(n)[2:])
        else:
            return sum(int(digit) for digit in str(n))
    
    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1
    return count
