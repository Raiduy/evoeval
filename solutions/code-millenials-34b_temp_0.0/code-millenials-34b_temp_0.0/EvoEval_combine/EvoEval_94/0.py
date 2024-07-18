
def sort_count_nums(arr):

    def sum_digits(n):
        if n < 0:
            n = -n
        return sum((int(digit) for digit in str(n)))
    count = sum((1 for num in arr if sum_digits(num) > 0))
    sorted_arr = sorted(arr, reverse=count % 2 == 0)
    return sorted_arr