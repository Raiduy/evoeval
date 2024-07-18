def happy_ants(path_length, sugar_locations, ant_positions):
    sugar_pieces = [0] * path_length
    for location in sugar_locations:
        sugar_pieces[location] += 1
    ants = [0] * path_length
    for (position, direction) in ant_positions:
        if direction == 'right':
            for i in range(position, path_length):
                if sugar_pieces[i] > 0:
                    ants[i] += 1
                    sugar_pieces[i] -= 1
        else:
            for i in range(position, -1, -1):
                if sugar_pieces[i] > 0:
                    ants[i] += 1
                    sugar_pieces[i] -= 1
    return sum(ants)