from datetime import datetime


def parse_date(date_str: str) -> datetime:
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None
def register_user(user_data: dict) -> bool:
    """Register a new user if the provided user data is valid.
    User data is a dictionary that must contain the following fields:
    - 'name' (string): The user's name
    - 'dob' (string): The user's date of birth in 'YYYY-MM-DD' format
    - 'email' (string): The user's email address

    To validate user data dictionary:
    - Check if necessary fields ('name', 'dob', 'email') exist
    - Check if 'dob' is valid date string
    - Check if 'name' and 'email' are non-empty strings

    If the user data is valid, this function adds the user to the system and returns True.
    If the user data is not valid, this function returns False and does not add the user.

    >>> register_user({'name': 'John Doe', 'dob': '1990-01-01', 'email': 'john.doe@example.com'})
    True

    >>> register_user({'name': '', 'dob': '1990-01-01', 'email': 'john.doe@example.com'})
    False

    >>> register_user({'name': 'John Doe', 'dob': '1990-01-32', 'email': 'john.doe@example.com'})
    False
    """
    if not all((key in user_data for key in ('name', 'dob', 'email'))):
        return False
    if parse_date(user_data['dob']) is None:
        return False
    if not isinstance(user_data['name'], str) or not isinstance(user_data['email'], str) or (not user_data['name']) or (not user_data['email']):
        return False
    print(f"User {user_data['name']} registered successfully.")
    return True