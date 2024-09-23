def next_smallest_sorted_binary(lst):
    """
    You are given a list of non-negative integers.
    First, sort the input list based on the number of ones in their binary representation in ascending order. 
    For the same number of ones, sort based on original value. 
    
    Then, return the 2nd smallest element from the sorted list. 
    Return None if there is no such element.

    next_smallest_sorted_binary([1, 2, 3, 4, 5]) == 2
    next_smallest_sorted_binary([5, 1, 4, 3, 2]) == 2
    next_smallest_sorted_binary([]) == None
    next_smallest_sorted_binary([1, 1]) == None
    """
    lst.sort(key=lambda x: (bin(x).count('1'), x))
    return lst[1] if len(lst) > 1 else None