
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
    negatives = [i for i in lst if i < 0]
    positives = [i for i in lst if i > 0]
    if not negatives:
        max_negative = None
    else:
        max_negative = max(negatives)
    if not positives:
        min_positive = None
    else:
        min_positive = min(positives)
    return (max_negative, min_positive)