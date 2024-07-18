def check_grids(grid):
    for row in range(0,9,3):
        for col in range(0,9,3):
            nums = grid[row][col:col+3] + grid[row+1][col:col+3] + grid[row+2][col:col+3]
            if len(set(nums)) != 9 or 0 in nums:
                return False
    return True

def check_rows(grid):
    for row in grid:
        if len(set(row)) != 9 or 0 in row:
            return False
    return True

def check_columns(grid):
    for col in range(9):
        check = []
        for row in grid:
            check.append(row[col])
        if len(set(check)) != 9 or 0 in check:
            return False
    return True
def correct_sudoku(grid):
    """A Sudoku puzzle is a grid of 81 squares. Its grid will consist of 9 rows and columns, making 81 squares total. 
    Each row and column should fit the numbers 1 to 9 without repeating any numbers within the row, column, or square.

    You are given a 9x9 2D array representing a Sudoku grid (as nested lists).

    Write a function correct_sudoku which accepts this grid as its parameter.

    Your task is to return True if this Sudoku grid is correct and False otherwise.
    """
    return check_rows(grid) and check_columns(grid) and check_grids(grid)