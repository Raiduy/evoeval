

def sum_squares(lst):
    """Return the sum of squares of each element in the list, after rounding each element to the nearest integer towards positive infinity.
    
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    return sum((int(x) ** 2 for x in lst))