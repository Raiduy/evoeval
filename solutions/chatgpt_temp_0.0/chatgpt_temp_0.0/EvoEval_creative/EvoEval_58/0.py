def interstellar_translator(earth_phrase):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    translated_phrase = ''
    words = earth_phrase.split()
    for word in words:
        translated_word = word.capitalize()
        for char in translated_word:
            if char in vowels:
                translated_word = translated_word.replace(char, vowels[(vowels.index(char) + 1) % len(vowels)])
            elif char in consonants:
                translated_word = translated_word.replace(char, consonants[(consonants.index(char) + 1) % len(consonants)])
            elif char == ' ':
                translated_word = translated_word.replace(char, '@')
        if word[0] in vowels:
            translated_word += 'xy'
        else:
            translated_word += 'yz'
        translated_phrase += translated_word + ' '
    return translated_phrase.strip()