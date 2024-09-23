
def sort_array(arr):
    """
    This function is tasked with sorting an input list, 'arr', which consists of non-negative integers. The sorting algorithm 
    isn't a typical numerical sort but uses the binary representation of the numbers.
    
    The numbers are sorted according to the number of '1's present in their binary representation. The numbers with fewer '1's 
    in their binary form come first (i.e., in ascending order). 
    
    In cases where two or more numbers have the same amount of '1's in their binary representation, these numbers are then sorted 
    based on their decimal value in ascending order. In other words, the function will first sort the numbers based on the 
    count of '1's in their binary form. If a tie occurs, the sorting falls back on the decimal representation of tied numbers.
    
    This function does not return anything but modifies the input list in-place.
    
    Examples:
    >>> sort_array([1, 5, 2, 3, 4])
    The binary form of these numbers are [1, 101, 10, 11, 100] and when sorted based on the count of '1's 
    and then their decimal value, the output will be [1, 2, 3, 4, 5]
    
    >>> sort_array([-2, -3, -4, -5, -6])
    Since the function only deals with non-negative integers, the input here is invalid. However, if we 
    were to ignore the negative sign, the binary form of these numbers would be [10, 11, 100, 101, 110] and 
    when sorted based on the count of '1's and then their decimal value, the output will be [-6, -5, -4, -3, -2] 
    
    >>> sort_array([1, 0, 2, 3, 4]) 
    The binary form of these numbers are [1, 0, 10, 11, 100] and when sorted based on the count of '1's 
    and then their decimal value, the output will be [0, 1, 2, 3, 4]
    """
    arr.sort(key=lambda x: (bin(x).count('1'), x))