
def find_max(words):
    """A function that takes in a list of words as input and returns the word with the most unique characters.
    If there are multiple words with the same maximum count of unique characters, it returns the word that comes first in alphabetic order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    unique_counts = [(len(set(word)), word) for word in words]
    unique_counts.sort(key=lambda x: (-x[0], x[1]))
    return unique_counts[0][1]