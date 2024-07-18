
def mod_shift_sort(arr, n: int, p: int):
    if not arr:
        return True
    else:
        mod_val = pow(2, n) % p
        for i in range(mod_val):
            temp_arr = arr[i:] + arr[:i]
            if temp_arr == sorted(temp_arr):
                return True
        return False