def adventure_game(map, instructions):
    (start_row, start_column) = (None, None)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'S':
                (start_row, start_column) = (i, j)
                break
    if start_row is None or start_column is None:
        return []
    path = [(start_row, start_column)]
    (current_row, current_column) = (start_row, start_column)
    for instruction in instructions:
        if instruction == 'up':
            if current_row > 0 and map[current_row - 1][current_column] != 'X':
                current_row -= 1
        elif instruction == 'down':
            if current_row < len(map) - 1 and map[current_row + 1][current_column] != 'X':
                current_row += 1
        elif instruction == 'left':
            if current_column > 0 and map[current_row][current_column - 1] != 'X':
                current_column -= 1
        elif instruction == 'right':
            if current_column < len(map[0]) - 1 and map[current_row][current_column + 1] != 'X':
                current_column += 1
        path.append((current_row, current_column))
        if map[current_row][current_column] == 'E':
            break
    return path