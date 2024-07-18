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
    if is_winner(board, player):
        return -1
    winning_moves = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                if is_winner(board, player):
                    winning_moves += 1
                board[i][j] = ' '
    return winning_moves