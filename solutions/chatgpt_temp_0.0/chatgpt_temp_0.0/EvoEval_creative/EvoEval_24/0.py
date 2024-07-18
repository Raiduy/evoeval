def alien_language_translator(english_word: str):
    alien_language = {'a': '+', 'b': '-', 'c': '*', 'd': '/', 'e': '%', 'f': '@', 'g': '!', 'h': '#', 'i': '$', 'j': '^', 'k': '&', 'l': '(', 'm': ')', 'n': '=', 'o': '?', 'p': ':', 'q': ';', 'r': '`', 's': '~', 't': '>', 'u': '<', 'v': '{', 'w': '}', 'x': '[', 'y': ']', 'z': '|'}
    translated_word = ''
    for letter in english_word:
        if letter.lower() in alien_language:
            translated_word += alien_language[letter.lower()]
        else:
            translated_word += letter
    return translated_word