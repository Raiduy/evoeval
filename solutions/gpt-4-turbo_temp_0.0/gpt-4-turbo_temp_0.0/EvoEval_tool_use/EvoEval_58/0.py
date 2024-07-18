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
    """Places a queen ('Q') at the cell board[row][col] if it's a valid location. It also checks if by
    placing queen in the cell does not attack any other queen ('Q') already placed on the board. If placement
    is successful, it should return True, else False.
    Queens can attack if they are in the same row or column or placed diagonally from another queen.
    """
    if not is_valid_location(board, row, col):
        return False
    for i in range(len(board)):
        if board[row][i] == 'Q' or board[i][col] == 'Q':
            return False
    for i in range(len(board)):
        row_offset = row - i
        col_offset = col - i
        if 0 <= row + row_offset < len(board) and 0 <= col + col_offset < len(board[0]):
            if board[row + row_offset][col + col_offset] == 'Q':
                return False
        if 0 <= row - row_offset < len(board) and 0 <= col - col_offset < len(board[0]):
            if board[row - row_offset][col - col_offset] == 'Q':
                return False
    for i in range(len(board)):
        row_offset = row - i
        col_offset = col + i
        if 0 <= row + row_offset < len(board) and 0 <= col - col_offset < len(board[0]):
            if board[row + row_offset][col - col_offset] == 'Q':
                return False
        if 0 <= row - row_offset < len(board) and 0 <= col + col_offset < len(board[0]):
            if board[row - row_offset][col + col_offset] == 'Q':
                return False
    board[row][col] = 'Q'
    return True