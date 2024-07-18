
def check_if_last_char_is_a_letter(txt):
    # Check if the string is empty or ends with a space, return False
    if not txt or txt.endswith(' '):
        return False
    
    # Check if the last character is an alphabetical character
    return txt[-1].isalpha()
