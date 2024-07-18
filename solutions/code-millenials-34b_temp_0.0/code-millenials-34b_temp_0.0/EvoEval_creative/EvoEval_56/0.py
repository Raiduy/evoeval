def str_to_morse_code(s):
    morse_code_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
    words = s.split(' ')
    morse_code = ''
    for word in words:
        for char in word:
            morse_code += morse_code_dict[char] + ' '
        morse_code = morse_code[:-1] + '/ '
    return morse_code[:-2]