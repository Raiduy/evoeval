def str_to_morse_code(s):
    morse_code_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
    words = s.split(' ')
    morse_code = []
    for word in words:
        morse_word = []
        for letter in word:
            morse_word.append(morse_code_dict[letter])
        morse_code.append(' '.join(morse_word))
    return ' / '.join(morse_code)