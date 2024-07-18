
def sort_array(arr):
    arr.sort()
    arr.sort(key=lambda x: bin(x).count('1'))
    return arr