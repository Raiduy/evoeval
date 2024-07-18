
def smallest_change(arr):
    """
    Calculate the minimum number of changes required to transform the input array, arr, into a palindrome. A palindrome
    array reads the same forwards and backwards. One change involves substituting an element with any other element.

    Example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    min_changes = 0
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] != arr[end]:
            min_changes += 1
        start += 1
        end -= 1
    return min_changes