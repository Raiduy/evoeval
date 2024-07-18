
def remove_consonants(text):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char in vowels or char.isspace()])