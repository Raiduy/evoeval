
def mod_shift_sort(arr, n: int, p: int):
    if not arr:
        return True
    arr.sort()
    for i in range(len(arr)):
        if arr[i] != arr[i % len(arr)]:
            return False
    return 2 ** n % p <= len(arr)