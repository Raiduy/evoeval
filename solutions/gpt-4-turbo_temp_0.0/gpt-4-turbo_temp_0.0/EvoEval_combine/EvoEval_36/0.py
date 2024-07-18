
def mod_shift_sort(arr, n: int, p: int) -> bool:
    if not arr:
        return True
    limit = pow(2, n) % p
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        shifted_arr = arr[-i:] + arr[:-i]
        if shifted_arr == sorted_arr:
            if i <= limit:
                return True
            else:
                return False
    return False