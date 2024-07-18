
def sort_array(arr):
    """
    Sorts an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.
    """
    # Convert each element to binary and count the number of ones
    ones_count = [str(bin(x)).count('1') for x in arr]
    
    # Sort the array based on the count of ones and decimal value
    arr.sort(key=lambda x: (ones_count[arr.index(x)], x))
    
    return arr
