
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    """
    # Remove duplicates by converting the list to a set, then back to a list
    unique_lst = list(set(lst))
    
    # Check if the list has less than 2 unique elements
    if len(unique_lst) < 2:
        return None
    
    # Sort the list to find the second smallest element
    unique_lst.sort()
    
    # Return the second element
    return unique_lst[1]
