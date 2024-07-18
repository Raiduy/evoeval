
def move_one_ball(arr):
    if len(arr) == 0:
        return True
    else:
        for i in range(len(arr)):
            arr = arr[i:] + arr[:i]
            if arr == sorted(arr):
                return True
        return False
