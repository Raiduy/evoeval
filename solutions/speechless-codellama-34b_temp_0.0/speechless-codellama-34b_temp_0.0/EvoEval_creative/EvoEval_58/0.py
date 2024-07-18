def interstellar_translator(earth_phrase):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    alien_phrase = ''
    for word in earth_phrase.split():
        new_word = ''
        for letter in word:
            if letter in vowels:
                new_letter = vowels[(vowels.index(letter) + 1) % len(vowels)]
            elif letter == 'z':
                new_letter = 'b'
            else:
                new_letter = consonants[(consonants.index(letter) + 1) % len(consonants)]
            new_word += new_letter
        if word[0] in vowels:
            new_word += 'xy'
        else:
            new_word += 'yz'
        new_word = new_word.capitalize()
        alien_phrase += new_word + '@'
    return alien_phrase[:-1]