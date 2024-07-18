def treasure_hunt(grid, bag_capacity):
    import math
    num_chambers = len(grid)
    num_chests = len(grid[0])
    num_trips = 0
    for i in range(num_chambers):
        for j in range(num_chests):
            if grid[i][j] == 1:
                num_trips += math.ceil((num_chests - j) / bag_capacity) + 1
    return num_trips