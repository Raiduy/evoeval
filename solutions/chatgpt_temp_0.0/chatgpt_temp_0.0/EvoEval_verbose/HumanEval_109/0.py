
def move_one_ball(arr):
    if len(arr) == 0:
        return True
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        shifted_arr = arr[i:] + arr[:i]
        if shifted_arr == sorted_arr:
            return True
    return False