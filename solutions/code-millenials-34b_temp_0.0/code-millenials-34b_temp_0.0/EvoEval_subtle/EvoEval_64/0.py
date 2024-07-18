FIX = """
Add more test cases.
"""

def vowels_count(s):
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s = s.lower()
    for char in s:
        if char in vowels:
            count += 1
    if s[-1] == 'y':
        count += 1
    return count