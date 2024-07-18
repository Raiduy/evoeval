def alien_language_translator(english_word: str) -> str:
    """
    Translates an English word into an alien language based on predefined symbol mappings.
    """
    alien_language_dict = {'a': '+', 'b': '-', 'c': '*', 'd': '/', 'e': '%', 'f': '@', 'g': '!', 'h': '#', 'i': '$', 'j': '^', 'k': '&', 'l': '(', 'm': ')', 'n': '=', 'o': '?', 'p': ':', 'q': ';', 'r': '`', 's': '~', 't': '>', 'u': '<', 'v': '{', 'w': '}', 'x': '[', 'y': ']', 'z': '|'}
    alien_word = ''.join((alien_language_dict[char] for char in english_word.lower()))
    return alien_word