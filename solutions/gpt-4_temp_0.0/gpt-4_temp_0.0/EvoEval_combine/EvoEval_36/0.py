
def mod_shift_sort(arr, n: int, p: int):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N]. The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
        However, the number of times you can perform the shift operation is 
        limited by the result of 2^n modulo p (modp(n, p)).
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    within the determined limit then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements and the values of n 
    and p are positive integers.

    For Example:
    
    mod_shift_sort([3, 4, 5, 1, 2], 3, 5) ==> True
    Explanation: By performing 2 right shift operations, non-decreasing order can
                 be achieved for the given array and 2 is less than 3 (2^3 mod 5).
    mod_shift_sort([3, 5, 4, 1, 2], 2, 3) ==> False
    Explanation: It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
    mod_shift_sort([3, 4, 5, 1, 2], 2, 3) ==> False
    Explanation: Although it is possible to get non-decreasing order for the array 
                by performing enough right shift operations, the number of operations 
                required is more than the limit (2^3 mod 5).
    """
    if not arr:
        return True
    limit = pow(2, n) % p
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        if arr == sorted_arr:
            return True
        if i >= limit:
            return False
        arr = [arr[-1]] + arr[:-1]
    return False