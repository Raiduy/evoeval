
def sort_count_nums(arr):
    count = 0
    for num in arr:
        if sum((int(digit) for digit in str(abs(num)))) > 0:
            count += 1
    if count % 2 == 0:
        return sorted(arr, reverse=True)
    else:
        return sorted(arr)