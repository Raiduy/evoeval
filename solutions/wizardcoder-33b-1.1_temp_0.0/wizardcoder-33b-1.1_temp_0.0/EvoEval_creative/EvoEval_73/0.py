def treasure_hunt(grid, bag_capacity):
    trips = 0
    treasures = 0
    for row in grid:
        for cell in row:
            if cell == 1:
                treasures += 1
    if treasures == 0:
        return 0
    trips += treasures // bag_capacity * 2
    if treasures % bag_capacity != 0:
        trips += 2
    return trips