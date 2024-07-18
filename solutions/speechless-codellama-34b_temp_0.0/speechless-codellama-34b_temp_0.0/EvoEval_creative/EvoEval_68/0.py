def magical_sorting(arr):
    if len(arr) == 0:
        return True
    else:
        for i in range(len(arr)):
            if arr[i] > arr[(i + 1) % len(arr)]:
                (arr[i], arr[(i + 1) % len(arr)]) = (arr[(i + 1) % len(arr)], arr[i])
                break
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True