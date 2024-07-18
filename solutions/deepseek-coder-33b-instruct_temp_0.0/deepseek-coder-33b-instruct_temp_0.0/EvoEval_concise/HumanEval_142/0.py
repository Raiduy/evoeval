


def sum_squares(lst):
    """
    This function receives a list of integers and modifies it based on the index of each entry. If the index is a multiple of 3, 
    the entry is squared. If the index is a multiple of 4 but not 3, the entry is cubed. Other entries remain unchanged. 
    The function returns the sum of all entries.
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    for i in range(len(lst)):
        if i % 3 == 0:
            lst[i] = lst[i] ** 2
        elif i % 4 == 0:
            lst[i] = lst[i] ** 3
    return sum(lst)