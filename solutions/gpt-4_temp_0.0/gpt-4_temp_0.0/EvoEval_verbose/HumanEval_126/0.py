def is_sorted(lst):
    """
    This function, is_sorted, checks if a given list of integers is sorted in ascending order. The function takes one argument, lst, which is the list that needs to be checked.

    The function will return True if the integers in the list are sorted in ascending order and False if they are not. Additionally, if the list contains more than one duplicate of the same integer, the function will return False. 

    It is assumed that the input list will not contain any negative numbers and will only consist of integers.

    The function works as follows:

    1. Checks if the list is in ascending order.
    2. If it is, the function then checks if any number in the list is duplicated more than once.
    3. If there is such a number, the function returns False. 
    4. If there are no such numbers and the list is in ascending order, the function returns True.
    """
    if lst != sorted(lst):
        return False
    for i in lst:
        if lst.count(i) > 1:
            return False
    return True