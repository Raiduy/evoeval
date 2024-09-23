def interstellar_translator(earth_phrase):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    translated_phrase = ''
    for word in earth_phrase.split():
        translated_word = ''
        for char in word:
            if char in vowels:
                translated_word += vowels[(vowels.index(char) + 1) % len(vowels)]
            elif char in consonants:
                translated_word += consonants[(consonants.index(char) + 1) % len(consonants)]
            else:
                translated_word += '@'
        if word[0] in vowels:
            translated_word += 'xy'
        else:
            translated_word += 'yz'
        translated_phrase += translated_word.capitalize() + ' '
    return translated_phrase.rstrip().replace(' ', '@')