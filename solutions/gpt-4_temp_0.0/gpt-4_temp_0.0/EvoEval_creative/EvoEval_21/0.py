def crossword_validator(grid: list, words: list) -> bool:
    n = len(grid)
    for word in words:
        found = False
        for i in range(n):
            if ''.join(grid[i]) == word or ''.join(grid[i][::-1]) == word:
                found = True
                break
            if ''.join([grid[j][i] for j in range(n)]) == word or ''.join([grid[j][i] for j in range(n)][::-1]) == word:
                found = True
                break
        if not found:
            return False
    return True