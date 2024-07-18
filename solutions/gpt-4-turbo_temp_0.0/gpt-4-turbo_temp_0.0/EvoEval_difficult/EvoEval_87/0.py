def get_row(lst, x, y):
    coordinates = []
    for (i, row) in enumerate(lst):
        for (j, col) in enumerate(row):
            for (k, depth) in enumerate(col):
                if depth == x and k != y:
                    coordinates.append((i, -j, k))
    sorted_coordinates = sorted(coordinates, key=lambda coord: (coord[0], coord[1], coord[2]))
    final_coordinates = [(i, -j, k) for (i, j, k) in sorted_coordinates]
    return final_coordinates