def has_duplicates(lst):
    """
    Given a list, this function checks if the list has any duplicate values.
    Returns True if duplicates exist, False otherwise.
    """
    return len(lst) != len(set(lst))

def min_value(lst):
    """
    Given a list, this function returns the minimum value in the list.
    Returns None if the list is empty.
    """
    if not lst: return None
    return min(lst)
def unique_minimum(lst):
    """
    Given a list of integers, this function returns the smallest integer in the list. 
    However, if the smallest integer has duplicates in the list, return None. 
    If the list is empty, return None.
    """
    if not lst:
        return None
    min_val = min(lst)
    if lst.count(min_val) > 1:
        return None
    return min_val