
def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    last_char = txt.split()[-1][-1]
    return last_char.isalpha()