def palindromic_and_odd_digit_array(arr):
    changes = 0
    odd_digits = set('13579')
    for i in range(len(arr) // 2):
        if arr[i] != arr[-i - 1]:
            changes += 1
    for num in arr:
        for digit in str(num):
            if digit not in odd_digits:
                changes += 1
    return changes