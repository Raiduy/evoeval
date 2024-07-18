
def sort_array(arr):
    bin_counts = [(str(bin(num)).count('1'), num) for num in arr]
    arr.sort(key=lambda x: (str(bin(x)).count('1'), x))
    for i in range(len(arr)):
        arr[i] = bin_counts[i][1]