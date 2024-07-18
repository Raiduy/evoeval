def adventure_game(map, instructions):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'S':
                pos = [i, j]
                break
    path = [(pos[0], pos[1])]
    for instruction in instructions:
        if instruction == 'up':
            if pos[0] > 0 and map[pos[0] - 1][pos[1]] != 'X':
                pos[0] -= 1
        elif instruction == 'down':
            if pos[0] < len(map) - 1 and map[pos[0] + 1][pos[1]] != 'X':
                pos[0] += 1
        elif instruction == 'left':
            if pos[1] > 0 and map[pos[0]][pos[1] - 1] != 'X':
                pos[1] -= 1
        elif instruction == 'right':
            if pos[1] < len(map[0]) - 1 and map[pos[0]][pos[1] + 1] != 'X':
                pos[1] += 1
        path.append((pos[0], pos[1]))
        if map[pos[0]][pos[1]] == 'E':
            break
    return path