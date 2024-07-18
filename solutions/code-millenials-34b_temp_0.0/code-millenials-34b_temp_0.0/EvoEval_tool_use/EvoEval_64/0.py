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
    """Write a function 'find_phone_numbers' which takes a string representing
    a paragraph as input and returns a list of all phone numbers found in the 
    paragraph. A phone number is defined as a string of exactly 10 digits 
    occurring together.

    Example:
    >>> find_phone_numbers("My phone number is 1234567890. Call me tomorrow.")
    ['1234567890']
    >>> find_phone_numbers("I have two phones. Their numbers are 9876543210 and 1234509876.")
    ['9876543210', '1234509876']
    """
    phone_numbers = []
    words = paragraph.split()
    for word in words:
        if check_digit_sequence(word) and len(word) == 10:
            phone_numbers.append(word)
    return phone_numbers