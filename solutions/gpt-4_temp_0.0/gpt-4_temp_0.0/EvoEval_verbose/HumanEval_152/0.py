
def compare(game, guess):
    differences = []
    for (actual, predicted) in zip(game, guess):
        difference = abs(actual - predicted)
        differences.append(difference)
    return differences