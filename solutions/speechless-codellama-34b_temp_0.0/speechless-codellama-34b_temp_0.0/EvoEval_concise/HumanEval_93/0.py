
def encode(message):
    result = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                if char in 'aeiou':
                    result += chr(ord(char) + 2)
                else:
                    result += char.upper()
            elif char in 'AEIOU':
                result += chr(ord(char) - 2)
            else:
                result += char.lower()
        else:
            result += char
    return result