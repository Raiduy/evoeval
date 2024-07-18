
def count_nums(arr):
    count = 0
    for num in arr:
        if sum((int(d) for d in str(abs(num)))) > 0:
            count += 1
    return count