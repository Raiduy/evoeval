
def double_the_difference(lst):
    sum = 0
    for i in lst:
        if i > 0 and i % 2 != 0:
            sum += i * i
    return sum