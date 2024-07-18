
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    # Initialize variables to keep track of the word with the maximum number of unique characters
    max_unique_chars = 0
    result_word = ""
    
    for word in words:
        # Calculate the number of unique characters in the current word
        unique_chars = len(set(word))
        
        # Update the result_word if the current word has more unique characters
        # or the same number but comes first lexicographically
        if unique_chars > max_unique_chars or (unique_chars == max_unique_chars and word < result_word):
            max_unique_chars = unique_chars
            result_word = word
            
    return result_word
