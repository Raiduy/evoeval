def crossword_validator(grid: list, words: list):
    """
    Consider a 2D grid representing a square crossword puzzle. Each cell of the grid contains a single character.

    Determine if all the words from a provided list of words can be found in the grid.
    Words can be found left-to-right (in a row), right-to-left (in a row),
    top-to-bottom down (in a column), and bottom-to-top (in a column).

    We assume that words are only found in contiguous cells and words do not 'wrap' around the grid.

    Note: the grid is a square (N x N) and all words are lowercase.

    Parameters:
    grid: list of list of char - where each char is a lowercase letter.
    words: list of str - where each str is a lowercase word.

    Returns:
    boolean - return True all words are found in the grid, False otherwise.

    >>> crossword_validator([['c', 'a', 't'], ['d', 'o', 'g'], ['d', 'o', 'p']], ['cat', 'dog', 'pop'])
    False
    >>> crossword_validator([['c', 'a', 't'], ['d', 'o', 'g'], ['d', 'o', 'p']], ['cdd', 'dog', 'pod'])
    True
    """
    grid_rows = [''.join(row) for row in grid]
    grid_cols = [''.join(col) for col in zip(*grid)]
    for word in words:
        if not any((word in row for row in grid_rows)) and (not any((word in col for col in grid_cols))):
            return False
    return True