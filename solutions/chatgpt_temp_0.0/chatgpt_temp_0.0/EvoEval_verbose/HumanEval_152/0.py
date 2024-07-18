
def compare(game, guess):
    """
    This function is designed to simulate the experience of anticipating the results of a series of events (like matches in a 
    game) and then comparing the actual outcomes with the predictions made. In a more specific context, the function aims to 
    assess the accuracy of a person's ability to predict the results of a series of matches.

    The function takes two inputs: an array of actual scores ('game') and an array of predicted scores ('guess'). Both arrays 
    are of the same length, with each index corresponding to a specific match. The function then compares the actual and 
    predicted scores on a match-by-match basis.

    The output of the function is another array of the same length, where each element denotes the difference between the actual 
    and predicted score for the corresponding match. If the prediction was accurate (i.e., the predicted score matches the 
    actual score), the output value is 0. If the prediction was not accurate, the output value is the absolute difference 
    between the predicted and actual score. This way, the output array provides a measure of the accuracy of the predictions.

    Examples:

    If the input is compare([1,2,3,4,5,1],[1,2,3,4,2,-2]), the function should return [0,0,0,0,3,3]. This is because the 
    predicted scores for the first four matches were accurate (hence the 0s), but the predictions for the last two matches 
    were off by 3 (5-2 and 1-(-2), respectively).

    If the input is compare([0,5,0,0,0,4],[4,1,1,0,0,-2]), the function should return [4,4,1,0,0,6]. This is because the 
    predicted score for the first match was 4 points too high, the predicted score for the second match was 4 points too low, 
    the predicted score for the third match was 1 point too high, the predictions for the fourth and fifth matches were 
    accurate, and the predicted score for the last match was 6 points too low.
    """
    differences = []
    for i in range(len(game)):
        difference = abs(game[i] - guess[i])
        differences.append(difference)
    return differences