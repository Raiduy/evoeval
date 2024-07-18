from typing import List


def candles_relight(candles: List[int]) -> int:
    if not candles:
        return 0
    lit_candles = 1
    max_height = candles[0]
    for candle in candles[1:]:
        if candle > max_height:
            lit_candles += 1
            max_height = candle
    return lit_candles