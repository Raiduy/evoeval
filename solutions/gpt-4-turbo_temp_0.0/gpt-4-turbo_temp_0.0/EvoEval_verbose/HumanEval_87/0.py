
def get_row(lst, x):
    coordinates = []
    for (row_idx, row) in enumerate(lst):
        for (col_idx, element) in enumerate(row):
            if element == x:
                coordinates.append((row_idx, col_idx))
    sorted_coordinates = sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))
    return sorted_coordinates