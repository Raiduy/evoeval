def palindromic_and_odd_digit_array(arr):
    if arr != arr[::-1]:
        arr = arr + arr[::-1]
    for num in arr:
        if num % 2 == 0:
            arr[arr.index(num)] = num + 1 if num % 2 == 0 else num
    return sum(arr)