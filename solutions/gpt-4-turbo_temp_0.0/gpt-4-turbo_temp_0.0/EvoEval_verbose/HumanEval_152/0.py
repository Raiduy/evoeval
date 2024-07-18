
def compare(game, guess):
    """
    This function compares the actual scores ('game') with the predicted scores ('guess') and returns an array indicating the 
    accuracy of the predictions.
    """
    differences = []
    for (actual, predicted) in zip(game, guess):
        difference = abs(actual - predicted)
        differences.append(difference)
    return differences