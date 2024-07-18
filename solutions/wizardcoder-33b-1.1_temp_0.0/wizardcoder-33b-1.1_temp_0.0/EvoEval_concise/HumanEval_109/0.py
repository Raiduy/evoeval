
def move_one_ball(arr):
    if not arr:
        return True
    max_index = arr.index(max(arr))
    if max_index == len(arr) - 1:
        return True
    return False