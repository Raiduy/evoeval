def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in descending order.
    Also, sort coordinates of the row by columns in ascending order.
    """
    coordinates = []
    for (i, row) in enumerate(lst):
        for (j, value) in enumerate(row):
            if value == x:
                coordinates.append((i, j))
    coordinates.sort(key=lambda coord: (-coord[0], coord[1]))
    return coordinates