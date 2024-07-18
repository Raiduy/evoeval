
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():  # Check if the character is an alphabet
            shift = 4
            if char.islower():
                # ord('a') = 97, ord('z') = 122
                # Subtract ord('a') to get a 0-based index, add the shift, then modulo 26 to wrap around, and add ord('a') back to get the new character
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                # Similar to above, but for uppercase letters
                # ord('A') = 65, ord('Z') = 90
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            # If the character is not an alphabet, just add it as it is.
            result += char
    return result
