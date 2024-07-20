def validate_email_structure(email: str) -> bool:
    if email.count('@') == 1 and email[0] != '@' and (email[-1] != '@'):
        at_index = email.index('@')
        if '.' in email[at_index:]:
            return True
    return False