from typing import List

def multiple_greatest_common_divisors(numbers: List[int]) -> int:
    gcd = numbers[0]
    for i in range(1, len(numbers)):
        gcd = math.gcd(gcd, numbers[i])
    if gcd == 1:
        return -1
    else:
        return gcd