def transform_canvas(canvas: str) -> str:
    if canvas.count('P') != 1:
        return 'Invalid canvas'
    painter_index = canvas.index('P')
    if canvas.count('-') % 2 == 0:
        return 'Invalid canvas'
    canvas_list = list(canvas)
    for i in range(painter_index + 1, len(canvas_list)):
        if canvas_list[i] == '-':
            canvas_list[i] = '*'
        elif canvas_list[i] == '#':
            break
    for i in range(painter_index - 1, -1, -1):
        if canvas_list[i] == '-':
            canvas_list[i] = '*'
        elif canvas_list[i] == '#':
            break
    return ''.join(canvas_list)