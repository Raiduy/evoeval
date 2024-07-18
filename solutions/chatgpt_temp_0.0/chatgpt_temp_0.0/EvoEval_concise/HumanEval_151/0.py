
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
    sum_of_squares = 0
    for num in lst:
        if num > 0 and num % 2 != 0:
            sum_of_squares += num ** 2
    return sum_of_squares