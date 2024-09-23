
def strange_sort_list(lst):
    """
    This function accepts a list of integers as an input and returns the list sorted in an unusual manner.
    This unusual or "strange" sorting is characterized by the following pattern: the minimum value is first, 
    followed by the maximum of the remaining integers, then the minimum of the remaining integers, and so on until there are no more integers left.

    The sorting continues in this min-max-min pattern until the entire list has been sorted. If there are duplicate integers, 
    they are treated separately - each occurrence is considered as a separate integer.
    
    When the input list is empty, the function should return an empty list. The order of equal elements is not guaranteed to be preserved.

    Here are some examples to illustrate how the function behaves:

    If the input is [1, 2, 3, 4], the output will be [1, 4, 2, 3]. 
    The minimum integer 1 is first, followed by the maximum of the remaining integers 4, 
    then the minimum of the remaining integers 2, and lastly the maximum of the remaining integers, 3.

    If the input is [5, 5, 5, 5], the output will be [5, 5, 5, 5]. 
    Since all the integers are the same, the output is the same as the input.

    If the input is [], the output will also be [] since there are no integers to sort.

    Parameters:
    lst (List[int]): A list of integers to be sorted in strange order.
    
    Returns:
    List[int]: A list of integers sorted in a strange order.
    """
    result = []
    while lst:
        min_val = min(lst)
        lst.remove(min_val)
        result.append(min_val)
        if lst:
            max_val = max(lst)
            lst.remove(max_val)
            result.append(max_val)
    return result