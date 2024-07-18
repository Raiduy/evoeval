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
    return check_grids(grid) and check_rows(grid) and check_columns(grid)