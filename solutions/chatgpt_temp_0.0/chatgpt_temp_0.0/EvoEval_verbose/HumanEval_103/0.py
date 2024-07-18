
def rounded_avg(n, m):
    if n > m:
        return -1
    total = 0
    count = 0
    for num in range(n, m + 1):
        total += num
        count += 1
    avg = round(total / count)
    binary = bin(avg)
    return binary