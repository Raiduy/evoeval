
def max_fill(grid, capacity):
    total_water = 0
    for row in grid:
        total_water += sum(row)
    if total_water % capacity == 0:
        return total_water // capacity
    else:
        return total_water // capacity + 1