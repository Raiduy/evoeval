

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    """
    # Round each element to the ceiling, square it, and sum the results
    return sum(math.ceil(x)**2 for x in lst)
