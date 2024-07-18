
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
    # Split the string into words
    words = test.split()
    
    # Create a dictionary to store the count of each letter
    count_dict = {}
    
    # Iterate over each word in the list
    for word in words:
        # If the letter is already in the dictionary, increment its count
        if word in count_dict:
            count_dict[word] += 1
        # If the letter is not in the dictionary, add it with a count of 1
        else:
            count_dict[word] = 1
    
    # Find the maximum count
    max_count = max(count_dict.values(), default=0)
    
    # Create a new dictionary with only the letters that have the maximum count
    max_count_dict = {k: v for k, v in count_dict.items() if v == max_count}
    
    return max_count_dict
