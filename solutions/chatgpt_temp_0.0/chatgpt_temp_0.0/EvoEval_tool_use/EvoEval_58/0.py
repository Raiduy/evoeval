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
    """Places a queen ('Q') at the cell board[row][col] if it's a valid location and not attacked by any other queen.
    If placement is successful, it should return True, else False.
    """
    if is_valid_location(board, row, col) and (not is_attacked(board, row, col)):
        board[row][col] = 'Q'
        return True
    return False