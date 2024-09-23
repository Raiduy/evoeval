from typing import List

def balance_triples(operations: List[int]) -> bool:
    balance = 0
    zero_count = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return False
        if balance == 0:
            zero_count += 1
    return zero_count >= 3