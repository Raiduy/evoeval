def vampires_in_matrix(m: list):
    vampires = set()
    humans = set()
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 2:
                vampires.add((i, j))
            elif m[i][j] == 1:
                humans.add((i, j))
    in_danger = 0
    for human in humans:
        if any((vampire[0] == human[0] or vampire[1] == human[1] for vampire in vampires)):
            in_danger += 1
    return in_danger