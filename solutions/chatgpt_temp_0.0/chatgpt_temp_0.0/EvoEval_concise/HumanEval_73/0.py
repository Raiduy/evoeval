
def smallest_change(arr):
    """
    Calculate the minimum number of changes required to transform the input array, arr, into a palindrome. A palindrome
    array reads the same forwards and backwards. One change involves substituting an element with any other element.

    Example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    changes = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            changes += 1
    return changes