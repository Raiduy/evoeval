def is_valid_date(date: str) -> bool:
    """
    A helper function that checks if a given date in 'yyyy-mm-dd'
    format is valid. This function assumes non-leap years and all months 
    have 30 days for simplicity.
    """
    year, month, day = map(int, date.split("-"))
    return (1 <= month <= 12) and (1 <= day <= 30)

def is_alphanumeric(password: str) -> bool:
    """
    A helper function that checks if a given password is alphanumeric, i.e., 
    it contains both numbers and letters.
    """
    return any(char.isdigit() for char in password) and any(char.isalpha() for char in password)
def create_user_account(username: str, password: str, date_of_birth: str):
    """
    The function takes a username, password and date of birth as input and
    creates a new user account. The function should ensure the following:

    1) The username should not be empty and should not contain special characters.
    2) The password should be alphanumeric (contains both numbers and letters).
    3) The date of birth should be a valid date in 'yyyy-mm-dd' format. This function assumes non-leap years and all months
    have 30 days for simplicity.

    If any of the above conditions are not met, the function should return
    "Unsuccessful account creation".
    If all conditions are met, the function should return "Successful account creation".
    """
    if not username or not username.isalnum():
        return 'Unsuccessful account creation'
    if not is_alphanumeric(password):
        return 'Unsuccessful account creation'
    if not is_valid_date(date_of_birth):
        return 'Unsuccessful account creation'
    return 'Successful account creation'