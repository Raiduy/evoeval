def happy_ants(path_length, sugar_locations, ant_positions):
    sugar_pieces = [False] * path_length
    for location in sugar_locations:
        sugar_pieces[location] = True
    ants = [False] * path_length
    for ant in ant_positions:
        if ant[1] == 'right':
            ants[ant[0]] = True
        else:
            ants[path_length - ant[0] - 1] = True
    happy_ants = 0
    for i in range(path_length):
        if ants[i] and sugar_pieces[i]:
            happy_ants += 1
            sugar_pieces[i] = False
    return happy_ants