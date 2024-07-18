def smallest_change(arr, k):
    n = len(arr)
    changes = 0
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            changes += 1
            arr[n - i - 1] = arr[i]
    sum_arr = sum(arr)
    if sum_arr % k != 0:
        changes += (k - sum_arr % k) // (k // 2)
    return changes