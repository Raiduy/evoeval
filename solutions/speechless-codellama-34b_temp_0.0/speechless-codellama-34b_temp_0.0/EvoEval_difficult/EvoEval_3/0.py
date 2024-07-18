from typing import List, Tuple

def account_balance(operations: List[Tuple[str, int]], daily_limit: int) -> str:
    balance = 0
    daily_withdrawal = 0
    for operation in operations:
        if operation[0] == 'deposit':
            balance += operation[1]
        elif operation[0] == 'withdrawal':
            balance -= operation[1]
            daily_withdrawal += operation[1]
        if daily_withdrawal > daily_limit:
            return 'Daily limit exceeded'
        if balance < 0:
            return 'Balance below zero'
    return 'All operations successful'