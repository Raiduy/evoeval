
def sort_count_nums(arr):
    count = sum((sum((int(digit) for digit in str(abs(num)))) > 0 for num in arr))
    sorted_arr = sorted(arr, reverse=count % 2 == 0)
    return sorted_arr