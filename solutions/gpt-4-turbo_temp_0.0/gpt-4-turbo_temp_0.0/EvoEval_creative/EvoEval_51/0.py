def alien_encoding(string, list_of_alphabets):
    if not list_of_alphabets:
        return string
    if not string:
        return ''
    encoded_string = ''
    for (i, char) in enumerate(string):
        encoded_char = list_of_alphabets[i % len(list_of_alphabets)]
        encoded_string += encoded_char
    return encoded_string