def adventure_game(map, instructions):
    start_row = 0
    start_column = 0
    path = [(start_row, start_column)]
    for instruction in instructions:
        if instruction == 'up':
            start_row -= 1
        elif instruction == 'down':
            start_row += 1
        elif instruction == 'left':
            start_column -= 1
        elif instruction == 'right':
            start_column += 1
        if start_row < 0 or start_row >= len(map) or start_column < 0 or (start_column >= len(map[0])):
            start_row -= 1
            start_column -= 1
            continue
        if map[start_row][start_column] == 'X':
            start_row -= 1
            start_column -= 1
            continue
        if map[start_row][start_column] == 'E':
            break
        path.append((start_row, start_column))
    return path