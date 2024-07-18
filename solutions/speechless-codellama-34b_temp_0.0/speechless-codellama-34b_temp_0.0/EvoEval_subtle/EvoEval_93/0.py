

def encode(message):
    result = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                if char in 'aeiou':
                    result += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
                else:
                    result += char.upper()
            elif char in 'AEIOU':
                result += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            else:
                result += char.lower()
        else:
            result += char
    return result