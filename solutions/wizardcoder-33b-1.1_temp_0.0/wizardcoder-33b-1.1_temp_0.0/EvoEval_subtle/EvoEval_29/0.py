
from typing import List


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    return [s for s in strings if s.endswith(suffix)]