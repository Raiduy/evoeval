
def compare(game, guess):
    return [abs(g - s) for g, s in zip(game, guess)]
