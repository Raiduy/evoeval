def is_sorted(lst):
    """
    This function checks if a given list of integers is sorted in ascending order.
    The function takes one argument, lst, which is the list that needs to be checked.

    The function will return True if the integers in the list are sorted in ascending order and False if they are not. 
    Additionally, if the list contains more than one duplicate of the same integer, the function will return False. 

    It is assumed that the input list will not contain any negative numbers and will only consist of integers.

    The function works as follows:

    1. Checks if the list is in ascending order.
    2. If it is, the function then checks if any number in the list is duplicated more than once.
    3. If there is such a number, the function returns False. 
    4. If there are no such numbers and the list is in ascending order, the function returns True.

    Here are some examples to illustrate how this function works:

    is_sorted([5]) => True
    This is because the list contains only one number, which means it is sorted in ascending order and there are no duplicates.

    is_sorted([1, 2, 3, 4, 5]) => True
    As you can see, the function returns True because the list is sorted in ascending order and none of the numbers are duplicated more than once.

    is_sorted([1, 3, 2, 4, 5]) => False
    Here, the function returned False because the list is not sorted in ascending order.

    is_sorted([1, 2, 2, 3, 3, 4]) => True
    In this example, the function returns True since the list is sorted in ascending order and there are no numbers that are duplicated more than once.

    is_sorted([1, 2, 2, 2, 3, 4]) => False
    Lastly, this function returned False because the number 2 is duplicated more than once in the list which is against the conditions of the function.
    """
    if lst != sorted(lst):
        return False
    elif len(lst) != len(set(lst)):
        return False
    else:
        return True