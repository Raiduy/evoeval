def is_valid_email(email: str) -> bool:
    """Checks if the given email is valid. A valid email has the following format:
    local@domain where local and domain are not empty and do not contain any spaces.
    
    Args:
        email (str): The email to check.
        
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    if email.count("@") != 1:
        return False

    local, domain = email.split("@")
    
    if not local or not domain or " " in email:
        return False

    return True


def is_valid_password(password: str) -> bool:
    """Checks if the given password is valid. A valid password has at least 8 characters,
    at least one uppercase letter, at least one lowercase letter and at least one number.
    
    Args:
        password (str): The password to check.
        
    Returns:
        bool: True if the password is valid, False otherwise.
    """
    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    return True
def register_user(email: str, password: str, confirmation: str) -> str:
    """Given an email, a password and a confirmation of the password, register a new user
    into the system.

    A valid email has the following format:
    local@domain where local and domain are not empty and do not contain any spaces.
    A valid password has at least 8 characters,
    at least one uppercase letter, at least one lowercase letter and at least one number.
    The password and its confirmation should be identical.
    If all conditions are met, return "User registered successfully".

    If the email is not valid, return "Invalid email".
    If the password is not valid, return "Invalid password".
    If the password and its confirmation are not identical, return "Password and confirmation do not match".

    Args:
        email (str): The email of the user.
        password (str): The password of the user.
        confirmation (str): The confirmation of the password.

    Returns:
        str: A message indicating the result of the registration.
    """
    if not is_valid_email(email):
        return 'Invalid email'
    if not is_valid_password(password):
        return 'Invalid password'
    if password != confirmation:
        return 'Password and confirmation do not match'
    return 'User registered successfully'