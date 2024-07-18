def string_transform(s):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    transformed_sentence = ''
    for char in s:
        if char in vowels:
            if char == 'a':
                transformed_sentence += 'e'
            elif char == 'e':
                transformed_sentence += 'i'
            elif char == 'i':
                transformed_sentence += 'o'
            elif char == 'o':
                transformed_sentence += 'u'
            elif char == 'u':
                transformed_sentence += 'a'
            elif char == 'A':
                transformed_sentence += 'E'
            elif char == 'E':
                transformed_sentence += 'I'
            elif char == 'I':
                transformed_sentence += 'O'
            elif char == 'O':
                transformed_sentence += 'U'
            elif char == 'U':
                transformed_sentence += 'A'
        elif char in consonants:
            if char == 'z':
                transformed_sentence += 'b'
            elif char == 'Z':
                transformed_sentence += 'B'
            else:
                transformed_sentence += chr(ord(char) + 1)
        else:
            transformed_sentence += char
    return transformed_sentence