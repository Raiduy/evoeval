def valid_moves(board, player):
    """This function determines the valid moves a player can make on a given tic-tac-toe board.
       A valid move is defined as one where the chosen cell of the board is not already occupied.

       Params:
       board - A 2D list of strings representing the game state.
       player - A string representing the current player ("X" or "O").
       
       Returns:
       A list of tuples, where each tuple represents the coordinates (i, j) of a valid move."
    """
    valid_moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                valid_moves.append((i,j))
    return valid_moves
def count_winning_moves(board, player):

    def is_winning(board, player):
        for row in board:
            if all((cell == player for cell in row)):
                return True
        for col in zip(*board):
            if all((cell == player for cell in col)):
                return True
        if all((board[i][i] == player for i in range(len(board)))):
            return True
        if all((board[i][len(board) - i - 1] == player for i in range(len(board)))):
            return True
        return False
    if is_winning(board, player):
        return -1
    winning_moves = 0
    for move in valid_moves(board, player):
        board_copy = [row.copy() for row in board]
        board_copy[move[0]][move[1]] = player
        if is_winning(board_copy, player):
            winning_moves += 1
    return winning_moves