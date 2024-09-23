def smallest_change_and_sum(arr, x, y):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.
    After finding the minimum changes, add the value of x and y to it.

    For example:
    smallest_change_and_sum([1, 2, 3, 5, 4, 7, 9, 6], 2, 3) == 9
    smallest_change_and_sum([1, 2, 3, 4, 3, 2, 2], 1, 2) == 4
    smallest_change_and_sum([1, 2, 3, 2, 1], 3, 2) == 5
    """
    changes = 0
    n = len(arr)
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            changes += 1
    return changes + x + y