def treasure_hunt(grid, bag_capacity):
    import math
    total_treasures = 0
    total_trips = 0
    for row in grid:
        total_treasures += sum(row)
    if total_treasures == 0:
        return 0
    else:
        total_trips = math.ceil(total_treasures / bag_capacity)
        return total_trips * 2