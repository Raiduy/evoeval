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
    balance = 0
    for (i, operation) in enumerate(operations):
        if isinstance(operation, int):
            balance += operation
        elif operation == 'deposit':
            balance += amounts[i]
        elif operation == 'withdraw':
            balance -= amounts[i]
    return balance