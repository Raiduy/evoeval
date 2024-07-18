from typing import List

def sort_happy_numbers(numbers: str) -> str:
    """ 
    Input is a space-delimited string of numerals from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 
    'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'. This function has two main operations:
    
    1) It checks if the string of numbers is 'happy'. A string is happy if, after removing spaces from the string, every 3 consecutive letters are distinct.
    For instance, 'one two three' is not happy, but 'one one two' is happy. If the string is not happy, return 'Not a happy string'.
    
    2) If the string is happy, it sorts the string with numbers from smallest to largest and returns the sorted string.
    """
    word_to_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    words = numbers.split()
    concatenated = ''.join(words)
    for i in range(len(concatenated) - 2):
        if concatenated[i] == concatenated[i + 1] == concatenated[i + 2]:
            return 'Not a happy string'
    sorted_words = sorted(words, key=lambda word: word_to_num[word])
    return ' '.join(sorted_words)