
def check_if_last_char_is_a_letter(txt):
    if not txt or txt.split()[-1] == '':
        return False
    elif txt.split()[-1][-1].isalpha():
        return True
    else:
        return False