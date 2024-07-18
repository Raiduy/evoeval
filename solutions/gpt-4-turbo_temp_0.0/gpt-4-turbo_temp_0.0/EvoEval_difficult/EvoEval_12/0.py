from typing import List, Optional, Tuple


def longest_substring(strings: List[str]) -> Tuple[Optional[str], Optional[int]]:
    vowels = 'aeiouAEIOU'
    longest = None
    longest_length = 0
    index_of_longest = None
    for (index, string) in enumerate(strings):
        for (i, char) in enumerate(string):
            if char in vowels:
                substring = string[i:]
                for (j, sub_char) in enumerate(substring):
                    if sub_char.lower() not in vowels:
                        substring = substring[:j]
                        break
                if len(substring) > longest_length:
                    longest = substring
                    longest_length = len(substring)
                    index_of_longest = index
                break
    return (longest, index_of_longest)