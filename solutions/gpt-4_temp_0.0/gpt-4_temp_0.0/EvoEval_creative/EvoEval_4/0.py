from typing import List


def candles_relight(candles: List[int]) -> int:
    """
    You've got a list representing a row of birthday candles of various heights.
    A candle at position "i" can be lit (gets the flame) if it is taller than all the candles 
    before it. The first candle is always lit. 
    Your task is to return the number of candles that can be lit.
    An empty list means there were no candles, so return 0.

    >>> candles_relight([3, 2, 1, 3, 2, 4])
    2
    >>> candles_relight([1, 2, 3, 4, 5])
    5
    >>> candles_relight([])
    0
    """
    if not candles:
        return 0
    lit_candles = 1
    max_height = candles[0]
    for candle in candles[1:]:
        if candle > max_height:
            lit_candles += 1
            max_height = candle
    return lit_candles