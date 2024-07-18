
def string_to_md5(text):
    """
    Converts a string 'text' to its md5 hash. Returns None for an empty string.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()