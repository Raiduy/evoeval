def alien_language_translator(english_word: str):
    """
    Assume there is an alien language where each English alphabet is replaced by a unique symbol. 
    In this language, the symbol for 'a' is '+', 'b' is '-', 'c' is '*', 'd' is '/', 'e' is '%', 'f' is '@', 'g' is '!',
    'h' is '#', 'i' is '$', 'j' is '^', 'k' is '&', 'l' is '(', 'm' is ')', 'n' is '=', 'o' is '?', 'p' is ':',
    'q' is ';', 'r' is '`', 's' is '~', 't' is '>', 'u' is '<', 'v' is '{', 'w' is '}', 'x' is '[', 'y' is ']', 'z' is '|'.
    Write a function that translates an English word into this alien language.

    >>> alien_language_translator("hello")
    '#%((?'

    >>> alien_language_translator("alien")
    '+($%='
    """
    alien_dict = {'a': '+', 'b': '-', 'c': '*', 'd': '/', 'e': '%', 'f': '@', 'g': '!', 'h': '#', 'i': '$', 'j': '^', 'k': '&', 'l': '(', 'm': ')', 'n': '=', 'o': '?', 'p': ':', 'q': ';', 'r': '`', 's': '~', 't': '>', 'u': '<', 'v': '{', 'w': '}', 'x': '[', 'y': ']', 'z': '|'}
    alien_word = ''
    for char in english_word:
        alien_word += alien_dict[char]
    return alien_word