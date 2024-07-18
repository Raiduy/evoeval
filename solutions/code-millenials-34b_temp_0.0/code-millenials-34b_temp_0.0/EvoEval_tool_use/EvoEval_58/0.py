def is_valid_location(board: list[list[str]], row: int, col: int) -> bool:
    """ Checks if a cell [row, col] is valid on the board.
    >>> is_valid_location([['','',''],['','',''],['','','']], 1, 1)
    True
    >>> is_valid_location([['','',''],['','',''],['','','']], 3, 3)
    False
    """
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return False
    return True
def place_queen(board: list[list[str]], row: int, col: int) -> bool:
    if not is_valid_location(board, row, col):
        return False
    if 'Q' in board[row]:
        return False
    for i in range(len(board)):
        if 'Q' in board[i]:
            if abs(i - row) == abs(board[i].index('Q') - col):
                return False
    board[row][col] = 'Q'
    return True