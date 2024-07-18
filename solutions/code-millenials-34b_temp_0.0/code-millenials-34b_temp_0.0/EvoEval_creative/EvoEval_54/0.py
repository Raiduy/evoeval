def find_star_map(lst, star):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == star:
                result.append((i, j))
    return result