
def find_max(words):
    """A function that takes in a list of words as input and returns the word with the most unique characters.
    If there are multiple words with the same maximum count of unique characters, it returns the word that comes first in alphabetic order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    max_unique_chars = 0
    max_word = ''
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars:
            max_word = min(word, max_word)
    return max_word