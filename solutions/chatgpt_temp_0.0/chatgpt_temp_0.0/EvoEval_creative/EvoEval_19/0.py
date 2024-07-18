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
    rows = len(m)
    cols = len(m[0]) if rows > 0 else 0
    count = 0
    for i in range(rows):
        for j in range(cols):
            if m[i][j] == 2:
                for k in range(rows):
                    if m[k][j] == 1:
                        count += 1
                for k in range(cols):
                    if m[i][k] == 1:
                        count += 1
    return count