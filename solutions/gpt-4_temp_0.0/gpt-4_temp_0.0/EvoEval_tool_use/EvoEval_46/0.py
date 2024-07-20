def is_valid_word(word: str) -> bool:
    """Check if a word contains only alphabets and it's length is more than 1
    Args:
        word (str): The word to check
    
    Returns:
        bool: Returns True if the word contains only alphabets and it's length is more than 1. Else, returns False.
    """
    if not word.isalpha() or len(word) <= 1:
        return False
    return True

def count_vowels(word: str) -> int:
    """Count the number of vowels in a word
    Args:
        word (str): The word to count vowels in
    
    Returns:
        int: The number of vowels in the word
    """
    vowels = 'aeiou'
    return len([char for char in word.lower() if char in vowels])
def word_info(sentence: str) -> dict:
    """The function takes a sentence as input and returns a dictionary containing information about the words in the sentence. 
    Each key in the dictionary is a valid word from the sentence and it's value is a dictionary which has two keys: 'length' 
    and 'vowels'. 'length' stores the length of the word and 'vowels' stores the number of vowels in the word.
    Words are considered valid if they contain only alphabets and their length is more than 1. 
    The function should ignore case while counting vowels.
    The function should ignore punctuation.

    Args:
        sentence (str): The sentence to analyze

    Returns:
        dict: A dictionary containing information about the words in the sentence

    Example:
        >>> word_info("Hello, world!")
        {"Hello": {"length": 5, "vowels": 2}, "world": {"length": 5, "vowels": 1}}
    """
    word_dict = {}
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()
    for word in words:
        if is_valid_word(word):
            word_dict[word] = {'length': len(word), 'vowels': count_vowels(word)}
    return word_dict