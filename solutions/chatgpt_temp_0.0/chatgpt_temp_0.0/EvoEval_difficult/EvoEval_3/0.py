from typing import List, Tuple

def account_balance(operations: List[Tuple[str, int]], daily_limit: int) -> bool:
    balance = 0
    withdrawal_total = 0
    for (operation, amount) in operations:
        if operation == 'deposit':
            balance += amount
        elif operation == 'withdrawal':
            withdrawal_total += amount
            if withdrawal_total > daily_limit:
                return 'Daily limit exceeded'
            balance -= amount
        if balance < 0:
            return 'Balance below zero'
    return 'All operations successful'