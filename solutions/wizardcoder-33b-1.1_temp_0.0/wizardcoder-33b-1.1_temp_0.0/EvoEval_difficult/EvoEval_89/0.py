def advanced_encrypt(s, n):
    result = ''
    for char in s:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            if n % 2 == 0:
                result += chr((ord(char) - ascii_offset + 2 * n) % 26 + ascii_offset)
            else:
                result += chr((ord(char) - ascii_offset - 2 * n) % 26 + ascii_offset)
        else:
            result += char
    return result