def transform_canvas(canvas: str) -> str:
    if canvas.count('P') != 1:
        return 'Invalid canvas'
    painter_index = canvas.index('P')
    empty_spaces = canvas.count('-')
    if empty_spaces % 2 != 0:
        return 'Invalid canvas'
    updated_canvas = list(canvas)
    updated_canvas[painter_index] = '*'
    for i in range(painter_index + 1, len(canvas)):
        if canvas[i] == '#':
            break
        if canvas[i] == '-':
            updated_canvas[i] = '*'
    for i in range(painter_index - 1, -1, -1):
        if canvas[i] == '#':
            break
        if canvas[i] == '-':
            updated_canvas[i] = '*'
    return ''.join(updated_canvas)