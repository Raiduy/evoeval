def split_words(s: str):
    """
    Helper function that splits a string into a list of words.
    """
    return s.split()


def check_alphabet_order(s: str):
    """
    Helper function that checks if a string is in alphabetical order.
    """
    return s == ''.join(sorted(s))
def longest_ordered_substring(s: str):
    """
    Function that takes a string s and returns the longest substring that is in alphabetical order.
    The string s only contains lowercase alphabets and space.
    """
    words = split_words(s)
    ordered_words = [word for word in words if check_alphabet_order(word)]
    if not ordered_words:
        return ''
    return max(ordered_words, key=len)