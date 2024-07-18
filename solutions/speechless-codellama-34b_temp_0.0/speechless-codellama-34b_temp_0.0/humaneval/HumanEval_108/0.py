
def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            num = -num
        digits = [int(d) for d in str(num)]
        if sum(digits) > 0:
            count += 1
    return count
