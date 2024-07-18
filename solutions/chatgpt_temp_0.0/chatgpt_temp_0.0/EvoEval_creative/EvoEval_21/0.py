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

    def search_word(word):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if search_right(i, j, word) or search_left(i, j, word) or search_down(i, j, word) or search_up(i, j, word):
                    return True
        return False

    def search_right(row, col, word):
        if col + len(word) > len(grid):
            return False
        for k in range(len(word)):
            if grid[row][col + k] != word[k]:
                return False
        return True

    def search_left(row, col, word):
        if col - len(word) < -1:
            return False
        for k in range(len(word)):
            if grid[row][col - k] != word[k]:
                return False
        return True

    def search_down(row, col, word):
        if row + len(word) > len(grid):
            return False
        for k in range(len(word)):
            if grid[row + k][col] != word[k]:
                return False
        return True

    def search_up(row, col, word):
        if row - len(word) < -1:
            return False
        for k in range(len(word)):
            if grid[row - k][col] != word[k]:
                return False
        return True
    for word in words:
        if not search_word(word):
            return False
    return True