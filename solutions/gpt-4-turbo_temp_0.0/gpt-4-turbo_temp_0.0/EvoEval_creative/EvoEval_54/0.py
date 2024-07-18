def find_star_map(lst, star):
    coordinates = []
    for (row_index, row) in enumerate(lst):
        for (col_index, element) in enumerate(row):
            if element == star:
                coordinates.append((row_index, col_index))
    return coordinates