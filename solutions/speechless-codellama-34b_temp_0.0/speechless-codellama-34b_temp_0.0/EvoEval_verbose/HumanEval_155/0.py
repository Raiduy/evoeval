
def even_odd_count(num):
    even_count = 0
    odd_count = 0
    num = abs(num)
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)