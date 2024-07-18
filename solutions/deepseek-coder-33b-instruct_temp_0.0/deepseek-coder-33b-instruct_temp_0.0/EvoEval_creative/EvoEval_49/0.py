def morse_decoder(msg):
    MORSE_CODE_DICT = {'A': '01', 'B': '1000', 'C': '1010', 'D': '100', 'E': '0', 'F': '0010', 'G': '110', 'H': '0000', 'I': '00', 'J': '0111', 'K': '101', 'L': '0100', 'M': '11', 'N': '10', 'O': '111', 'P': '0110', 'Q': '1101', 'R': '010', 'S': '000', 'T': '1', 'U': '001', 'V': '0001', 'W': '011', 'X': '1001', 'Y': '1011', 'Z': '1100', '1': '01111', '2': '00111', '3': '00011', '4': '00001', '5': '00000', '6': '10000', '7': '11000', '8': '11100', '9': '11110', '0': '11111'}
    REVERSE_MORSE_CODE_DICT = {v: k for (k, v) in MORSE_CODE_DICT.items()}
    words = msg.split('/')
    decoded_words = []
    for word in words:
        chars = word.split(' ')
        decoded_chars = []
        for char in chars:
            decoded_chars.append(REVERSE_MORSE_CODE_DICT[char])
        decoded_word = ''.join(decoded_chars)
        decoded_words.append(decoded_word)
    decoded_msg = ' '.join(decoded_words)
    return decoded_msg