
def max_fill(grid, capacity):
    import math
    total_water = sum((row.count(1) for row in grid))
    if total_water == 0:
        return 0
    return math.ceil(total_water / capacity)