
def double_the_difference(lst):
    if not lst:
        return 0
    else:
        return sum([i**2 for i in lst if isinstance(i, int) and i > 0 and i % 2 != 0])

