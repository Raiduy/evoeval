def count_distinct_characters_substrings(string: str, length: int) -> dict:
    if length > len(string):
        return {}
    result = {}
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        distinct_characters = len(set(substring))
        result[substring] = distinct_characters
    return result