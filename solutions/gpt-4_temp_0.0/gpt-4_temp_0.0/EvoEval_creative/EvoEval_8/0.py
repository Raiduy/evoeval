def transform_canvas(canvas: str) -> str:
    if canvas.count('P') != 1:
        return 'Invalid canvas'
    painter_index = canvas.index('P')
    left_canvas = canvas[:painter_index]
    right_canvas = canvas[painter_index + 1:]
    for i in range(len(left_canvas) - 1, -1, -1):
        if left_canvas[i] == '-':
            left_canvas = left_canvas[:i] + '*' + left_canvas[i + 1:]
        elif left_canvas[i] == '#':
            break
    for i in range(len(right_canvas)):
        if right_canvas[i] == '-':
            right_canvas = right_canvas[:i] + '*' + right_canvas[i + 1:]
        elif right_canvas[i] == '#':
            break
    painted_canvas = left_canvas + 'P' + right_canvas
    if painted_canvas.count('*') % painted_canvas.count('-') == 0:
        return 'Invalid canvas'
    return painted_canvas