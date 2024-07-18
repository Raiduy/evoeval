from typing import List, Tuple, Optional

def account_operations(operations: List[int]) -> Tuple[Optional[int], Optional[int], bool]:
    balance = 0
    largest_withdrawal = None
    smallest_deposit = None
    balance_never_negative = True
    for operation in operations:
        balance += operation
        if balance < 0:
            balance_never_negative = False
            break
        if operation > 0:
            if smallest_deposit is None or operation < smallest_deposit:
                smallest_deposit = operation
        elif operation < 0:
            if largest_withdrawal is None or operation > largest_withdrawal:
                largest_withdrawal = operation
    return (largest_withdrawal, smallest_deposit, not balance_never_negative)