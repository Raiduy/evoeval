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
    vampires = []
    humans = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 2:
                vampires.append((i, j))
            elif m[i][j] == 1:
                humans.append((i, j))
    in_danger = 0
    for human in humans:
        for vampire in vampires:
            if human[0] == vampire[0] or human[1] == vampire[1]:
                in_danger += 1
                break
    return in_danger