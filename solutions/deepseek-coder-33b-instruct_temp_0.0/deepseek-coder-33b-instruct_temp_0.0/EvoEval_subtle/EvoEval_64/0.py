FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    Only count the lowercase vowels.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("YACED")
    0
    """
    count = 0
    for char in s:
        if char.lower() in 'aeiou':
            count += 1
        elif char.lower() == 'y' and s.index(char) == len(s) - 1:
            count += 1
    return count