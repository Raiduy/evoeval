

def sort_third(l: list):
    """Takes a list 'l' and returns a new list with l's elements at indices divisible by three sorted, while other elements remain the same.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    divisible_by_three.sort()
    for i in range(len(l)):
        if i % 3 == 0:
            l[i] = divisible_by_three.pop(0)
    return l