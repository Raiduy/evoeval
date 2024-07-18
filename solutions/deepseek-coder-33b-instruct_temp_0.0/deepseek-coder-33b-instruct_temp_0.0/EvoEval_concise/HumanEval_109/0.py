
def move_one_ball(arr):
    """Determines if it's possible to sort an array of N unique integers in non-decreasing order 
    by repeatedly performing a right shift operation. A right shift operation refers to moving 
    all elements one position to the right, with the last element moving to the first position. 

    Returns True if possible, False if not. An empty array is considered sorted and will return True.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: 2 right shift operations can sort the array in non-decreasing order.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation: No amount of right shift operations can sort the array in non-decreasing order.                
    """
    if len(arr) == 0:
        return True
    else:
        sorted_arr = sorted(arr)
        for i in range(len(arr)):
            arr = arr[-1:] + arr[:-1]
            if arr == sorted_arr:
                return True
        return False