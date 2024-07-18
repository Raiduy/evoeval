
def minPath(grid, k):
    n = len(grid)
    visited = set()
    ans = []

    def dfs(x, y, k, path):
        if k == 0:
            ans.append(path.copy())
            return
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] not in visited:
                visited.add(grid[nx][ny])
                path.append(grid[nx][ny])
                dfs(nx, ny, k - 1, path)
                path.pop()
                visited.remove(grid[nx][ny])

    for i in range(n):
        for j in range(n):
            visited.add(grid[i][j])
            dfs(i, j, k - 1, [grid[i][j]])
            visited.remove(grid[i][j])

    ans.sort()
    return ans[0]
