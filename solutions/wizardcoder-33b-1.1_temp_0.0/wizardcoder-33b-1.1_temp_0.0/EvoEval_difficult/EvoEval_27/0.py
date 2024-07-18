def flip_case_special(string: str, special_index: int) -> str:
    special_index = special_index % len(string)
    result = ''
    for i in range(len(string)):
        if i == special_index:
            if string[i].isupper():
                result += string[i].lower()
            else:
                result += string[i]
        elif string[i].isupper():
            result += string[i].lower()
        else:
            result += string[i].upper()
    return result