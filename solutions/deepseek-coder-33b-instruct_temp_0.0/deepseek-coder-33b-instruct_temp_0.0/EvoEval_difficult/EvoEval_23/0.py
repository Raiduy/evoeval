def strlen_custom(string: str, ignore_whitespace: bool=False, count_only_alphabets: bool=False) -> int:
    if ignore_whitespace and count_only_alphabets:
        string = ''.join((e for e in string if e.isalpha() and (not e.isspace())))
    elif ignore_whitespace:
        string = ''.join((e for e in string if not e.isspace()))
    elif count_only_alphabets:
        string = ''.join((e for e in string if e.isalpha()))
    return len(string)