def magical_transformation(s):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    transformed = ''
    for (i, char) in enumerate(s):
        if char in vowels:
            if char == 'u':
                transformed += 'a' if char.islower() else 'A'
            else:
                transformed += chr(ord(char) + 1) if char.islower() else chr(ord(char) + 1).upper()
        elif char in consonants:
            if char == 'z':
                transformed += 'b' if char.islower() else 'B'
            elif char == 'Z':
                transformed += 'B'
            else:
                transformed += chr(ord(char) + 1) if char.islower() else chr(ord(char) + 1).upper()
        else:
            transformed += char
        if i % 2 == 0 and char == '?':
            transformed = transformed[:-1] + '!' if transformed[-1] == '?' else transformed[:-1] + '?'
    return transformed