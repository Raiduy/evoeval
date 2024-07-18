def magical_sorting(arr):

    def is_sorted(arr):
        return all((arr[i] <= arr[i + 1] for i in range(len(arr) - 1)))
    if is_sorted(arr) or not arr:
        return True
    min_index = arr.index(min(arr))
    arr = arr[min_index:] + arr[:min_index]
    inversions = sum((1 for i in range(len(arr) - 1) for j in range(i + 1, len(arr)) if arr[i] > arr[j]))
    if inversions > 1:
        return False
    else:
        return True