def validate_email_structure(email: str) -> bool:
    """
    email is a string.
    return True if the email has a valid format (i.e., there is exactly one "@" character that is not the first or last character
    and there is at least one "." character after the "@" character).
    """
    if email.count('@') != 1:
        return False
    if email[0] == '@' or email[-1] == '@':
        return False
    if email.find('@') == len(email) - 1:
        return False
    if email.find('.') < email.find('@'):
        return False
    return True