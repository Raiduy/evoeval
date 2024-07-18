
def move_one_ball(arr):
    if len(arr) <= 1:
        return True
    break_count = 0
    for i in range(len(arr)):
        if arr[i] > arr[(i + 1) % len(arr)]:
            break_count += 1
        if break_count > 1:
            return False
    return True