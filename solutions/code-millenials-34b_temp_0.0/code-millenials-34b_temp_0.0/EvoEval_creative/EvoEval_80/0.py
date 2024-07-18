def adventure_game(map, instructions):
    for i in range(len(map)):
        if 'S' in map[i]:
            (start_row, start_column) = (i, map[i].index('S'))
            break
    path = [(start_row, start_column)]
    movements = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    for instruction in instructions:
        new_row = start_row + movements[instruction][0]
        new_column = start_column + movements[instruction][1]
        if 0 <= new_row < len(map) and 0 <= new_column < len(map[0]) and (map[new_row][new_column] != 'X'):
            (start_row, start_column) = (new_row, new_column)
            path.append((start_row, start_column))
        if map[start_row][start_column] == 'E':
            return path
    return path