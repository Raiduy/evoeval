def text_to_morse(text):
    """Converts text to Morse code."""
    morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '  '}
    text = text.upper()
    morse_code = [morse_dict[char] for char in text if char in morse_dict]
    morse_code_str = ' '.join(morse_code).replace('   ', '  ')
    return morse_code_str