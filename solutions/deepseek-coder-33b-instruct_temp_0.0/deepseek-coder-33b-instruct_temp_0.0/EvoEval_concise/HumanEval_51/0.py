

def remove_vowels(text):
    """
    Function to eliminate vowels from a given string.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])