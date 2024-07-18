def happy_ants(path_length, sugar_locations, ant_positions):
    sugar_map = {loc: False for loc in sugar_locations}
    happy_ants_count = 0
    for (ant_pos, direction) in ant_positions:
        if ant_pos in sugar_map and (not sugar_map[ant_pos]):
            sugar_map[ant_pos] = True
            happy_ants_count += 1
        if direction == 'right':
            for i in range(ant_pos + 1, path_length):
                if i in sugar_map and (not sugar_map[i]):
                    sugar_map[i] = True
                    happy_ants_count += 1
                else:
                    break
        elif direction == 'left':
            for i in range(ant_pos - 1, -1, -1):
                if i in sugar_map and (not sugar_map[i]):
                    sugar_map[i] = True
                    happy_ants_count += 1
                else:
                    break
    return happy_ants_count