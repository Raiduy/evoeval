
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
    # Split the string into a list of words
    words = test.split()
    
    # Create a dictionary to store the count of each letter
    letter_count = {}
    
    # Iterate over each word in the list
    for word in words:
        # Iterate over each letter in the word
        for letter in word:
            # If the letter is already in the dictionary, increment its count
            if letter in letter_count:
                letter_count[letter] += 1
            # If the letter is not in the dictionary, add it with a count of 1
            else:
                letter_count[letter] = 1
    
    # Find the maximum count
    max_count = max(letter_count.values()) if letter_count else 0
    
    # Create a new dictionary with only the letters that have the maximum count
    max_count_letters = {k: v for k, v in letter_count.items() if v == max_count}
    
    return max_count_letters
