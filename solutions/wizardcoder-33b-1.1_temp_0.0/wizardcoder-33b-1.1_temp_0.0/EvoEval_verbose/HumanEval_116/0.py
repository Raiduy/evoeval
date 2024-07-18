
def sort_array(arr):
    if all((isinstance(i, int) and i >= 0 for i in arr)):
        arr.sort(key=lambda x: (bin(x).count('1'), x))
    else:
        print('Invalid input. The list should only contain non-negative integers.')