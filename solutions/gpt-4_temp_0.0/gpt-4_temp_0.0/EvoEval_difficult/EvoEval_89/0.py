def advanced_encrypt(s, n):
    result = ''
    for char in s:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - ascii_offset + n * 2 * (-1 if n % 2 else 1)) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
    return result