def cipher_mapping(s, cipher):
    """Given a string 's' and a mapping dictionary 'cipher', your task is to implement 
    a function that returns a new string where each character in 's' has been replaced 
    by its corresponding value in 'cipher'. 
    If a character in 's' does not exist in 'cipher', leave it as it is in the new string.
    If 's' is an empty string, the function should return an empty string.
    """
    new_string = ''
    for char in s:
        if char in cipher:
            new_string += cipher[char]
        else:
            new_string += char
    return new_string