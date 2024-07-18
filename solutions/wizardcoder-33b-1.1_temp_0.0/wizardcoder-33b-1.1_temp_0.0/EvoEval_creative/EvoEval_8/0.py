def transform_canvas(canvas: str) -> str:
    if canvas.count('P') != 1:
        return 'Invalid canvas'
    painter_index = canvas.index('P')
    left_part = canvas[:painter_index]
    right_part = canvas[painter_index + 1:]
    left_part = left_part[::-1]
    right_part = right_part[::-1]
    left_wall_index = left_part.find('#') if '#' in left_part else len(left_part)
    right_wall_index = right_part.find('#') if '#' in right_part else len(right_part)
    left_part = left_part[:left_wall_index].replace('-', '*') + left_part[left_wall_index:]
    right_part = right_part[:right_wall_index].replace('-', '*') + right_part[right_wall_index:]
    canvas = left_part[::-1] + 'P' + right_part[::-1]
    if canvas.count('*') % 2 != 0:
        return 'Invalid canvas'
    return canvas