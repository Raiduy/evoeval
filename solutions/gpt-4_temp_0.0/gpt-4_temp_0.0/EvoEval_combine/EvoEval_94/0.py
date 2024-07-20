
def sort_count_nums(arr):

    def sum_digits(n):
        return sum((int(digit) for digit in str(abs(n))))
    count = sum((1 for num in arr if sum_digits(num) > 0))
    return sorted(arr, reverse=count % 2 == 0)