def advanced_encrypt(s, n):
    result = ''
    for char in s:
        if char.isalpha():
            shift = n * 2
            if n % 2 == 0:
                shift = -shift
            if char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result