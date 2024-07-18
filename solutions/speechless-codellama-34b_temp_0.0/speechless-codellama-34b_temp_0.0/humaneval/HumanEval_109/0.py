
def move_one_ball(arr):
    if not arr:
        return True
    else:
        for i in range(len(arr)):
            if arr[i] <= arr[(i+1)%len(arr)]:
                return True
        return False
