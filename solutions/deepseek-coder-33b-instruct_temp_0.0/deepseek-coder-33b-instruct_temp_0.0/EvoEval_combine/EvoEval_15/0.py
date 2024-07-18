from typing import List

def balance_triples(operations: List[int]) -> bool:
    balance = 0
    sums = []
    for operation in operations:
        balance += operation
        sums.append(balance)
        if balance < 0:
            return False
    sums.sort()
    for i in range(len(sums) - 2):
        if sums[i] == sums[i + 1] == sums[i + 2]:
            return True
    return False