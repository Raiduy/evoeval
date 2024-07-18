
def max_fill(grid, capacity):
    import math
    total_water = sum((sum(row) for row in grid))
    total_lowerings = math.ceil(total_water / capacity)
    return total_lowerings