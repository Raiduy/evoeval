def happy_ants(path_length, sugar_locations, ant_positions):
    sugar = [0] * path_length
    for loc in sugar_locations:
        sugar[loc] = 1
    ant_count = len(ant_positions)
    happy_ant_count = 0
    for i in range(ant_count):
        (pos, direction) = ant_positions[i]
        if direction == 'left':
            for j in range(pos, -1, -1):
                if sugar[j] == 1:
                    happy_ant_count += 1
                    sugar[j] = 0
                    break
        else:
            for j in range(pos, path_length):
                if sugar[j] == 1:
                    happy_ant_count += 1
                    sugar[j] = 0
                    break
    return happy_ant_count