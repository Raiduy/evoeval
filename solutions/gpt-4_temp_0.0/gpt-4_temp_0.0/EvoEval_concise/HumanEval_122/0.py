
def add_elements(arr, k):
    """
    This function takes an array (arr) of integers and another integer (k). Its task is to return 
    the sum of the elements in the first k elements of arr that have at most two digits.

    Example:
        arr = [111,21,3,4000,5,6,7,8,9], k = 4
        should return: 24  # 21 + 3

    Constraints:
        1. The length of arr is between 1 and 100.
        2. k is between 1 and the length of arr.
    """
    sum = 0
    for i in range(k):
        if arr[i] >= -99 and arr[i] <= 99:
            sum += arr[i]
    return sum