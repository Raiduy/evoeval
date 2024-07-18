from typing import List, Tuple

def account_balance(operations: List[Tuple[str, int]], daily_limit: int) -> str:
    balance = 0
    daily_withdrawal = 0
    for (operation, amount) in operations:
        if operation == 'deposit':
            balance += amount
        elif operation == 'withdrawal':
            if daily_withdrawal + amount > daily_limit:
                return 'Daily limit exceeded'
            if balance - amount < 0:
                return 'Balance below zero'
            balance -= amount
            daily_withdrawal += amount
    return 'All operations successful'