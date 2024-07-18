

def strlen(string: str) -> int:
    if not isinstance(string, str):
        raise TypeError('The input to this function should be a string.')
    return len(string)