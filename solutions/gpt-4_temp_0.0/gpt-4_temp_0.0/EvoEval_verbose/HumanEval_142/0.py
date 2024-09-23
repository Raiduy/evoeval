def sum_squares(lst):
    """
    This function is designed to perform certain mathematical operations on a list of integers, 'lst', based on the index position of each 
    integer in the list. The operations and their conditions are as follows: 

    1. If an integer's index is a multiple of 3, the function will square that integer.
    2. If an integer's index is a multiple of 4, but not a multiple of 3, the function will cube that integer.
    3. If an integer's index is not a multiple of either 3 or 4, the function will leave that integer unchanged. 

    After performing the above operations, the function will then sum together all the entries in the list and return this sum. 

    It's important to note that Python uses zero-based indexing, so the first element of the list is at index 0, the second element is at 
    index 1, and so on. 

    If an empty list is provided, the function will simply return 0, as there are no entries to perform operations on and sum together.
    """
    total = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            total += lst[i] ** 2
        elif i % 4 == 0:
            total += lst[i] ** 3
        else:
            total += lst[i]
    return total