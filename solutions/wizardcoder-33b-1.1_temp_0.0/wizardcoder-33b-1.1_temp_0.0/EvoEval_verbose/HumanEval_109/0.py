
def move_one_ball(arr):
    if not arr:
        return True
    else:
        min_index = arr.index(min(arr))
        return arr[min_index:] + arr[:min_index] == sorted(arr)