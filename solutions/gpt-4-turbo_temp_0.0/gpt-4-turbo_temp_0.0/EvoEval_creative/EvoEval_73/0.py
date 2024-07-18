def treasure_hunt(grid, bag_capacity):
    import math
    total_treasures = sum((row.count(1) for row in grid))
    if total_treasures == 0:
        return 0
    trips = math.ceil(total_treasures / bag_capacity) * 2
    return trips