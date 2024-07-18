from typing import List, Optional, Tuple


def longest_substring(strings: List[str]) -> Tuple[Optional[str], Optional[int]]:
    if not strings:
        return (None, None)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_length = 0
    max_index = 0
    max_substring = None
    for (i, string) in enumerate(strings):
        for j in range(len(string)):
            if string[j].lower() in vowels:
                for k in range(j, len(string)):
                    if string[k].lower() not in vowels:
                        if k - j > max_length:
                            max_length = k - j
                            max_index = i
                            max_substring = string[j:k]
                        break
    return (max_substring, max_index if max_substring else None, None)