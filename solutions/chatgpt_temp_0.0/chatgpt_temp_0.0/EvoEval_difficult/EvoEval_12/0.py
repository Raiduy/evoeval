from typing import List, Optional, Tuple


def longest_substring(strings: List[str]) -> Tuple[Optional[str], Optional[int]]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    longest_substring = ''
    longest_substring_index = None
    for (i, string) in enumerate(strings):
        string = string.lower()
        substring = ''
        substring_index = None
        for (j, char) in enumerate(string):
            if char in vowels:
                if substring == '':
                    substring_index = j
                substring += char
            else:
                if substring != '' and len(substring) > len(longest_substring):
                    longest_substring = substring
                    longest_substring_index = i
                substring = ''
        if substring != '' and len(substring) > len(longest_substring):
            longest_substring = substring
            longest_substring_index = i
    if longest_substring == '':
        return (None, None)
    else:
        return (longest_substring, longest_substring_index)