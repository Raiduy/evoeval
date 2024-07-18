def flip_case_special(string: str, special_index: int) -> str:
    result = []
    for (i, char) in enumerate(string):
        if i == special_index:
            if char.isupper():
                result.append(char.lower())
            else:
                result.append(char)
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char.upper())
    return ''.join(result)