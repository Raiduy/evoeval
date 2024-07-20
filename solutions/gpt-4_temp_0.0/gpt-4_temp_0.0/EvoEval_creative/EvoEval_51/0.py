def alien_encoding(string, list_of_alphabets):
    if not string:
        return ''
    if not list_of_alphabets:
        return string
    encoded_string = ''
    for i in range(len(string)):
        encoded_string += list_of_alphabets[i % len(list_of_alphabets)]
    return encoded_string