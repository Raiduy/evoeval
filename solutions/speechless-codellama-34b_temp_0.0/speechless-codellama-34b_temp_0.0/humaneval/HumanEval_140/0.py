
def fix_spaces(text):
    new_text = ""
    space_count = 0
    for char in text:
        if char == " ":
            space_count += 1
        else:
            if space_count > 2:
                new_text += "-"
            elif space_count == 1:
                new_text += "_"
            elif space_count == 2:
                new_text += "__"
            new_text += char
            space_count = 0
    if space_count > 2:
        new_text += "-"
    elif space_count == 1:
        new_text += "_"
    elif space_count == 2:
        new_text += "__"
    return new_text
