
FIX = """
Add more test cases.
"""

def vowels_count(s):
    count = 0
    for char in s:
        if char.lower() in 'aeiou':
            count += 1
        elif char.lower() == 'y' and s.index(char) == len(s) - 1:
            count += 1
    return count
