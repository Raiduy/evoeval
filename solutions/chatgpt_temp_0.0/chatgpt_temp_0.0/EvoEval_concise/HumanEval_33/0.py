

def sort_third(l: list):
    """Takes a list 'l' and returns a new list with l's elements at indices divisible by three sorted, while other elements remain the same.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    divisible_by_three = [x for (i, x) in enumerate(l) if (i + 1) % 3 == 0]
    sorted_divisible_by_three = sorted(divisible_by_three)
    result = [x if (i + 1) % 3 != 0 else sorted_divisible_by_three.pop(0) for (i, x) in enumerate(l)]
    return result