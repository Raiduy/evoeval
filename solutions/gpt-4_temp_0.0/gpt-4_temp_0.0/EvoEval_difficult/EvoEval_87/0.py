def get_row(lst, x, y):
    coordinates = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            for k in range(len(lst[i][j])):
                if lst[i][j][k] == x and k != y:
                    coordinates.append((i, j, k))
    coordinates.sort(key=lambda x: (x[0], -x[1], x[2]))
    return coordinates