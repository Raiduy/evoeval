
def can_arrange(arr):
    """Define a function that returns the highest index of a number in the array that is not equal to or greater than its preceding number. Return -1 if no such number exists. The input array does not have duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return i
    return -1