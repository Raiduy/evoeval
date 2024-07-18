def interstellar_translator(earth_phrase):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    translation = ''
    words = earth_phrase.split(' ')
    for word in words:
        first_letter = word[0]
        new_word = ''
        for letter in word:
            if letter in vowels:
                index = vowels.find(letter)
                if index == len(vowels) - 1:
                    new_word += vowels[0]
                else:
                    new_word += vowels[index + 1]
            elif letter in consonants:
                index = consonants.find(letter)
                if index == len(consonants) - 1:
                    new_word += consonants[0]
                else:
                    new_word += consonants[index + 1]
            elif letter == ' ':
                new_word += '@'
            elif letter == 'z':
                new_word += 'b'
        if first_letter in vowels:
            new_word += 'xy'
        else:
            new_word += 'yz'
        translation += new_word.capitalize() + '@'
    return translation[:-1]