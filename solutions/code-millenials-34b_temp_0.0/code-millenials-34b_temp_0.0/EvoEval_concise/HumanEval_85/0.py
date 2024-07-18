
def add(lst):
    """Sum the even numbers at odd indices in a non-empty list of integers, lst.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    total_sum = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            total_sum += lst[i]
    return total_sum