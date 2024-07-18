def check_digit_sequence(num_str):
    """
    This is a helper function that checks if a string is a sequence of digits, 
    returning True if it is and False otherwise.
    :param num_str: str  
    :return: bool
    """

    for char in num_str:
        if not char.isdigit():
            return False
    return True
def find_phone_numbers(paragraph):
    """
    This function searches for and returns all phone numbers in a given paragraph.
    A phone number is defined as a sequence of exactly 10 digits.
    """
    phone_number_pattern = '\\b\\d{10}\\b'
    phone_numbers = re.findall(phone_number_pattern, paragraph)
    return phone_numbers