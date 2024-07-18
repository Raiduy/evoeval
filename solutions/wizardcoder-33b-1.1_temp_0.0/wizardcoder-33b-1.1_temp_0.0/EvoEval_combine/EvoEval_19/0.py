from typing import List, Tuple, Optional

def account_operations(operations: List[int]) -> Tuple[Optional[int], Optional[int], bool]:
    balance = 0
    min_deposit = None
    max_withdrawal = None
    falls_below_zero = False
    for operation in operations:
        if operation > 0:
            if min_deposit is None or operation < min_deposit:
                min_deposit = operation
        elif max_withdrawal is None or operation > max_withdrawal:
            max_withdrawal = operation
        balance += operation
        if balance < 0:
            falls_below_zero = True
    return (max_withdrawal, min_deposit, falls_below_zero)