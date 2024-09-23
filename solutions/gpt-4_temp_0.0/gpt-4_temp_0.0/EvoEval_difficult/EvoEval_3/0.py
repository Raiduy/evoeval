from typing import List, Tuple

def account_balance(operations: List[Tuple[str, int]], daily_limit: int) -> str:
    balance = 0
    daily_withdrawal = 0
    for (operation, amount) in operations:
        if operation == 'deposit':
            balance += amount
        elif operation == 'withdrawal':
            balance -= amount
            daily_withdrawal += amount
            if daily_withdrawal > daily_limit:
                return 'Daily limit exceeded'
            if balance < 0:
                return 'Balance below zero'
        daily_withdrawal = 0
    return 'All operations successful'