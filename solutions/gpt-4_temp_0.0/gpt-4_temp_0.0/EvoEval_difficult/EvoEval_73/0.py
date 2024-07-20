def smallest_change(arr, k):
    n = len(arr)
    l = 0
    r = n - 1
    changes = 0
    while l < r:
        if arr[l] != arr[r]:
            changes += 1
        l += 1
        r -= 1
    if sum(arr) % k != 0:
        changes += 1
    return changes