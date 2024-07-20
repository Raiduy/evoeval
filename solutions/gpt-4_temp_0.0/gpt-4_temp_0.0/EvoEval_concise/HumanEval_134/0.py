
def check_if_last_char_is_a_letter(txt):
    """
    Construct a function that returns True if the last character of the
    input string is an alphabetical character that is not part of a word,
    otherwise it returns False. A "word" is defined as a group of characters
    separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    """
    if not txt:
        return False
    last_char = txt[-1]
    if last_char.isalpha():
        if len(txt) == 1 or txt[-2] == ' ':
            return True
    return False