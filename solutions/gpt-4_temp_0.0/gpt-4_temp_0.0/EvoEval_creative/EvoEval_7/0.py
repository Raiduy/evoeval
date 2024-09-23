def find_shangri_la(code_sequence: list[int]) -> str:
    """
    You are an explorer trying to find the mythical city of Shangri-La. According to an ancient text,
    Shangri-La can be found by following a code sequence of numbers, each referring to the direction to move.
    The directions correspond to 0: North, 1: East, 2: South, 3: West.
    
    Implement a function that takes a sequence of numbers as input and returns whether the sequence leads to Shangri-La.
    Assume starting point is always (0,0). If the sequence leads back to the starting point, it has found Shangri-La and 
    function should return 'Shangri-La found'. Otherwise, return 'Shangri-La not found'.
    Not moving is considered as not found.
    
    Note: Every move is considered as unit = 1.

    Example:
    >>> find_shangri_la([0, 1, 2, 3])
    'Shangri-La found'
    
    >>> find_shangri_la([0, 1, 0, 3])
    'Shangri-La not found'
    """
    (x, y) = (0, 0)
    for direction in code_sequence:
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x -= 1
    if x == 0 and y == 0:
        return 'Shangri-La found'
    else:
        return 'Shangri-La not found'