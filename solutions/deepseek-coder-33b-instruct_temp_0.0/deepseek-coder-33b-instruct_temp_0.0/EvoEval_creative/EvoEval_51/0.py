def alien_encoding(string, list_of_alphabets):
    if not list_of_alphabets:
        return string
    if not string:
        return ''
    result = ''
    for i in range(len(string)):
        result += list_of_alphabets[i % len(list_of_alphabets)]
    return result