def find_castle(arr):
    n = len(arr)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = 1
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            left_max[i] = left_max[i - 1] + 1
        else:
            left_max[i] = left_max[i - 1]
    right_max[n - 1] = 1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            right_max[i] = right_max[i + 1] + 1
        else:
            right_max[i] = right_max[i + 1]
    max_hills = 0
    for i in range(n):
        max_hills = max(max_hills, left_max[i] + right_max[i])
    return max_hills