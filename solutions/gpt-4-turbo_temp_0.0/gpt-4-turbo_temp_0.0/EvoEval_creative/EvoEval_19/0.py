def vampires_in_matrix(m: list):
    """
    vampires_in_matrix takes a 2D list of integers as an input,
    where 0 represents an empty cell, 1 represents a human, and 2 represents a vampire.
    The function will return the number of humans that are in danger of being bitten.
    A human is considered in danger if they share a row or a column with a vampire.
    """
    rows = len(m)
    cols = len(m[0]) if rows > 0 else 0
    danger_rows = set()
    danger_cols = set()
    for i in range(rows):
        for j in range(cols):
            if m[i][j] == 2:
                danger_rows.add(i)
                danger_cols.add(j)
    humans_in_danger = 0
    for i in range(rows):
        for j in range(cols):
            if m[i][j] == 1 and (i in danger_rows or j in danger_cols):
                humans_in_danger += 1
    return humans_in_danger