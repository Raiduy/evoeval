from typing import List

def balance_triples(operations: List[int]) -> bool:
    balance = 0
    count = 0
    for op in operations:
        balance += op
        if balance == 0:
            count += 1
        if balance < 0:
            return False
    return count >= 3