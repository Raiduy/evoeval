def magical_sorting(arr):
    if not arr:
        return True
    out_of_order = sum((arr[i] > arr[i + 1] for i in range(len(arr) - 1)))
    if out_of_order == 0 or out_of_order == 2:
        return True
    return False