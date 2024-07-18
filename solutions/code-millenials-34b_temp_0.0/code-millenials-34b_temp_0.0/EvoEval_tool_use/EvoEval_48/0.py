def is_valid_email(email: str) -> bool:
    """Check if the given string is a valid email address.
    >>> is_valid_email('example@example.com')
    True
    >>> is_valid_email('example.com')
    False
    """
    if '@' in email and '.' in email:
        return True
    else:
        return False

def normalize_email(email: str) -> str:
    """Normalize the given email address by making it lower case.
    >>> normalize_email('Example@Example.Com')
    'example@example.com'
    """
    return email.lower()
def email_to_username(email_list: list) -> dict:
    """Return a dictionary where each key is a valid (contains both '@' and '.'), normalized email address (lower case) from the email_list
    and each value is a username extracted from the email (the part before '@'). 
    If an email is not valid, it should be ignored.

    >>> email_to_username(['Example@Example.Com', 'test@domain.com', 'invalid.email'])
    {'example@example.com': 'Example', 'test@domain.com': 'test'}
    """
    email_dict = {}
    for email in email_list:
        if is_valid_email(email):
            normalized_email = normalize_email(email)
            username = normalized_email.split('@')[0]
            email_dict[normalized_email] = username
    return email_dict