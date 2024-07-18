def check_credit_card_format(credit_card_number):
    """This helper function checks if the input credit card number is in the correct format.
    
    A correct format for this function would be exactly 16 digits. Dashes, spaces, or any
    other characters are not considered valid.

    Args:
        credit_card_number (str): A string representing a credit card number.

    Returns:
        bool: True if the input credit card number is in the correct format, False otherwise.
    """
    
    if len(credit_card_number) != 16:
        return False

    if not credit_card_number.isdigit():
        return False

    return True
def process_payments(payment_data):
    """This function processes a list of payments. Each payment is a dictionary with two keys: 'credit_card_number' 
    and 'amount'. 

    The function should output a list of tuples. Each tuple contains two elements, the credit card number 
    and a string representing the status of the payment. If the credit card number is valid and the amount is 
    higher than zero, the status should be 'Processed'. If the credit card number is not valid (A correct format would be exactly 16 digits) or the amount is 
    not higher than zero, the status should be 'Failed'.

    Example:
    process_payments([{'credit_card_number': '1234567812345678', 'amount': 100}, {'credit_card_number': '1234', 'amount': 0}])
    ==> [('1234567812345678', 'Processed'), ('1234', 'Failed')]

    Args:
        payment_data (List[Dict[str, Union[str, int]]]): A list of dictionaries. Each dictionary represents a payment and 
        contains two keys: 'credit_card_number' (str) and 'amount' (int).

    Returns:
        List[Tuple[str, str]]: A list of tuples. Each tuple represents a payment and contains the credit card number and 
        the status of the payment.
    """
    result = []
    for payment in payment_data:
        credit_card_number = payment['credit_card_number']
        amount = payment['amount']
        if check_credit_card_format(credit_card_number) and amount > 0:
            result.append((credit_card_number, 'Processed'))
        else:
            result.append((credit_card_number, 'Failed'))
    return result