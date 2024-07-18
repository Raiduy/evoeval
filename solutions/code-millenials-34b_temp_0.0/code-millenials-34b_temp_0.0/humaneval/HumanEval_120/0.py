
def maximum(arr, k):
    # Use Python's built-in heapq module to find the k largest numbers in arr
    import heapq
    return sorted(heapq.nlargest(k, arr))
