
def choose_num(x, y):
    """Returns the largest even integer within the inclusive range [x, y]. 
    If no even number exists, return -1.

    Example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if y % 2 == 0:
        return y
    elif x % 2 == 0:
        return x
    else:
        return -1