
from typing import List, Any


def filter_even_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int) and value % 2 == 0]