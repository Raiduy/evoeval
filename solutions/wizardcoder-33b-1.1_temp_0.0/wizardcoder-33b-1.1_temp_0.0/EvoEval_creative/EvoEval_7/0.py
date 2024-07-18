def find_shangri_la(code_sequence: list[int]) -> str:
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
    if x == 0 and y == 0 and code_sequence:
        return 'Shangri-La found'
    else:
        return 'Shangri-La not found'