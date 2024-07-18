def string_transform(s):
    """Transforms the input string according to specified rules."""
    vowel_map = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}
    consonant_map = {chr(i): chr((i - 98) % 26 + 97) for i in range(98, 123)}
    consonant_map['z'] = 'b'

    def transform_char(c):
        if c.lower() in vowel_map:
            return vowel_map[c.lower()].upper() if c.isupper() else vowel_map[c.lower()]
        elif c.lower() in consonant_map:
            return consonant_map[c.lower()].upper() if c.isupper() else consonant_map[c.lower()]
        else:
            return c
    transformed_string = ''.join((transform_char(c) for c in s))
    return transformed_string