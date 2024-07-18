def advanced_encrypt(s, n):
    result = ''
    for char in s:
        if char.isalpha():
            shift = n * 2
            if char.islower():
                new_char = chr((ord(char) - 97 + shift * (-1 if n % 2 else 1)) % 26 + 97)
            else:
                new_char = chr((ord(char) - 65 + shift * (-1 if n % 2 else 1)) % 26 + 65)
            result += new_char
        else:
            result += char
    return result