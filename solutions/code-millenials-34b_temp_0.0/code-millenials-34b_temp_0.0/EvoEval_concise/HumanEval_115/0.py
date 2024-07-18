
def max_fill(grid, capacity):
    import math
    total_wells = sum((sum(row) for row in grid))
    return math.ceil(total_wells / capacity)