def find_castle(arr):
    max_hills = 0
    for i in range(len(arr)):
        left = i - 1
        while left >= 0 and arr[left] <= arr[i]:
            left -= 1
        right = i + 1
        while right < len(arr) and arr[right] <= arr[i]:
            right += 1
        max_hills = max(max_hills, right - left - 1)
    return max_hills