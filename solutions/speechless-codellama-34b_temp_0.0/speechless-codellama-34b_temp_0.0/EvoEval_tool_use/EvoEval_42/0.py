def is_valid_phone(phone: str) -> bool:
    """Check whether the given string is a valid phone number.

    A valid phone number contains exactly 10 digits and the total sum of these digits is divisible by 3.

    >>> is_valid_phone("1234567890")
    True
    >>> is_valid_phone("12345")
    False
    >>> is_valid_phone("12345678901")
    False
    """
    if not (len(phone) == 10 and phone.isdigit()):
        return False
    return sum(int(d) for d in phone) % 3 == 0
def find_valid_phones(text: str) -> list:
    """Return list of all valid phone numbers from the given text.

    A valid phone number contains exactly 10 digits and the total sum of these digits must be divisible by 3.

    >>> find_valid_phones("Call me at 1234567890. Also, 9876543210 is a valid number.")
    ['1234567890', '9876543210']
    >>> find_valid_phones("Invalid numbers: 12345, 12345678901.")
    []
    """
    valid_phones = []
    for word in text.split():
        if is_valid_phone(word):
            valid_phones.append(word)
    return valid_phones