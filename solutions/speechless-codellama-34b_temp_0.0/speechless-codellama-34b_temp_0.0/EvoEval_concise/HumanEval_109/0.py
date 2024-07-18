
def move_one_ball(arr):
    if not arr:
        return True
    for i in range(len(arr)):
        if arr[i] <= arr[(i + 1) % len(arr)]:
            continue
        else:
            return False
    return True