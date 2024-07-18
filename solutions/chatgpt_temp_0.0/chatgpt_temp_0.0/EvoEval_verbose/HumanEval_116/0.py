
def sort_array(arr):
    if any((num < 0 for num in arr)):
        print('Invalid input. The list should only contain non-negative integers.')
        return

    def count_ones(num):
        return bin(num).count('1')
    arr.sort(key=lambda x: (count_ones(x), x))