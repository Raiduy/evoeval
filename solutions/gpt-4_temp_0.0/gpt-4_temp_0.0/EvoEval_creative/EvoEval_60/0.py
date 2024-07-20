def happy_ants(path_length, sugar_locations, ant_positions):
    happy_ants = 0
    for ant in ant_positions:
        if ant[1] == 'right':
            for sugar in sugar_locations:
                if sugar >= ant[0]:
                    happy_ants += 1
                    break
        else:
            for sugar in sugar_locations:
                if sugar <= ant[0]:
                    happy_ants += 1
                    break
    return happy_ants