def alien_language_translator(english_word: str) -> str:
    alien_dict = {'a': '+', 'b': '-', 'c': '*', 'd': '/', 'e': '%', 'f': '@', 'g': '!', 'h': '#', 'i': '$', 'j': '^', 'k': '&', 'l': '(', 'm': ')', 'n': '=', 'o': '?', 'p': ':', 'q': ';', 'r': '`', 's': '~', 't': '>', 'u': '<', 'v': '{', 'w': '}', 'x': '[', 'y': ']', 'z': '|'}
    return ''.join((alien_dict[char] for char in english_word))