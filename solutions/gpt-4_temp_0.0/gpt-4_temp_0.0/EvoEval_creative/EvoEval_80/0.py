def adventure_game(map, instructions):
    start_position = [(i, j) for i in range(len(map)) for j in range(len(map[i])) if map[i][j] == 'S'][0]
    path = [start_position]
    current_position = start_position
    moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    for instruction in instructions:
        new_position = (current_position[0] + moves[instruction][0], current_position[1] + moves[instruction][1])
        if 0 <= new_position[0] < len(map) and 0 <= new_position[1] < len(map[0]) and (map[new_position[0]][new_position[1]] != 'X'):
            current_position = new_position
            path.append(current_position)
        if map[current_position[0]][current_position[1]] == 'E':
            break
    return path