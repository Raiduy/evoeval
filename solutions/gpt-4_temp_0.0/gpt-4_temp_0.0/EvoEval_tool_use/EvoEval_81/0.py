def has_uppercase(password):
    """Checks if password contains at least one uppercase letter"""
    return any(char.isupper() for char in password)

def has_lowercase(password):
    """Checks if password contains at least one lowercase letter"""
    return any(char.islower() for char in password)

def has_digit(password):
    """Checks if password contains at least one digit"""
    return any(char.isdigit() for char in password)

def has_special_char(password):
    """Checks if password contains at least one special character"""
    special_chars = "!@#$%^&*"
    return any(char in special_chars for char in password)
def is_valid_password(password):
    """Checks if password is secure"""
    if len(password) < 8:
        return False
    if not has_uppercase(password):
        return False
    if not has_lowercase(password):
        return False
    if not has_digit(password):
        return False
    if not has_special_char(password):
        return False
    return True