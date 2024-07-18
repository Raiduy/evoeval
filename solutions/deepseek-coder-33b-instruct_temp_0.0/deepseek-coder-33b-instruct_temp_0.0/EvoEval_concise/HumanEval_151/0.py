
def double_the_difference(lst):
    """
    Returns the sum of squares of positive odd integers in the list. 
    Zero is included, negatives are excluded. Returns 0 for an empty list.

    Example:
    double_the_difference([1, 3, 2, 0]) == 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    """
    return sum((i ** 2 for i in lst if i > 0 and i % 2 != 0))