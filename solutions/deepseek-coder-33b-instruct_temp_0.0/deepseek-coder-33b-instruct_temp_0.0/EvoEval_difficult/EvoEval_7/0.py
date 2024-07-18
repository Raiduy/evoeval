from typing import List, Optional


def filter_by_substring(strings: List[str], substring: str, start: Optional[int]=None, end: Optional[int]=None) -> List[str]:
    filtered_strings = []
    for string in strings:
        if start is not None and end is not None:
            string_to_check = string[start:end + 1]
        elif start is not None:
            string_to_check = string[start:]
        elif end is not None:
            string_to_check = string[:end + 1]
        else:
            string_to_check = string
        if substring in string_to_check:
            filtered_strings.append(string)
    return filtered_strings