

def sum_squares(lst):
    sum_of_squares = 0
    for i in lst:
        sum_of_squares += math.ceil(i) ** 2
    return sum_of_squares