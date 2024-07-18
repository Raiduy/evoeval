
def compare(game, guess):
    """
    This function compares the actual and predicted scores on a match-by-match basis.

    Parameters:
    game (list): A list of actual scores.
    guess (list): A list of predicted scores.

    Returns:
    list: A list of differences between the actual and predicted scores.

    Examples:
    >>> compare([1,2,3,4,5,1],[1,2,3,4,2,-2])
    [0, 0, 0, 0, 3, 3]
    >>> compare([0,5,0,0,0,4],[4,1,1,0,0,-2])
    [4, 4, 1, 0, 0, 6]
    """
    return [abs(g - gs) for (g, gs) in zip(game, guess)]