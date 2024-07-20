
def count_nums(arr):
    count = 0
    for num in arr:
        if num < 0:
            num = str(num)[1:]
            digits = [-int(num[0])] + [int(d) for d in num[1:]]
        else:
            digits = [int(d) for d in str(num)]
        if sum(digits) > 0:
            count += 1
    return count