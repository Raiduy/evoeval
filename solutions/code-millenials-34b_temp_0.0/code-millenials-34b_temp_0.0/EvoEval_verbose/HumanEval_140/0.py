
def fix_spaces(text):
    result = ''
    consecutive_spaces = 0
    for char in text:
        if char != ' ':
            if consecutive_spaces == 0:
                result += char
            else:
                result += '-'
                consecutive_spaces = 0
        else:
            consecutive_spaces += 1
    return result.replace(' ', '_')