
def get_row(lst, x):
    """
    This function is designed to work with a two-dimensional data structure, more specifically, a list of lists. This structure could be compared to a matrix, but with one significant difference. Unlike in a standard matrix, in this list of lists each row (i.e., each nested list) can have a different number of columns (i.e., a different number of elements).

    The function takes in two parameters. The first parameter, 'lst', is your two-dimensional data structure (the list of lists). The second parameter, 'x', is an integer. The function's job is to find all occurrences of this integer 'x' within the list of lists, and return their coordinates.

    A coordinate is represented as a tuple, with the first element being the row index, and the second element being the column index. The indexing starts from 0, meaning that the first row and the first column are represented as 0. Therefore, a coordinate of (1, 2) refers to the second row, third column.

    The function will return a list of such coordinates, with one tuple for each occurrence of the integer 'x' in the list of lists. If 'x' is not found in the list of lists, the function will return an empty list.

    The function also puts some effort into sorting the returned coordinates. First, it sorts the coordinates by the row index in ascending order. This means that coordinates for smaller rows (i.e., those further to the top) appear before larger rows (those further to the bottom). Within each row, it sorts the coordinates by the column index in descending order. This means that if 'x' appears multiple times in the same row, the coordinates for the rightmost appearances will appear before the leftmost ones.

    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    coordinates = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coordinates.append((i, j))
    return sorted(coordinates, key=lambda x: (x[0], -x[1]))