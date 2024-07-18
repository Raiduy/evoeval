
from typing import List

def md5_substring_filter(strings: List[str], hash_substring: str) -> List[str]:
    if not strings:
        return None
    result = []
    for string in strings:
        if string:
            md5_hash = hashlib.md5(string.encode()).hexdigest()
            if hash_substring in md5_hash:
                result.append(string)
    return result