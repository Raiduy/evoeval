def alien_encoding(string, list_of_alphabets):
    if string == '':
        return ''
    if list_of_alphabets == []:
        return string
    encoded_string = ''
    for i in range(len(string)):
        alphabet_index = i % len(list_of_alphabets)
        encoded_string += list_of_alphabets[alphabet_index]
    return encoded_string