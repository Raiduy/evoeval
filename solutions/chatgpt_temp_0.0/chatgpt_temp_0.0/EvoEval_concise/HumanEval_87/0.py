
def get_row(lst, x):
    """
    Given a jagged 2D list 'lst' and an integer 'x', this function finds all occurrences of 'x' in the list. It returns a list of tuples where each tuple represents the coordinates (row, column) of 'x' in the list. The rows start from 0 and are sorted in ascending order. If 'x' occurs multiple times in the same row, the columns are sorted in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    occurrences = []
    for (row_idx, row) in enumerate(lst):
        for (col_idx, val) in sorted(enumerate(row), key=lambda x: x[1], reverse=True):
            if val == x:
                occurrences.append((row_idx, col_idx))
    return sorted(occurrences)