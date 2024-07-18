
def strange_sort_list(lst):
    """
    This function accepts a list of integers as an input and returns the list sorted in an unusual manner.
    This unusual or "strange" sorting is characterized by the following pattern: the minimum value is first, 
    followed by the maximum of the remaining integers, then the minimum of the remaining integers, and so on until there are no more integers left.

    The sorting continues in this min-max-min pattern until the entire list has been sorted. If there are duplicate integers, 
    they are treated separately - each occurrence is considered as a separate integer.
    
    When the input list is empty, the function should return an empty list. The order of equal elements is not guaranteed to be preserved.

    Parameters:
    lst (List[int]): A list of integers to be sorted in strange order.
    
    Returns:
    List[int]: A list of integers sorted in a strange order.
    """
    sorted_list = []
    while lst:
        if lst:
            min_val = min(lst)
            sorted_list.append(min_val)
            lst.remove(min_val)
        if lst:
            max_val = max(lst)
            sorted_list.append(max_val)
            lst.remove(max_val)
    return sorted_list