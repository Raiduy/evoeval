def check_vowel(s):
    """
    Given a character s, returns True if it's a vowel, False otherwise.
    
    For example:
    check_vowel('a') returns True
    check_vowel('b') returns False
    """
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return s in vowel_list
def frequency_count(s):
    """
    Given a string s, count the frequency of each vowel (case-insensitive) in the string. Return the results as a dictionary.

    For example:
    frequency_count('hello world') returns {'e': 1, 'o': 2}
    frequency_count('Python is cool') returns {'o': 3, 'i': 1}
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s.lower()
    freq_dict = {vowel: s.count(vowel) for vowel in vowels if s.count(vowel) > 0}
    return freq_dict