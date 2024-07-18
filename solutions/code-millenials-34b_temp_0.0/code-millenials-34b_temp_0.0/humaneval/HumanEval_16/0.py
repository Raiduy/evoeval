

def count_distinct_characters(string: str) -> int:
    # Convert the string to lower case to ignore case distinctions
    string_lower = string.lower()
    
    # Convert the string to a set to remove duplicate characters
    distinct_chars = set(string_lower)
    
    # Return the number of distinct characters
    return len(distinct_chars)
