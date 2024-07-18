def treasure_hunt(grid, bag_capacity):
    import math
    rows = len(grid)
    cols = len(grid[0])
    total_chests = sum((sum(row) for row in grid))
    if bag_capacity < total_chests:
        return total_chests * 2
    else:
        return rows + cols