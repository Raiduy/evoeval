
def check_if_last_char_is_a_letter(txt):
    if not txt or txt.endswith(' '):
        return False
    if txt[-1].isalpha():
        if len(txt) == 1 or not txt[-2].isalpha():
            return True
    return False