from typing import List, Union

def validate_operation(operation: Union[int, str]) -> bool:
    """
    Helper function to validate the bank operation.
    It checks if the operation is either integer or a valid string operation like 'deposit' or 'withdraw'.
    If the operation is valid, it returns True else False.

    >>> validate_operation(100)
    True
    >>> validate_operation('deposit')
    True
    >>> validate_operation('invalid_operation')
    False
    """
    valid_operations = ['deposit', 'withdraw']
    return isinstance(operation, int) or operation in valid_operations
def process_operations(operations: List[Union[int, str]], amounts: List[int]) -> int:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. The operations list can contain both integers and strings.
    
    - If an integer is encountered, it needs to be added directly to the balance.
    - If a string is encountered, it refers to the operation 'deposit' or 'withdraw'. The corresponding amount for the operation is retrieved from the amounts list (order is maintained). 'deposit' adds to the balance and 'withdraw' subtracts from the balance.
    
    Your task is to perform all the operations and return the final balance of the account.

    >>> process_operations([1, 'deposit', 'withdraw', 5], [200, 100])
    106
    >>> process_operations(['deposit', 2, 'withdraw'], [100, 50])
    52
    """
    balance = 0
    amount_index = 0
    for operation in operations:
        if isinstance(operation, int):
            balance += operation
        elif operation == 'deposit':
            balance += amounts[amount_index]
            amount_index += 1
        elif operation == 'withdraw':
            balance -= amounts[amount_index]
            amount_index += 1
    return balance