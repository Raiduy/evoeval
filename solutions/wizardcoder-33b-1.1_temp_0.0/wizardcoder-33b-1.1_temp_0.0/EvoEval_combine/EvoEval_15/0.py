from typing import List

def balance_triples(operations: List[int]) -> bool:
    balance = 0
    sums = set()
    for operation in operations:
        balance += operation
        if balance in sums:
            return True
        sums.add(balance)
    return False