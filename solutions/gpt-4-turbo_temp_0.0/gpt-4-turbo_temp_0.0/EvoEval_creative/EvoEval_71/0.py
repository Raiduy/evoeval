def letter_shift_cipher(s, n):
    result = ''
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in s:
        if char.isalpha():
            shift = ord(char) + n
            if char.islower():
                if shift > ord('z'):
                    shift -= 26
                elif shift < ord('a'):
                    shift += 26
            elif char.isupper():
                if shift > ord('Z'):
                    shift -= 26
                elif shift < ord('A'):
                    shift += 26
            result_char = chr(shift)
            result += result_char
            if result_char.lower() in vowels:
                vowel_count += 1
        else:
            result += char
    return (result, vowel_count)