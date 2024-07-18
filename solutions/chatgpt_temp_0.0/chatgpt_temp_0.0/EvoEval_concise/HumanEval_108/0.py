
def count_nums(arr):
    count = 0
    for num in arr:
        sum_of_digits = sum((int(digit) for digit in str(num)))
        if num < 0:
            sum_of_digits -= int(str(num)[1])
        if sum_of_digits > 0:
            count += 1
    return count