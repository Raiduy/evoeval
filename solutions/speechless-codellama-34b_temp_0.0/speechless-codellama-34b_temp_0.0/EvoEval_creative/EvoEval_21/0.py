def crossword_validator(grid: list, words: list):
    n = len(grid)
    for word in words:
        for i in range(n):
            for j in range(n):
                if grid[i][j] == word[0]:
                    if i > 0 and grid[i - 1][j] == word[1]:
                        if i > 1 and grid[i - 2][j] == word[2]:
                            if i > 2 and grid[i - 3][j] == word[3]:
                                return True
                        elif j > 0 and grid[i][j - 1] == word[1]:
                            if j > 1 and grid[i][j - 2] == word[2]:
                                if j > 2 and grid[i][j - 3] == word[3]:
                                    return True
                    elif j > 0 and grid[i][j - 1] == word[1]:
                        if j > 1 and grid[i][j - 2] == word[2]:
                            if j > 2 and grid[i][j - 3] == word[3]:
                                return True
                    elif i < n - 1 and grid[i + 1][j] == word[1]:
                        if i < n - 2 and grid[i + 2][j] == word[2]:
                            if i < n - 3 and grid[i + 3][j] == word[3]:
                                return True
                    elif j < n - 1 and grid[i][j + 1] == word[1]:
                        if j < n - 2 and grid[i][j + 2] == word[2]:
                            if j < n - 3 and grid[i][j + 3] == word[3]:
                                return True
    return False