def alien_language_translator(english_word: str):
    alien_dict = {'a': '+', 'b': '-', 'c': '*', 'd': '/', 'e': '%', 'f': '@', 'g': '!', 'h': '#', 'i': '$', 'j': '^', 'k': '&', 'l': '(', 'm': ')', 'n': '=', 'o': '?', 'p': ':', 'q': ';', 'r': '`', 's': '~', 't': '>', 'u': '<', 'v': '{', 'w': '}', 'x': '[', 'y': ']', 'z': '|'}
    alien_word = ''
    for char in english_word:
        if char.isalpha():
            alien_word += alien_dict[char.lower()]
        else:
            alien_word += char
    return alien_word