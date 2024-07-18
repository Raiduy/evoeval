def happy_ants(path_length, sugar_locations, ant_positions):
    sugar_set = set(sugar_locations)
    happy_count = 0
    for (position, direction) in ant_positions:
        if direction == 'right':
            for i in range(position, path_length):
                if i in sugar_set:
                    happy_count += 1
                    break
        else:
            for i in range(position, -1, -1):
                if i in sugar_set:
                    happy_count += 1
                    break
    return happy_count