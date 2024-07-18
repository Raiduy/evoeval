
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    counts = {}
    max_count = 0
    
    # Split the string into individual letters
    letters = test.split()
    
    # Count the occurrences of each letter
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
            
        # Update the maximum count if necessary
        if counts[letter] > max_count:
            max_count = counts[letter]
    
    # Create a dictionary of letters with the maximum count
    result = {}
    for letter, count in counts.items():
        if count == max_count:
            result[letter] = count
    
    return result
