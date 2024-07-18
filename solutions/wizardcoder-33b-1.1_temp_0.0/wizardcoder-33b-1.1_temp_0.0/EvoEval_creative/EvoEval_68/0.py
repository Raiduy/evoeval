def magical_sorting(arr):
    if not arr:
        return True
    swap_used = False
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if swap_used:
                return False
            else:
                swap_used = True
                if arr[i] > arr[(i + 2) % len(arr)]:
                    (arr[i], arr[(i + 2) % len(arr)]) = (arr[(i + 2) % len(arr)], arr[i])
                else:
                    (arr[i], arr[i + 1]) = (arr[i + 1], arr[i])
    return True