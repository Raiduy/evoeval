def magical_sorting(arr):
    if len(arr) == 0:
        return True
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        return True
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            break
    else:
        return True
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            (arr[i], arr[(i + 1) % n]) = (arr[(i + 1) % n], arr[i])
            break
    else:
        return False
    return arr == sorted_arr