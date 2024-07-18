from typing import List, Tuple, Optional

def account_operations(operations: List[int]) -> Tuple[Optional[int], Optional[int], bool]:
    balance = 0
    largest_withdrawal = None
    smallest_deposit = None
    balance_falls_below_zero = False
    for operation in operations:
        balance += operation
        if operation < 0 and (largest_withdrawal is None or operation < largest_withdrawal):
            largest_withdrawal = operation
        if operation > 0 and (smallest_deposit is None or operation < smallest_deposit):
            smallest_deposit = operation
        if balance < 0:
            balance_falls_below_zero = True
    return (largest_withdrawal, smallest_deposit, balance_falls_below_zero)