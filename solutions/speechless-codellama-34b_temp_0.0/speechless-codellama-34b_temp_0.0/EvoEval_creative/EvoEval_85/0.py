def princess_rescue(coord, grid):
    min_moves = float('inf')

    def dfs(row, col, moves):
        if row < 0 or col < 0 or row >= len(grid) or (col >= len(grid[0])) or (grid[row][col] == 1):
            return
        if (row, col) == coord:
            nonlocal min_moves
            min_moves = min(min_moves, moves)
            return
        dfs(row - 1, col, moves + 1)
        dfs(row, col - 1, moves + 1)
    dfs(0, 0, 0)
    return min_moves if min_moves != float('inf') else -1