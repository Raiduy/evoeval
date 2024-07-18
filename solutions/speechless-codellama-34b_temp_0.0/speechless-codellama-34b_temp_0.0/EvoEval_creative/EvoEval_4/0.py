from typing import List


def candles_relight(candles: List[int]) -> int:
    if not candles:
        return 0
    lit_candles = 1
    max_height = candles[0]
    for i in range(1, len(candles)):
        if candles[i] > max_height:
            lit_candles += 1
            max_height = candles[i]
    return lit_candles