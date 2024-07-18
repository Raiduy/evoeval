
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """This function, vowels_count, accepts a string s, representing a word and returns the number of vowels in it. 
    The vowels are 'a', 'e', 'i', 'o', 'u' and 'y' (only if it's at the end of the word).

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in s.lower():
        if char in vowels:
            count += 1
    if s[-1].lower() == 'y':
        count += 1
    return count