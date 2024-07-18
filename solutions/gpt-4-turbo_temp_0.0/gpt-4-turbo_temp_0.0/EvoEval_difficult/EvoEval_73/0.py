def smallest_change(arr, k):
    n = len(arr)
    changes_for_palindrome = 0
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            changes_for_palindrome += 1
    sum_of_elements = sum(arr)
    changes_for_divisibility = 0 if sum_of_elements % k == 0 else 1
    total_changes = changes_for_palindrome + changes_for_divisibility
    return total_changes