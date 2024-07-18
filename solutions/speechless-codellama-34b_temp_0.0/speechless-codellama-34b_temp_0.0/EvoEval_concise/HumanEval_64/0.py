
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
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    if s[-1] == 'y' or s[-1] == 'Y':
        count += 1
    return count