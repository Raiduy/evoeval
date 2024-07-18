def palindromic_and_odd_digit_array(arr):
    """Given a list of positive integers 'arr', return the minimum number of elements
    that need to be changed to make the array both palindromic and containing only odd digits. 
    A palindromic array is an array that is read the same backwards and forwards. 
    An array containing only odd digits is an array where every digit in every element is an odd number. 
    In one change, you can change one element to any other positive integer.
    
    For example:
    >>> palindromic_and_odd_digit_array([1, 2, 3, 5, 4, 2, 9, 6])
    4
    >>> palindromic_and_odd_digit_array([1, 2, 3, 4, 3, 6, 2])
    4
    >>> palindromic_and_odd_digit_array([1, 2, 3, 2, 1])
    2
    """

    def is_palindromic(num):
        return str(num) == str(num)[::-1]

    def has_even_digit(num):
        return any((int(digit) % 2 == 0 for digit in str(num)))
    changes_needed = 0
    for num in arr:
        if not is_palindromic(num) or has_even_digit(num):
            changes_needed += 1
    return changes_needed