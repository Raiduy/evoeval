def adventure_game(map, instructions):
    (start_row, start_col) = next(((i, j) for (i, row) in enumerate(map) for (j, val) in enumerate(row) if val == 'S'))
    current_position = (start_row, start_col)
    path = [current_position]
    moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    for instruction in instructions:
        if map[current_position[0]][current_position[1]] == 'E':
            break
        move = moves[instruction]
        new_position = (current_position[0] + move[0], current_position[1] + move[1])
        if 0 <= new_position[0] < len(map) and 0 <= new_position[1] < len(map[0]) and (map[new_position[0]][new_position[1]] != 'X'):
            current_position = new_position
        path.append(current_position)
    return path