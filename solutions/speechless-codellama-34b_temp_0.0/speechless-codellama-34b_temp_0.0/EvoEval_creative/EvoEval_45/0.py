def find_castle(arr):
    n = len(arr)
    left = [0] * n
    right = [0] * n
    max_left = 0
    max_right = 0
    for i in range(n):
        while max_left < i and arr[max_left] < arr[i]:
            max_left += 1
        left[i] = i - max_left
        while max_right < i and arr[max_right] < arr[n - i - 1]:
            max_right += 1
        right[n - i - 1] = i - max_right
    max_hills = 0
    for i in range(n):
        max_hills = max(max_hills, left[i] + right[i] + 1)
    return max_hills