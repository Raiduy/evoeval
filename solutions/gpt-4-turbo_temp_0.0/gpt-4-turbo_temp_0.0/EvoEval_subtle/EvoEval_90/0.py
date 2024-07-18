
def next_largest(lst):
    """
    You are given a list of integers.
    Write a function next_largest() that returns the 2nd largest element of the list.
    Return None if there is no such element.
    """
    unique_elements = list(set(lst))
    if len(unique_elements) < 2:
        return None
    unique_elements.sort()
    return unique_elements[-2]