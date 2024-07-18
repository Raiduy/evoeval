

def sum_squares(lst):
    rounded_nums = [math.ceil(num) for num in lst]
    squared_nums = [num ** 2 for num in rounded_nums]
    return sum(squared_nums)