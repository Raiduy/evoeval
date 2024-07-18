
def choose_num(x, y):
    """Returns the largest even integer within the inclusive range [x, y]. 
    If no even number exists, return -1.

    Example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    largest_even = -1
    for num in range(x, y + 1):
        if num % 2 == 0:
            largest_even = num
    return largest_even