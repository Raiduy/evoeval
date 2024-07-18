def flip_case_special(string: str, special_index: int) -> str:
    actual_index = special_index % len(string)
    special_char = string[actual_index]
    if special_char.isupper():
        special_char = special_char.lower()
    flipped_string = ''
    for i in range(len(string)):
        if i == actual_index:
            flipped_string += special_char
        elif string[i].isupper():
            flipped_string += string[i].lower()
        else:
            flipped_string += string[i].upper()
    return flipped_string