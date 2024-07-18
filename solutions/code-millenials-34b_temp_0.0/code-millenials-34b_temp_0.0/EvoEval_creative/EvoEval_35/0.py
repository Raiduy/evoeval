def validate_email_structure(email: str):
    if email[0] == '@' or email[-1] == '@' or '@' not in email:
        return False
    else:
        split_email = email.split('@')
        if len(split_email) != 2 or '.' not in split_email[1]:
            return False
    return True