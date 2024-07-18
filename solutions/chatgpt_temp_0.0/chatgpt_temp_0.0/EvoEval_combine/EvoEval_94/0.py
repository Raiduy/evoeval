
def sort_count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            num = -num
        digit_sum = sum((int(digit) for digit in str(num)))
        if digit_sum > 0:
            count += 1
    if count % 2 == 0:
        sorted_arr = sorted(arr, reverse=True)
    else:
        sorted_arr = sorted(arr)
    return sorted_arr