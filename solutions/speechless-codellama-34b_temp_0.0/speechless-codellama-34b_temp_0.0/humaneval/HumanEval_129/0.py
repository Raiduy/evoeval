
def minPath(grid, k):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    min_path = [0] * k
    min_path_val = float('inf')

    def dfs(row, col, path, path_val):
        nonlocal min_path, min_path_val
        if len(path) == k:
            if path_val < min_path_val:
                min_path = path[:]
                min_path_val = path_val
            return
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n and not visited[new_row][new_col]:
                visited[new_row][new_col] = True
                path.append(grid[new_row][new_col])
                dfs(new_row, new_col, path, path_val + grid[new_row][new_col])
                visited[new_row][new_col] = False
                path.pop()

    for row in range(n):
        for col in range(n):
            visited[row][col] = True
            dfs(row, col, [grid[row][col]], grid[row][col])
            visited[row][col] = False

    return min_path
