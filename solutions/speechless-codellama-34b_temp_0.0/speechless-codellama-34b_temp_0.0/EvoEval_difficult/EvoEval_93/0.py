def encode_complex(message, shift, key):
    result = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                if char in 'aeiou':
                    result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    result += key[ord(char) - ord('a')]
            elif char in 'AEIOU':
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += key[ord(char) - ord('A')].upper()
        else:
            result += char
    return result