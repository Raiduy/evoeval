from typing import List

def parse_sentence(sentence: str) -> List[str]:
    """ 
    Parses a sentence into a list of words.
    Input is a string which is a valid sentence in English.
    Returns a list of words in the sentence.
    """
    words = sentence.split(" ")
    return words


def is_vowel(letter: str) -> bool:
    """ 
    Checks if a given letter is a vowel.
    Input is a string of one English letter.
    Returns True if the letter is a vowel, False otherwise.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter.lower() in vowels
def vowels_first(sentence: str) -> str:
    """
    Input is a string which is a valid sentence in English.
    The function returns a new sentence with the same words, but sorted such that words starting with a vowel come first.
    Words are sorted in the order of their occurrence in the original sentence.
    >>> vowels_first('The quick brown fox jumps over the lazy dog')
    'over The quick brown fox jumps the lazy dog'
    >>> vowels_first('An apple fell from the tree')
    'An apple fell from the tree'
    """
    words = parse_sentence(sentence)
    vowels = [word for word in words if is_vowel(word[0])]
    consonants = [word for word in words if not is_vowel(word[0])]
    sorted_words = vowels + consonants
    return ' '.join(sorted_words)