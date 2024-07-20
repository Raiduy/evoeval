from typing import List, Optional, Tuple


def longest_substring(strings: List[str]) -> Tuple[Optional[str], Optional[int]]:
    vowels = 'aeiouAEIOU'
    longest_substring = None
    longest_length = 0
    longest_index = None
    for (i, string) in enumerate(strings):
        for j in range(len(string)):
            if string[j] in vowels:
                k = j
                while k < len(string) and string[k] in vowels:
                    k += 1
                if k - j > longest_length:
                    longest_length = k - j
                    longest_substring = string[j:k]
                    longest_index = i
    return (longest_substring, longest_index)