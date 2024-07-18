def str_to_morse_code(s):
    morse_code_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
    words = s.split()
    morse_words = []
    for word in words:
        morse_letters = [morse_code_dict[letter] for letter in word]
        morse_words.append(' '.join(morse_letters))
    morse_code = ' / '.join(morse_words)
    return morse_code