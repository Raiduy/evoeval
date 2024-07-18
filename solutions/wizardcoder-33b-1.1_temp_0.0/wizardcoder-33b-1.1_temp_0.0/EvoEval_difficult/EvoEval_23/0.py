def strlen_custom(string: str, ignore_whitespace: bool=False, count_only_alphabets: bool=False) -> int:
    if ignore_whitespace and count_only_alphabets:
        return len([char for char in string if char.isalpha()])
    elif ignore_whitespace:
        return len([char for char in string if not char.isspace()])
    elif count_only_alphabets:
        return len([char for char in string if char.isalpha()])
    else:
        return len(string)