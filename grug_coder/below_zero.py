from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for o in operations:
        balance += o
        if balance < 0:
            return True
    return False