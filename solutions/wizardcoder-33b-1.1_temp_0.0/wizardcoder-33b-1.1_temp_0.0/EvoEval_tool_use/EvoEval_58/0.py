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
    Queens can attack if they are in the same row or column or placed diagonally from another queen

    Note: The board is represented as a list of lists, where each inner list represents a row in the board.
    The indexing of the board starts from 0, with row=0 representing the top row and col=0 representing the leftmost column.

    >>> place_queen([['','',''],['','',''],['','','']], 2, 2)
    True
    >>> place_queen([['','Q',''],['','',''],['','','']], 0, 1)
    False
    """
    if not is_valid_location(board, row, col):
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'Q':
                if i == row or j == col or abs(i - row) == abs(j - col):
                    return False
    board[row][col] = 'Q'
    return True