
def maximum(arr, k):
    arr_sorted = sorted(arr, reverse=True)
    return arr_sorted[:k]