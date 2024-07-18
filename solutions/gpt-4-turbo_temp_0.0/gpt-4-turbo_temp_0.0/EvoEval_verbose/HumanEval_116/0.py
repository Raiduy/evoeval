
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
    """

    def sort_key(x):
        return (bin(x).count('1'), x)
    arr.sort(key=sort_key)