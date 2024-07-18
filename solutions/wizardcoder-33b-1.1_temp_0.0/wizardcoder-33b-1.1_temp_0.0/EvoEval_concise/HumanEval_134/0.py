
def check_if_last_char_is_a_letter(txt):
    words = txt.split()
    if not words:
        return False
    last_word = words[-1]
    return last_word[-1].isalpha()