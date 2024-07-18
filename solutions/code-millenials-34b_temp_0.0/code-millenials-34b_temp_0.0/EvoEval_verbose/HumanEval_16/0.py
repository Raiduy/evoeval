

def count_distinct_characters(string: str) -> int:
    string = string.lower()
    distinct_chars = set(string)
    return len(distinct_chars)