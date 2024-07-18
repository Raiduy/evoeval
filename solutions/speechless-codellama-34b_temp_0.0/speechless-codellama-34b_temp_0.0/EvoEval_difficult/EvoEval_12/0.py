from typing import List, Optional, Tuple


def longest_substring(strings: List[str]) -> Tuple[Optional[str], Optional[int]]:
    if not strings:
        return (None, None)
    vowels = set('aeiouAEIOU')
    longest_substring = ''
    longest_substring_index = -1
    for (i, string) in enumerate(strings):
        current_substring = ''
        for char in string:
            if char in vowels:
                current_substring += char
            elif current_substring:
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
                    longest_substring_index = i
                current_substring = ''
    if longest_substring:
        return (longest_substring, longest_substring_index)
    else:
        return (None, None)