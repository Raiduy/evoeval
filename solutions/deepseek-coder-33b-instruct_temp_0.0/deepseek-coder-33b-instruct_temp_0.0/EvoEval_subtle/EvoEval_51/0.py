
def remove_consonants(text):
    """
    remove_consonants is a function that takes string and returns string without consonants.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char in vowels or char.isspace()])