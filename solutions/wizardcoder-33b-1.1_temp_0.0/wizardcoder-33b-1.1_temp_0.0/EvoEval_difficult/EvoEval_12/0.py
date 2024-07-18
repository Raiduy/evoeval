from typing import List, Optional, Tuple


def longest_substring(strings: List[str]) -> Tuple[Optional[str], Optional[int]]:
    vowels = 'aeiouAEIOU'
    longest_substring = None
    longest_substring_index = None
    longest_substring_length = 0
    for (i, string) in enumerate(strings):
        for j in range(len(string)):
            if string[j] in vowels:
                for k in range(j + 1, len(string) + 1):
                    if k - j > longest_substring_length:
                        longest_substring = string[j:k]
                        longest_substring_index = i
                        longest_substring_length = k - j
    return (longest_substring, longest_substring_index)