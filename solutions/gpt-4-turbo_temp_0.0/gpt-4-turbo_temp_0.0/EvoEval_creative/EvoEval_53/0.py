def magical_transformation(s):
    vowel_map = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a', 'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
    consonant_map = {chr(i): chr((i - 98) % 26 + 99) for i in range(98, 123)}
    consonant_map.update({chr(i).upper(): chr((i - 66) % 26 + 67) for i in range(66, 91)})
    consonant_map['z'] = 'b'
    consonant_map['Z'] = 'B'

    def transform_char(c, index):
        if c in vowel_map:
            return vowel_map[c]
        elif c.lower() in consonant_map:
            return consonant_map[c]
        elif c == '?' and index % 2 == 0:
            return '!'
        elif c == '!' and index % 2 != 0:
            return '?'
        else:
            return c
    transformed_string = ''.join((transform_char(c, i) for (i, c) in enumerate(s)))
    return transformed_string