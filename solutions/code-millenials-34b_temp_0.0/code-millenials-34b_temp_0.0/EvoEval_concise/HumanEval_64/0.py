
FIX = """
Add more test cases.
"""

def vowels_count(s):
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i in range(len(s)):
        if s[i].lower() in vowels:
            count += 1
            if s[i].lower() == 'y' and i != len(s) - 1:
                count -= 1
    return count