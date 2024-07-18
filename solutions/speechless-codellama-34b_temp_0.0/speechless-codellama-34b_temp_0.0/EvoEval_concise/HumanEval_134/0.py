
def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    last_char = txt[-1]
    if not last_char.isalpha():
        return False
    if txt.endswith(' '):
        return False
    if txt.count(' ') == 0:
        return True
    words = txt.split(' ')
    last_word = words[-1]
    if len(last_word) == 1:
        return True
    return False