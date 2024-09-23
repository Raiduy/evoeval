
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    # Initialize max_unique_chars to 0 and max_word to empty string
    max_unique_chars = 0
    max_word = ''

    # Sort the words in lexicographical order
    words.sort()

    # Iterate over each word in the list
    for word in words:
        # Count the number of unique characters in the word
        unique_chars = len(set(word))

        # If the number of unique characters is greater than max_unique_chars
        if unique_chars > max_unique_chars:
            # Update max_unique_chars and max_word
            max_unique_chars = unique_chars
 
