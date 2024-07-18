
def max_fill(grid, capacity):
    total_water = 0
    num_lowers = 0
    for row in grid:
        for well in row:
            if well == 1:
                total_water += 1
    while total_water > 0:
        total_water -= capacity
        num_lowers += 1
    if total_water < 0:
        num_lowers += 1
    return num_lowers