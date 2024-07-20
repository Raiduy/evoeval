from typing import List, Tuple

def split_by_delimiter(text: str, delimiter: str) -> List[str]:
    """
    This helper function splits the given input string by a specified delimiter and returns a list of the resulting substrings.
    """
    return text.split(delimiter)


def is_integer(text: str) -> bool:
    """
    This helper function checks if the given input string can be converted into an integer.
    """
    try:
        int(text)
        return True
    except ValueError:
        return False
from typing import List, Tuple

def process_records(records: List[str]) -> List[Tuple[int, str]]:
    processed_records = []
    for record in records:
        parts = split_by_delimiter(record, '-')
        if len(parts) == 2 and is_integer(parts[0]):
            processed_records.append((int(parts[0]), parts[1]))
    return processed_records