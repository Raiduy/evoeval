
def max_fill(grid, capacity):
    import math
    total_water = sum((sum(row) for row in grid))
    bucket_lowers = math.ceil(total_water / capacity)
    return bucket_lowers