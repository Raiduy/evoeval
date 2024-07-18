

def remove_vowels(text):
    """
    The function remove_vowels, as the name suggests, is designed to eliminate all vowel characters from a given text string. 

    This function takes a single argument:
    text (str): This is the input string from which vowels are to be removed.

    The function processes the text to remove any of the following vowel characters: 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'. It maintains the other characters as they are including spaces, special characters, and consonants.

    Outputs a new string which excludes all the vowel characters present in the input string.

    Examples:

    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef
ghijklm")
    'bcdf
ghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])