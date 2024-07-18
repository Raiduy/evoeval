def sum_squares(lst):
    total_sum = 0
    for (index, value) in enumerate(lst):
        if index % 3 == 0:
            total_sum += value ** 2
        elif index % 4 == 0:
            total_sum += value ** 3
        else:
            total_sum += value
    return total_sum