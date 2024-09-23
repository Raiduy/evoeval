
def is_sorted(lst):
    """
    Determine if a list of positive integers is sorted in ascending order. 
    Returns False if there are any duplicates beyond a pair of the same number.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    """
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
        if lst.count(lst[i]) > 2:
            return False
    return True