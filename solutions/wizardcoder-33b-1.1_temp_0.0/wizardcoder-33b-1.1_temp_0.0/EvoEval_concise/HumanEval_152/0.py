
def compare(game, guess):
    """Determine the accuracy of an individual's predictions for a series of match results. 
    Provided are two lists of equal length, the 'game' containing actual scores and 'guess' containing predictions. 
    Return a list where each element is the absolute difference between the corresponding game score and guess. 
    If a guess is accurate, the difference is 0.
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(game[i] - guess[i]) for i in range(len(game))]