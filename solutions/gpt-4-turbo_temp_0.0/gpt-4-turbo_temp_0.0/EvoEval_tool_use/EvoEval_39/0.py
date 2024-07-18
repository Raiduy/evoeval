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
    max_length = 0
    longest_substring = ''
    current_substring = ''
    for char in s:
        if not current_substring or char >= current_substring[-1]:
            current_substring += char
        else:
            if len(current_substring) > max_length:
                max_length = len(current_substring)
                longest_substring = current_substring
            current_substring = char
    if len(current_substring) > max_length:
        longest_substring = current_substring
    return longest_substring