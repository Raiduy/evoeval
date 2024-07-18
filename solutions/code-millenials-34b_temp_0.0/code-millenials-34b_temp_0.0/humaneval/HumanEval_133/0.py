

def sum_squares(lst):
    sum_sq = 0
    for i in lst:
        sum_sq += math.ceil(i) ** 2
    return sum_sq
