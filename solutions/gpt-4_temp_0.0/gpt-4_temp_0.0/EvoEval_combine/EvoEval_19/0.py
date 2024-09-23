from typing import List, Tuple, Optional

def account_operations(operations: List[int]) -> Tuple[Optional[int], Optional[int], bool]:
    balance = 0
    largest_withdrawal = None
    smallest_deposit = None
    balance_below_zero = False
    for operation in operations:
        if operation < 0:
            if balance + operation < 0:
                balance_below_zero = True
                break
            elif largest_withdrawal is None or operation > largest_withdrawal:
                largest_withdrawal = operation
        elif smallest_deposit is None or operation < smallest_deposit:
            smallest_deposit = operation
        balance += operation
    return (largest_withdrawal, smallest_deposit, balance_below_zero)