
def largest_smallest_integers(lst):
    """
    Returns a tuple (a, b), where 'a' is the maximum negative integer 
    and 'b' is the minimum positive integer in the given list.
    If no negative or positive integers are present, returns None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    max_negative = None
    min_positive = None
    for num in lst:
        if num < 0:
            if max_negative is None or num > max_negative:
                max_negative = num
        elif num > 0:
            if min_positive is None or num < min_positive:
                min_positive = num
    return (max_negative, min_positive)