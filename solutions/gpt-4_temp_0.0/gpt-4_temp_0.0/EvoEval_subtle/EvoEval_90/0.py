
def next_largest(lst):
    """
    You are given a list of integers.
    Write a function next_largest() that returns the 2nd largest element of the list.
    Return None if there is no such element.
    
    next_largest([1, 2, 3, 4, 5]) == 4
    next_largest([5, 1, 4, 3, 2]) == 4
    next_largest([]) == None
    next_largest([1, 1]) == None
    """
    if len(lst) < 2:
        return None
    else:
        lst = list(set(lst))
        if len(lst) < 2:
            return None
        else:
            lst.sort()
            return lst[-2]