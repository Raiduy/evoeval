def morse_decoder(msg):
    morse_code_dict = {'01': 'A', '1000': 'B', '1010': 'C', '100': 'D', '0': 'E', '0010': 'F', '110': 'G', '0000': 'H', '00': 'I', '0111': 'J', '101': 'K', '0100': 'L', '11': 'M', '10': 'N', '111': 'O', '0110': 'P', '1101': 'Q', '010': 'R', '000': 'S', '1': 'T', '001': 'U', '0001': 'V', '011': 'W', '1001': 'X', '1011': 'Y', '1100': 'Z', '01111': '1', '00111': '2', '00011': '3', '00001': '4', '00000': '5', '10000': '6', '11000': '7', '11100': '8', '11110': '9', '11111': '0'}
    words = msg.split('/')
    decoded_message = []
    for word in words:
        decoded_word = []
        characters = word.strip().split(' ')
        for char in characters:
            if char in morse_code_dict:
                decoded_word.append(morse_code_dict[char])
        decoded_message.append(''.join(decoded_word))
    return ' '.join(decoded_message)