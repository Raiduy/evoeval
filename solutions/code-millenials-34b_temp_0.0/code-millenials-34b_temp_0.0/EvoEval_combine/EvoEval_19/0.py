from typing import List, Tuple, Optional

def account_operations(operations: List[int]) -> Tuple[Optional[int], Optional[int], bool]:
    balance = 0
    max_withdrawal = None
    min_deposit = None
    negative_balance = False
    for op in operations:
        balance += op
        if balance < 0:
            negative_balance = True
            break
        if op < 0 and (max_withdrawal is None or op > max_withdrawal):
            max_withdrawal = op
        elif op > 0 and (min_deposit is None or op < min_deposit):
            min_deposit = op
    return (max_withdrawal, min_deposit, negative_balance)