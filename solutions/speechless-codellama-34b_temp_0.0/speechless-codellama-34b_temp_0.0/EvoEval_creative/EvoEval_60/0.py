def happy_ants(path_length, sugar_locations, ant_positions):
    happy_ants = []
    for ant in ant_positions:
        position = ant[0]
        direction = ant[1]
        sugar_count = 0
        while True:
            if position in sugar_locations:
                sugar_count += 1
                sugar_locations.remove(position)
            if position == path_length - 1 and direction == 'right':
                happy_ants.append(sugar_count)
                break
            elif position == 0 and direction == 'left':
                happy_ants.append(sugar_count)
                break
            if direction == 'right':
                position += 1
            else:
                position -= 1
    return len(happy_ants)