from typing import List
import re

def check_valid_phone_number(phone_number: str) -> bool:
    """
    Helper function to check if a given phone number is valid.
    A valid phone number has the format xxx-xxx-xxxx

    Args:
    phone_number (str): The phone number to check.

    Returns:
    bool: True if the phone number is valid, False otherwise.
    """
    pattern = "^(\d{3})-(\d{3})-(\d{4})$"
    if re.match(pattern, phone_number):
        return True
    return False
def retrieve_info_from_text(text: str) -> List[str]:
    """
    Given a string of text, your goal is to find and return a list of all valid phone numbers in the text.
    A valid phone number has the format xxx-xxx-xxxx.
    If there are no valid phone numbers in the text, return an empty list.

    Args:
    text (str): The text to parse.

    Returns:
    List[str]: A list of valid phone numbers.

    >>> retrieve_info_from_text('My phone number is 123-456-7890.')
    ['123-456-7890']

    >>> retrieve_info_from_text('My phone number is 123-456-7890 and office number is 987-654-3210')
    ['123-456-7890', '987-654-3210']

    >>> retrieve_info_from_text('This text has no phone numbers.')
    []
    """
    pattern = '(\\d{3}-\\d{3}-\\d{4})'
    phone_numbers = re.findall(pattern, text)
    return phone_numbers