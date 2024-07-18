def interstellar_translator(earth_phrase):

    def translate_char(c):
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        if c in vowels:
            return vowels[(vowels.index(c) + 1) % len(vowels)]
        elif c in consonants:
            return consonants[(consonants.index(c) + 1) % len(consonants)]
        return c

    def translate_word(word):
        translated_word = ''
        for (i, c) in enumerate(word):
            if i == 0:
                if c in 'aeiou':
                    translated_word += translate_char(c).upper()
                    append_text = 'xy'
                else:
                    translated_word += translate_char(c).upper()
                    append_text = 'yz'
            else:
                translated_word += translate_char(c)
        return translated_word + append_text
    translated_phrase = '@'.join((translate_word(word) for word in earth_phrase.split(' ')))
    return translated_phrase