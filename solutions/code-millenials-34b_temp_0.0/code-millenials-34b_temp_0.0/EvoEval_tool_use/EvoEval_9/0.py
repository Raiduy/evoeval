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
    """
    Given a list of strings where each string is a record in the format "ID-NAME", 
    where ID is an integer and NAME is a string without hyphens, return a list 
    of tuples where each tuple is in the format (ID, NAME). If a record is not 
    in the correct format, it should be ignored.

    >>> process_records(["1-John", "2-Jane", "invalid", "3-Jack"])
    [(1, "John"), (2, "Jane"), (3, "Jack")]
    """
    processed_records = []
    for record in records:
        parts = split_by_delimiter(record, '-')
        if len(parts) == 2 and is_integer(parts[0]) and (not '-' in parts[1]):
            processed_records.append((int(parts[0]), parts[1]))
    return processed_records