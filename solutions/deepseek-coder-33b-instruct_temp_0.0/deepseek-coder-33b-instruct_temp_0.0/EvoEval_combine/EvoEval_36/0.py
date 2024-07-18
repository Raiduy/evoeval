
def mod_shift_sort(arr, n: int, p: int):
    if not arr:
        return True
    max_shift = pow(2, n, p)
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        if arr == sorted_arr:
            return True
        else:
            arr = arr[-1:] + arr[:-1]
    return False