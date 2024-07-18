

def strlen(string: str) -> int:
    if not isinstance(string, str):
        raise TypeError('Input should be a string')
    return len(string)