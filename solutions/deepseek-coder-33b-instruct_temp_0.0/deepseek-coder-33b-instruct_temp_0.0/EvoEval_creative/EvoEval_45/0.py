def find_castle(arr):
    n = len(arr)
    left = [1] * n
    right = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            left[i] = left[i - 1] + 1
        else:
            left[i] = 1
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            right[i] = right[i + 1] + 1
        else:
            right[i] = 1
    max_hills = 0
    for i in range(n):
        max_hills = max(max_hills, left[i] + right[i] - 1)
    return max_hills