def transform_canvas(canvas: str) -> str:
    if canvas.count('P') != 1:
        return 'Invalid canvas'
    painted_canvas = list(canvas)
    painter_index = canvas.find('P')
    empty_spaces = canvas.count('-')
    for i in range(painter_index - 1, -1, -1):
        if painted_canvas[i] == '-':
            painted_canvas[i] = '*'
        else:
            break
    for i in range(painter_index + 1, len(painted_canvas)):
        if painted_canvas[i] == '-':
            painted_canvas[i] = '*'
        else:
            break
    painted_spaces = painted_canvas.count('*')
    if empty_spaces > 0 and painted_spaces > 0 and (empty_spaces % painted_spaces == 0):
        return 'Invalid canvas'
    return ''.join(painted_canvas)