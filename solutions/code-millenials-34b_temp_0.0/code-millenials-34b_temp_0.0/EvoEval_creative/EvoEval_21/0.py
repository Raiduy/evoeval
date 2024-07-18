def crossword_validator(grid, words):

    def search(word, grid, i, j, dx, dy):
        for k in range(len(word)):
            if grid[i + k * dy][j + k * dx] != word[k]:
                return False
        return True

    def find_word(word, grid):
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if search(word, grid, i, j, 1, 0) or search(word, grid, i, j, 0, 1) or search(word, grid, i, j, -1, 0) or search(word, grid, i, j, 0, -1):
                    return True
        return False
    return all((find_word(word, grid) for word in words))