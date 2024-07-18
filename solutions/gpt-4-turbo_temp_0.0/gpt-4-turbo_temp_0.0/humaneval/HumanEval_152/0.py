
def compare(game, guess):
    """Compares the actual game results with guesses and returns a list indicating how far off each guess was."""
    # Initialize an empty list to store the differences
    differences = []
    
    # Iterate over the pairs of game results and guesses
    for game_score, guess_score in zip(game, guess):
        # Calculate the absolute difference if they are not the same, else 0
        difference = abs(game_score - guess_score) if game_score != guess_score else 0
        # Append the difference to the result list
        differences.append(difference)
    
    # Return the list of differences
    return differences
