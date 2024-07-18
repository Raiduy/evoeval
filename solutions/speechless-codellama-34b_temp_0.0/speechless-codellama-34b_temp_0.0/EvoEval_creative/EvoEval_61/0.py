def transform_string(s):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    next_vowel = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a', 'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
    prev_consonant = {'b': 'z', 'c': 'b', 'd': 'c', 'f': 'd', 'g': 'f', 'h': 'g', 'j': 'h', 'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'p': 'n', 'q': 'p', 'r': 'q', 's': 'r', 't': 's', 'v': 't', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y', 'B': 'Z', 'C': 'B', 'D': 'C', 'F': 'D', 'G': 'F', 'H': 'G', 'J': 'H', 'K': 'J', 'L': 'K', 'M': 'L', 'N': 'M', 'P': 'N', 'Q': 'P', 'R': 'Q', 'S': 'R', 'T': 'S', 'V': 'T', 'W': 'V', 'X': 'W', 'Y': 'X', 'Z': 'Y'}
    result = []
    for (i, c) in enumerate(s):
        if c.isalpha():
            if i % 2 == 0:
                result.append(c.swapcase())
            elif c in vowels:
                result.append(next_vowel[c])
            else:
                result.append(prev_consonant[c])
        else:
            result.append(c)
    return ''.join(result)