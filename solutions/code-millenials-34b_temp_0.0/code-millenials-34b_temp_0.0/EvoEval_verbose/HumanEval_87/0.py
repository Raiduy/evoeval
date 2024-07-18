
def get_row(lst, x):
    coordinates = []
    for (row_index, row) in enumerate(lst):
        for (column_index, element) in enumerate(row):
            if element == x:
                coordinates.append((row_index, column_index))
    coordinates.sort(key=lambda a: (a[0], -a[1]))
    return coordinates