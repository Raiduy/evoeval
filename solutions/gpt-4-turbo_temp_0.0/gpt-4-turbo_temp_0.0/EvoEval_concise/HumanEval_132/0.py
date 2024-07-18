
def is_nested(string):
    open_brackets = 0
    valid_nesting_found = False
    for char in string:
        if char == '[':
            open_brackets += 1
        elif char == ']':
            if open_brackets > 0:
                open_brackets -= 1
                valid_nesting_found = True
            else:
                return False
    return valid_nesting_found and open_brackets == 0