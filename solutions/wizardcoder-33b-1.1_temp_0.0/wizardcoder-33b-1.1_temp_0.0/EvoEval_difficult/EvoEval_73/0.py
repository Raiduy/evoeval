def smallest_change(arr, k):
    n = len(arr)
    changes = 0
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            changes += 1
    if changes % k != 0:
        changes += k - changes % k
    return changes