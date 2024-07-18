
def unique_digits(x):
    """Returns a sorted list of integers from the input list x that do not contain any even digits.

    The list is sorted in ascending order.
    
    Example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    def has_even_digit(num):
        for digit in str(num):
            if int(digit) % 2 == 0:
                return True
        return False
    filtered_numbers = [num for num in x if not has_even_digit(num)]
    return sorted(filtered_numbers)