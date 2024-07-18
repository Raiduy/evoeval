
def mod_shift_sort(arr, n: int, p: int):
    if len(arr) == 0:
        return True
    arr.sort()
    num_shifts = pow(2, n, p)
    return num_shifts >= len(arr)