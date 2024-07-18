
def choose_num(x, y):
    """Returns the largest even integer within the inclusive range [x, y]. 
    If no even number exists, return -1.

    Example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    largest_even = -1
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            largest_even = i
            break
    return largest_even