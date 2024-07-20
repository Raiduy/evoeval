def vampires_in_matrix(m: list):
    """
    vampires_in_matrix takes a 2D list of integers as an input,
    where 0 represents an empty cell, 1 represents a human, and 2 represents a vampire.
    The function will return the number of humans that are in danger of being bitten.
    A human is considered in danger if they share a row or a column with a vampire.

    >>> vampires_in_matrix([[0, 1, 0], [2, 0, 1], [1, 1, 0]])
    2
    >>> vampires_in_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    0
    >>> vampires_in_matrix([[1, 2, 1], [1, 1, 1], [2, 1, 1]])
    6
    >>> vampires_in_matrix([[1, 1, 1], [0, 0, 0], [2, 2, 2]])
    3
    >>> vampires_in_matrix([[2]])
    0
    """
    rows_with_vampires = set()
    cols_with_vampires = set()
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 2:
                rows_with_vampires.add(i)
                cols_with_vampires.add(j)
    humans_in_danger = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1 and (i in rows_with_vampires or j in cols_with_vampires):
                humans_in_danger += 1
    return humans_in_danger