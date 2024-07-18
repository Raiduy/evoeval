def smallest_change(arr, k):
    n = len(arr)
    changes = 0
    total_sum = 0
    for i in range(n // 2):
        total_sum += arr[i] + arr[n - i - 1]
        if arr[i] != arr[n - i - 1]:
            changes += 1
    if total_sum % k != 0:
        changes += k - total_sum % k
    return changes