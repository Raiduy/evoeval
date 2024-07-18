
from typing import List


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    return [string for string in strings if string.endswith(suffix)]