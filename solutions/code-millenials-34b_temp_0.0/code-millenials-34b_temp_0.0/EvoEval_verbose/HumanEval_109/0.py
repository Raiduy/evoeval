
def move_one_ball(arr):
    if not arr:
        return True
    n = len(arr)
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions % 2 == 0