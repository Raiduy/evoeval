
def compare(game, guess):
    """Determine the accuracy of an individual's predictions for a series of match results. 
    Provided are two lists of equal length, the 'game' containing actual scores and 'guess' containing predictions. 
    Return a list where each element is the absolute difference between the corresponding game score and guess. 
    If a guess is accurate, the difference is 0.
    """
    differences = []
    for (game_score, guess_score) in zip(game, guess):
        differences.append(abs(game_score - guess_score))
    return differences