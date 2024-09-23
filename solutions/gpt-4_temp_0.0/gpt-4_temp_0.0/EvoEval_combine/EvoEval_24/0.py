from typing import List

def sort_happy_numbers(numbers: str) -> str:
    """ 
    Input is a space-delimited string of numerals from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 
    'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'. This function has two main operations:
    
    1) It checks if the string of numbers is 'happy'. A string is happy if, after removing spaces from the string, every 3 consecutive letters are distinct.
    For instance, 'one two three' is not happy, but 'one one two' is happy. If the string is not happy, return 'Not a happy string'.
    
    2) If the string is happy, it sorts the string with numbers from smallest to largest and returns the sorted string.
    
    >>> sort_happy_numbers('three one five')
    'Not a happy string'
    
    >>> sort_happy_numbers('three two two')
    'Not a happy string'
    
    >>> sort_happy_numbers('five two eight')
    'two five eight'
    """
    no_spaces = numbers.replace(' ', '')
    for i in range(len(no_spaces) - 2):
        if no_spaces[i] == no_spaces[i + 1] or no_spaces[i] == no_spaces[i + 2] or no_spaces[i + 1] == no_spaces[i + 2]:
            return 'Not a happy string'
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_list = numbers.split()
    num_list.sort(key=lambda x: num_dict[x])
    return ' '.join(num_list)