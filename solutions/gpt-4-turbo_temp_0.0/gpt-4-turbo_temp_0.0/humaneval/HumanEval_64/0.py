
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Convert the string to lowercase to make the function case-insensitive
    s = s.lower()
    
    # Count the vowels in the string
    count = sum(1 for char in s if char in 'aeiou')
    
    # Check if the last character is 'y', add 1 to count if true
    if s.endswith('y'):
        count += 1
    
    return count