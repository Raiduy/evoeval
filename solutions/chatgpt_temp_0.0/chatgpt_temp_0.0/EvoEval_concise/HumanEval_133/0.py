

def sum_squares(lst):
    """Return the sum of squares of each element in the list, after rounding each element to the nearest integer towards positive infinity.
    
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    sum_of_squares = 0
    for num in lst:
        rounded_num = int(num + 0.5)
        sum_of_squares += rounded_num ** 2
    return sum_of_squares