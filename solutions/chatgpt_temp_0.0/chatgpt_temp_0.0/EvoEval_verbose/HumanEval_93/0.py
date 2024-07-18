
def encode(message):
    encoded_message = ''
    for letter in message:
        if letter.islower():
            encoded_message += letter.upper()
        elif letter.isupper():
            encoded_message += letter.lower()
        else:
            encoded_message += letter
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = list(encoded_message)
    for i in range(len(encoded_message)):
        if encoded_message[i].lower() in vowels:
            encoded_message[i] = chr(ord(encoded_message[i]) + 2)
    return ''.join(encoded_message)