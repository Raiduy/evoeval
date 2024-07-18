
def mod_shift_sort(arr, n, p):
    if not arr:
        return True
    max_val = max(arr)
    min_val = min(arr)
    shift_limit = pow(2, n, p)
    shift_count = 0
    for i in range(len(arr)):
        if arr[i] == max_val:
            shift_count = i
            break
    for i in range(len(arr) - 1):
        if arr[(i + shift_count) % len(arr)] > arr[(i + shift_count + 1) % len(arr)]:
            return False
    return shift_count <= shift_limit