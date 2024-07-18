def crossword_validator(grid: list, words: list) -> bool:
    n = len(grid)

    def word_in_line(word, line):
        return word in line or word[::-1] in line
    for word in words:
        word_found = False
        for i in range(n):
            if word_in_line(word, ''.join(grid[i])):
                word_found = True
                break
            column = ''.join([grid[j][i] for j in range(n)])
            if word_in_line(word, column):
                word_found = True
                break
        if not word_found:
            return False
    return True