def find_star_map(lst, star):
    coordinates = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == star:
                coordinates.append((i, j))
    return coordinates