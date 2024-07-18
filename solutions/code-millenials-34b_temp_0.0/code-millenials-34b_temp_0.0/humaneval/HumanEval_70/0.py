
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    # Sort the list in increasing order
    lst.sort()

    # Initialize an empty list 
    result = []

    # While there are still elements in the list
    while lst:
        # Add the smallest element to the new list
        result.append(lst.pop(0))

        # If there are still elements in the list
        if lst:
            # Add the largest element to the new list
            result.append(lst.pop())
            
    return result
