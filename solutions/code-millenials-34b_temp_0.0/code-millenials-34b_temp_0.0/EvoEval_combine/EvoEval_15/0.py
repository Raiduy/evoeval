from typing import List

def balance_triples(operations: List[int]) -> bool:
    balance = 0
    triples = 0
    seen_balances = set()
    for op in operations:
        balance += op
        if balance < 0:
            return False
        if balance == 0 and balance not in seen_balances:
            seen_balances.add(balance)
            triples += 1
        if triples >= 3:
            return True
    return False