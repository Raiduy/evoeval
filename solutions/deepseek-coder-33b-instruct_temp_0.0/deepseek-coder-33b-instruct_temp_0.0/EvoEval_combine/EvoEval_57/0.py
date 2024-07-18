def palindromic_and_odd_digit_array(arr):
    n = len(arr)
    changes = 0
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            changes += 1
        if arr[i] % 2 == 0 or arr[n - i - 1] % 2 == 0:
            changes += 1
    if n % 2 == 1 and arr[n // 2] % 2 == 0:
        changes += 1
    return changes