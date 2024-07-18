
from typing import List

def md5_substring_filter(strings: List[str], hash_substring: str) -> List[str]:
    if not strings:
        return None
    filtered_strings = []
    for string in strings:
        if string != '' and hashlib.md5(string.encode()).hexdigest().find(hash_substring) != -1:
            filtered_strings.append(string)
    return filtered_strings