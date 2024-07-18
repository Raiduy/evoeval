def validate_email_structure(email: str) -> bool:
    """Validate the structure of an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email address has a valid format, False otherwise.
    """
    if email.count('@') != 1:
        return False
    (local_part, domain_part) = email.split('@')
    if not local_part or not domain_part:
        return False
    if '.' not in domain_part:
        return False
    if domain_part.startswith('.') or domain_part.endswith('.'):
        return False
    return True