def crossword_validator(grid: list, words: list) -> bool:
    grid_t = list(map(list, zip(*grid)))
    for word in words:
        if not any((''.join(row) in ''.join(word) for row in grid)):
            if not any((''.join(col) in ''.join(word) for col in grid_t)):
                if not any((''.join(row[::-1]) in ''.join(word) for row in grid)):
                    if not any((''.join(col[::-1]) in ''.join(word) for col in grid_t)):
                        return False
    return True