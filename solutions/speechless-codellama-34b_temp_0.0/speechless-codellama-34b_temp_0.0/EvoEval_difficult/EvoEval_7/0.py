from typing import List, Optional


def filter_by_substring(strings: List[str], substring: str, start: Optional[int]=None, end: Optional[int]=None) -> List[str]:
    filtered_strings = []
    for string in strings:
        if start is None and end is None:
            if substring in string:
                filtered_strings.append(string)
        elif start is not None and end is None:
            if substring in string[start:]:
                filtered_strings.append(string)
        elif start is None and end is not None:
            if substring in string[:end]:
                filtered_strings.append(string)
        elif substring in string[start:end]:
            filtered_strings.append(string)
    return filtered_strings